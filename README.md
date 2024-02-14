# API Automation Testing 
## Setup
1. 安裝 venv<br/>
`python3.7 -m venv venv`<br/>
2. 加載 venv<br/>
`source ./venv/bin/activate`<br/>
3. 安裝依賴套件<br/>
`python -m pip install -U pip setuptools`<br/>
`pip install -r requirements.txt`<br/>
4. 安裝 Allure 外部套件<br/>
`brew install allure`<br/>
沒有 brew 就需要再安裝<br/>
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
## 執行方式<br/>
`python startup.py`<br/>
## 產出報告<br/>
`allure serve report/json`<br/><br/>
![](doc/allurereport.png)
## 架構圖<br/>
![](doc/apitestingframediagram.png)
## 流程圖<br/>
![](doc/apitestingflow.png)
