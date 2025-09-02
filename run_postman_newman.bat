@echo off
REM Requires Node.js and Newman installed: npm install -g newman newman-reporter-htmlextra
IF NOT EXIST reports (
    mkdir reports
)
newman run ReqRes.postman_collection.json -e ReqRes.postman_environment.json -r cli,htmlextra --reporter-htmlextra-export reports\postman-report.html
echo Report: %CD%\reports\postman-report.html
