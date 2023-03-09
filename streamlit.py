import streamlit as st
import requests
import pandas as pd
import wget
import webbrowser
from bokeh.models.widgets import Div
from slack import Slack
import datetime
import pytz
import time
import sqlite3

# st.set_page_config(layout="wide")
kst = pytz.timezone('Asia/Seoul')


conn = sqlite3.connect('example.db')
df_sql = pd.read_sql_query("SELECT * FROM demo", conn)
placeholder = st.empty()



demo_sheet_url = "https://docs.google.com/spreadsheets/d/19zYpEc0SGDdFedT5Ej-JqD3IEVy2m0gO7XPbTbTiw00/edit?usp=sharing"
demo_sheet = demo_sheet_url.replace("/edit?usp=sharing", "/export?format=csv")
channel_name = 'server-bot'


def load_data(url):
    return pd.read_csv(url)

def color_status(val):
    if val == 'Not working':
        color = 'red'
    elif val == 'Working':
        color = 'green'
    else:
        color = 'black'
    return f'color: {color}'


def get_status(url):
    try:
        res = requests.get(f"{url}")
        if res.status_code == 200:
            return "Working"
    except requests.exceptions.ConnectionError:
        return "Not working"
    return "Working"




if __name__ == "__main__":
    st.title("NLP & AI Sever status")

    if st.button("Demo Spreadsheet"):
        js = f"window.open('{demo_sheet_url}')"  # New tab or window
        # js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

    demo = df_sql
    tasks = demo.task.unique()

    for task in tasks:
        st.write(f"### {task}")
        df = demo[demo.task == task]
        # df["status"] = df.url.apply(get_status)
        st.table(df[["name", "status"]].style.applymap(color_status, subset=['status']))



    # while True:
    #     placeholder.text(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    #     time.sleep(10) # 10초마다 새로고침














