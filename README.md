## Demo site monitoring with Streamlit
```
이 프로젝트는 매 시간 주기적으로 데모 사이트의 상태를 체크하고, 이상이 있을 경우 Slack 봇을 통해 알림을 보내는 웹 페이지입니다.

이 프로젝트는 Python의 streamlit과 sqlite3 모듈을 활용하여 개발되었습니다. streamlit은 사용자 친화적인 인터페이스를 만드는 데 사용되며, sqlite3은 데이터베이스를 관리하는 데 사용됩니다.
```


### 실행 방법
이 리포지토리를 클론합니다.

```bash
git clone https://github.com/yourusername/site-monitoring-webpage.git
```

Python 3.x와 필요한 라이브러리를 설치합니다.

```bash
pip install -r requirements.txt
```

Sqlite3를 사용하여 데이터베이스를 생성합니다.

```bash
python create_db.py
```
웹 페이지를 실행합니다.

```bash
streamlit run streamlit.py
```
웹 브라우저에서 localhost:8501에 접속합니다.

update.py 파일을 실행하여 매 시간마다 데모 사이트의 상태를 체크하고 Slack 봇 알림을 받을 수 있습니다.

```
python update.py
````

### 기여하기
이 프로젝트에 기여하려면, 이 리포지토리를 포크하고 새로운 브랜치를 만든 다음 Pull Request를 보내주십시오.

### 라이센스
이 프로젝트는 MIT 라이센스 하에 배포됩니다. 자세한 내용은 LICENSE 파일을 참조하십시오.
