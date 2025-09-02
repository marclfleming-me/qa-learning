@echo off
REM Create venv if not exists
IF NOT EXIST .venv (
    python -m venv .venv
)

CALL .venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Make reports directory
IF NOT EXIST reports (
    mkdir reports
)

REM Run pytest with HTML report
pytest -v --html=reports\test-report.html --self-contained-html

echo.
echo Report generated at: %CD%\reports\test-report.html
