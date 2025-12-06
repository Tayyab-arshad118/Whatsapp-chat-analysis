from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

f= open('romanEng2.txt')
sw=f.read()
sw=sw.split()

def fetch_stats(selected_user,df):
    if selected_user != "Overall":
        df = df[df['user']==selected_user]

    num_messages = df.shape[0]

    words = []
    for message in df['message']:
        words.extend(message.split())
    
    media_count = df[df['message']=='<Media omitted>\n'].shape[0]

    links = []
    extract=URLExtract()
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words),media_count,len(links)
        
    
def most_active_user(df):
    x = (df[df['user'] != 'group_notification']['user']).value_counts().head(5)
    xx = round(((df[df['user'] != 'group_notification']['user']).value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'user':'Name','count':'Percent'})

    return x,xx


def wordcloud_gen(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user']==selected_user]
    wc = WordCloud(collocations=False,width=500,height=500,min_font_size=10,background_color='white',stopwords= sw)
    df_wc=wc.generate(df[(df['user'] != 'group_notification') & (df['message'] != '<Media omitted>\n')]['message'].str.lower().str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user']==selected_user]
    temp = df[(df['user'] != 'group_notification') & (df['message'] != '<Media omitted>\n')]
    words=[]
    for message in df['message']:
        for word in message.lower().split():
            if word not in sw:
                words.append(word)
    return pd.DataFrame(Counter(words).most_common(20))

def top_emoji(selected_user,df):
    df = df[df['user'] == selected_user] if selected_user != 'Overall' else df
    emojis=[]
    for words in df['message']:
        emojis.extend([c for c in words if emoji.is_emoji(c)])
    
    top_emoji = (pd.DataFrame(Counter(emojis).most_common(25)))
    return top_emoji.rename(columns={0: 'Emoji', 1: 'Count'})


def monthly_timeline(selected_user,df):
    df = df[df['user'] == selected_user] if selected_user != 'Overall' else df
    timeline = df.groupby(['year','month','month_name'])['message'].count().reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(str(timeline['month'][i]) + "-" + str(timeline['year'][i]))
    timeline['time']=time
    return timeline


def daily_timeline(selected_user,df):
    df = df[df['user'] == selected_user] if selected_user != 'Overall' else df
    daily = df.groupby('date')['message'].count().reset_index()
    return daily

def monthly_activity(selected_user,df):
    df = df[df['user'] == selected_user] if selected_user != 'Overall' else df
    return df['month_name'].value_counts()


def daily_activity(selected_user,df):
    df = df[df['user'] == selected_user] if selected_user != 'Overall' else df
    return df['day_name'].value_counts()

def top_daily_user(selected_user,df):
    df = df[df['user'] == selected_user] if selected_user != 'Overall' else df
    return df.pivot_table(index='day_name',columns='period',values='message',aggfunc='count').fillna(0)
 



    
