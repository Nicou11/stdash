import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title('요청 / 처리 건수(h)')
#st.sidebar.page_link("streamlit.py", label="Home")
st.sidebar.page_link("pages/req_D_T.py", label="Requests by Date and Time")
st.sidebar.page_link("pages/req_pre.py", label="Request and Prediction")
st.sidebar.markdown("---")

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

font1 = {'family': 'serif',
      'color':  'darkred',
      'weight': 'normal',
      'size': 16}

df['request_time'] = pd.to_datetime(df['request_time']).dt.strftime('%Y-%m-%d %H')
df['prediction_time'] = pd.to_datetime(df['prediction_time']).dt.strftime('%Y-%m-%d %H')
req_time = df.groupby('request_time').size()
pre_time = df.groupby('prediction_time').size()

plt.title("Requests by Date and Time")
#plt.text(3.5, 220, 'High', fontdict=font1)
plt.bar(req_time.index, req_time.values, label='Request')
plt.plot(pre_time.index, pre_time.values, marker='o', color='r', label='Prediction')
plt.xlabel('Date, Time')
plt.ylabel('Count')
plt.xticks(rotation = 45)
plt.legend()

# 화면에 그리기
st.pyplot(plt)
