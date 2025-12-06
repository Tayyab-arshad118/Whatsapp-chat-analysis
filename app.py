import streamlit as st
import preprocess
import helper
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# Custom CSS Styling
# ------------------------------------------
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        color: #4CAF50;
        margin-top: 30px;
    }
    .sub-text {
        text-align: center;
        font-size: 1.2rem;
        opacity: 0.8;
        margin-bottom: 40px;
    }
    .upload-box {
        padding: 30px;
        border-radius: 15px;
        border: 2px dashed #4CAF50;
        text-align: center;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)


# ------------------------------------------
# Sidebar
# ------------------------------------------
st.sidebar.title("Whatsapp Chat Analyzer")
chat = st.sidebar.file_uploader("Upload exported chat (.txt file)")


# ------------------------------------------
# BEFORE UPLOAD → Show a clean landing page
# ------------------------------------------
if chat is None:
    st.markdown("<h1 class='main-title'>WhatsApp Chat Analyzer</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='sub-text'>Analyze your chat’s messages, emojis, media, timelines and more!</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="upload-box">
            <h3>➡ Upload your WhatsApp chat file using the sidebar ☝</h3>
            <p>The analysis will appear automatically after upload.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.stop()  # Stop here until file is uploaded


# ------------------------------------------
# AFTER UPLOAD → Run analysis
# ------------------------------------------
byte_data = chat.getvalue()
data = byte_data.decode("utf-8")
df = preprocess.preprocess(data)

# Fetch users
userlist = df["user"].unique().tolist()
if "group_notification" in userlist:
    userlist.remove("group_notification")
userlist.sort()
userlist.insert(0, "Overall")

selected_user = st.sidebar.selectbox("Show analysis for:", userlist)

if st.sidebar.button("Run Analysis 🚀"):

    # Top Stats
    num_messages, words, media_count, links_count = helper.fetch_stats(selected_user, df)

    st.title("Top Statistics")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Messages", num_messages)

    with col2:
        st.metric("Total Words", words)

    with col3:
        st.metric("Media Shared", media_count)

    with col4:
        st.metric("Links Shared", links_count)

    # Monthly Timeline
    st.title("Monthly Timeline")
    monthly_df = helper.monthly_timeline(selected_user, df)
    fig, ax = plt.subplots()
    ax.plot(monthly_df["time"], monthly_df["message"], color="black")
    plt.xticks(rotation="vertical")
    st.pyplot(fig)

    # Daily Timeline
    st.title("Daily Timeline")
    daily_df = helper.daily_timeline(selected_user, df)
    fig, ax = plt.subplots()
    ax.plot(daily_df["date"], daily_df["message"], color="red")
    plt.xticks(rotation="vertical")
    st.pyplot(fig)

    # Activity Map
    st.title("Activity Map")
    col1, col2 = st.columns(2)

    with col1:
        st.header("Busiest Day")
        busy_day = helper.daily_activity(selected_user, df)
        fig, ax = plt.subplots()
        ax.bar(busy_day.index, busy_day.values)
        st.pyplot(fig)

    with col2:
        st.header("Busiest Month")
        busy_month = helper.monthly_activity(selected_user, df)
        fig, ax = plt.subplots()
        ax.bar(busy_month.index, busy_month.values, color="purple")
        plt.xticks(rotation="vertical")
        st.pyplot(fig)

    # Heatmap
    st.title("Weekly Activity Heatmap")
    user_heatmap = helper.top_daily_user(selected_user, df)
    fig, ax = plt.subplots()
    sns.heatmap(user_heatmap, ax=ax)
    st.pyplot(fig)

    # Most Busy Users
    if selected_user == "Overall":
        st.title("👥 Most Active Users")
        x, xx = helper.most_active_user(df)

        col1, col2 = st.columns(2)

        with col1:
            fig, ax = plt.subplots()
            ax.bar(x.index, x.values, color="red")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

        with col2:
            st.dataframe(xx)

    # WordCloud
    st.title("WordCloud")
    wc = helper.wordcloud_gen(selected_user, df)
    fig, ax = plt.subplots()
    ax.imshow(wc)
    ax.axis("off")
    st.pyplot(fig)

    # Common Words
    st.title("Most Common Words")
    common_df = helper.most_common_words(selected_user, df)
    fig, ax = plt.subplots()
    ax.barh(common_df[0], common_df[1])
    st.pyplot(fig)

    # Emoji Analysis
    st.title("Emoji Usage")
    col1, col2 = st.columns(2)

    with col1:
        emoji_df = helper.top_emoji(selected_user, df)
        st.dataframe(emoji_df)

    with col2:
        fig, ax = plt.subplots()
        ax.pie(emoji_df["Count"].head(), labels=emoji_df["Emoji"].head())
        st.pyplot(fig)
