import streamlit as st
import preprocess
import helper
import matplotlib.pyplot as plt
import seaborn as sns

# Sidebar
st.sidebar.title("Whatsapp Chat Analyzer")
chat = st.sidebar.file_uploader("Choose a file")

if chat is not None:
    byte_data = chat.getvalue()
    data = byte_data.decode("utf-8")
    df = preprocess.preprocess(data)

    # Fetch users
    userlist = df["user"].unique().tolist()
    userlist.remove("group_notification")
    userlist.sort()
    userlist.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt", userlist)

    if st.sidebar.button("Show Analysis"):

        # Top Stats
        num_messages, words, media_count, links_count = helper.fetch_stats(
            selected_user, df
        )

        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(words)

        with col3:
            st.header("Media Shared")
            st.title(media_count)

        with col4:
            st.header("Links Shared")
            st.title(links_count)

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
        ax.plot(monthly_df["time"], daily_df["message"], color="red")
        plt.xticks(rotation="vertical")
        st.pyplot(fig)

        # Activity Map
        st.title("Activity Map")
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most Busy Day")
            busy_day = helper.daily_activity(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values)
            st.pyplot(fig)

        with col2:
            st.header("Most Busy Month")
            busy_month = helper.monthly_activity(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color="purple")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

        # Weekly Heatmap
        st.title("Weekly Activity Map")
        user_heatmap = helper.top_daily_user(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)

        # Most Busy Users
        if selected_user == "Overall":
            st.title("Most Busy Users")
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
        st.pyplot(fig)

        # Most Common Words
        st.title("Most Common Words")
        most_common_word_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.barh(most_common_word_df[0], most_common_word_df[1])
        st.pyplot(fig)

        # Emoji Analysis
        st.title("Most Used Emojis")
        col1, col2 = st.columns(2)

        with col1:
            top_emojis = helper.top_emoji(selected_user, df)
            st.dataframe(top_emojis)

        with col2:
            fig, ax = plt.subplots()
            ax.pie(
                top_emojis["Count"].head(),
                labels=top_emojis["Emoji"].head()
            )
            st.pyplot(fig)
