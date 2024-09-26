import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title('CNN JOB MON')

def load_data():
    url = 'http://43.202.66.118:8006/all'
    r = requests.get(url)
    d = r.json()
    return d

data = load_data()
df = pd.DataFrame(data)

# TODO
# request_time, prediction_time 이용해서 '%Y-%m-%d %H' 형식
# 즉 시간별로 GROUP BY COUNT 하여 plt 차트 그려보기

df['request_time'] = pd.to_datetime(df['request_time'])
df['request_time'] = df['request_time'].dt.strftime('%Y-%m-%d %H')
time = df.groupby('request_time').size()

plt.bar(time.index, time.values)
plt.plot(time.index, time.values, marker='o', color='r')
plt.xlabel('Request Time')
plt.ylabel('Count')


# 화면에 그리기
st.pyplot(plt)
