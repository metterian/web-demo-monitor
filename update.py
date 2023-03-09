#%%
import datetime
from enum import Enum, auto
import sqlite3

import pandas as pd
import pytz
import requests
from slack import Slack
from dataclasses import dataclass

from secret import slack_token


kst = pytz.timezone('Asia/Seoul')
demo_sheet_url = "https://docs.google.com/spreadsheets/d/19zYpEc0SGDdFedT5Ej-JqD3IEVy2m0gO7XPbTbTiw00/edit?usp=sharing"
demo_sheet = demo_sheet_url.replace("/edit?usp=sharing", "/export?format=csv")
slack = Slack(slack_token)
channel_name = 'server-bot'

@dataclass
class Status:
    working = "working"
    not_working = "not working"

def get_status(url) -> Status:
    try:
        res = requests.get(f"{url}")
        if res.status_code == 200:
            return Status.working
    except requests.exceptions.ConnectionError:
        return Status.not_working
    return Status.working

# conn = sqlite3.connect('example.db') # Connection 객체 생성
# df_sql = pd.read_sql_query("SELECT * FROM demo", conn)
# df_sql = pd.read_csv(demo_sheet)
# df_sql['status'] = df_sql['url'].apply(get_status)


# check status and send slack message if status is changed
def check_status(data: pd.Series) -> Status:
    cur_status = get_status(data['url'])
    status = data['status']
    demo_name = data['name']
    demo_url = data['url']

    now = datetime.datetime.now(tz=kst)
    server_time = now.strftime("%Y-%m-%d %H:%M:%S %Z")

    if cur_status != status:
        print(f"{server_time}-{demo_name} is {cur_status}")
        channel_id = slack.get_channel_id(channel_name)
        slack.post_message(channel_id, text=f"[{server_time}] **{demo_name}** is {cur_status}\n{demo_url}")
        return cur_status
    else:
        return status


with sqlite3.connect('example.db') as conn:
    df_sql = pd.read_sql_query("SELECT * FROM demo", conn)
    df_sql['status'] = df_sql.apply(check_status, axis=1)
    df_sql.to_sql('demo', conn, if_exists='replace', index=False)


print("Done")
