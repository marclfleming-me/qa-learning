@echo off
IF NOT EXIST .venv (
    python -m venv .venv
)
CALL .venv\Scripts\activate
pip install -r requirements.txt

IF NOT EXIST reports (
    mkdir reports
)

pytest -v -m api --html=reports\api-report.html --self-contained-html --base-url=https://reqres.in
echo Report: %CD%\reports\api-report.html
