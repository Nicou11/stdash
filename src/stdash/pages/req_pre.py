import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import requests

#st.title('Request and Prediction count')
#st.sidebar.page_link("streamlit.py", label="Home")
st.sidebar.page_link("pages/app.py", label="Requests by Date and Time")
st.sidebar.page_link("pages/req_pre.py", label="Request and Prediction")
st.sidebar.markdown("---")


def load_data():
    url = 'http://43.202.66.118:8016/all'
    r = requests.get(url).json()
    return r

data = load_data()
df = pd.DataFrame(data)

req = df.groupby('request_user').size().reset_index(name='req')
req.set_index('request_user', inplace=True)
req.rename_axis('user', inplace=True)
prd = df.groupby('prediction_model').size().reset_index(name='prd')
prd.set_index('prediction_model', inplace=True)
prd.rename_axis('user', inplace=True)

join_df = req.join(prd, how='left')

index = np.arange(len(join_df.index))
bar_width = 0.4
b1 = plt.bar(index, join_df['req'], bar_width, alpha=0.7, color='red', label='request')
b2 = plt.bar(index + bar_width, join_df['prd'], bar_width, alpha=0.7, color='blue', label='prediction')

plt.xlabel('Username')
plt.ylabel('Count')
plt.title('Request and Prediction count by User')
plt.xticks(index, join_df.index)
plt.legend()

st.pyplot(plt)
