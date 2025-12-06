import re
import pandas as pd
import numpy as np
import streamlit as st

def preprocess(data):
    pattern = '\d{1,2}\/\d{1,2}\/\d{2},\s\d{1,2}:\d{2}\s(?:AM|PM)\s-\s'


    messages = re.split(pattern,data)[1:]
    pattern_for_date = r'(\d{1,2}\/\d{1,2}\/\d{2}),\s(\d{1,2}:\d{2})\u202f(AM|PM)\s-\s'
    dates= re.findall(pattern_for_date, data)
    dates = [f"{date}, {time} {meridiem}" for date, time, meridiem in dates]

    df = pd.DataFrame({'user_message':messages,'messages-date':dates})
    df['messages-date']=pd.to_datetime(df['messages-date'],format='%m/%d/%y, %I:%M %p')


    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:# user name
            users.append(entry[1])
            messages. append(entry[2])
        else:
            users. append('group_notification' )
            messages.append(entry[0])

    df['user' ] = users
    df['message' ] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['year'] = df['messages-date'].dt.year
    df['month_name'] = df['messages-date'].dt.month_name()
    df['day'] = df['messages-date'].dt.day
    df['hour'] = df['messages-date'].dt.hour
    df['minute'] = df['messages-date'].dt.minute
    df['month'] = df['messages-date'].dt.month
    df['date'] = df['messages-date'].dt.date
    df['day_name'] = df['messages-date'].dt.day_name()
    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period
    return df