#%%
import sqlite3
import pandas as pd
import requests
from slack import Slack
import datetime
import pytz
from secret import slack_token



kst = pytz.timezone('Asia/Seoul')
demo_sheet_url = "https://docs.google.com/spreadsheets/d/19zYpEc0SGDdFedT5Ej-JqD3IEVy2m0gO7XPbTbTiw00/edit?usp=sharing"
demo_sheet = demo_sheet_url.replace("/edit?usp=sharing", "/export?format=csv")
slack = Slack(slack_token)
channel_name = 'server-bot'

def get_status(url):
    try:
        res = requests.get(f"{url}")
        if res.status_code == 200:
            return "Working"
    except requests.exceptions.ConnectionError:
        return "Not working"
    return "Working"

conn = sqlite3.connect('example.db') # Connection 객체 생성
df_sql = pd.read_sql_query("SELECT * FROM demo", conn)
# df_sql = pd.read_csv(demo_sheet)
# df_sql['status'] = df_sql['url'].apply(get_status)


# check status and send slack message if status is changed
def check_status(data: pd.Series):
    cur_status = get_status(data['url'])
    status = data['status']
    demo_name = data['name']
    demo_url = data['url']

    now = datetime.datetime.now()
    kst_now = now.astimezone(kst)
    server_time = kst_now.strftime("%Y-%m-%d %H:%M:%S %Z")

    if cur_status != status:
        print(f"{server_time}-{demo_name} is {cur_status}")
        channel_id = slack.get_channel_id(channel_name)
        slack.post_message(channel_id, text=f"[{server_time}] **{demo_name}** is {cur_status}\n{demo_url}")
        return cur_status
    else:
        return status

df_sql['status'] = df_sql.apply(check_status, axis=1)


# update table
df_sql.to_sql('demo', conn, if_exists='replace', index=False)
conn.commit()
conn.close()

print("Done")
