#%%
import sqlite3
import pandas as pd
import requests



demo_sheet_url = "https://docs.google.com/spreadsheets/d/19zYpEc0SGDdFedT5Ej-JqD3IEVy2m0gO7XPbTbTiw00/edit?usp=sharing"
demo_sheet = demo_sheet_url.replace("/edit?usp=sharing", "/export?format=csv")


def get_status(url):
    try:
        res = requests.get(f"{url}")
        if res.status_code == 200:
            return "Working"
    except requests.exceptions.ConnectionError:
        return "Not working"
    return "Working"

conn = sqlite3.connect('example.db') # Connection 객체 생성
c = conn.cursor() # Cursor 객체 생성

# CREATE TABLE 문 실행
c.execute('''CREATE TABLE demo (
    task text,
    name text,
    url text
)''')


df = pd.read_csv(demo_sheet)

df.to_sql('demo', conn, if_exists='replace', index=False)


conn.commit()
conn.close()
