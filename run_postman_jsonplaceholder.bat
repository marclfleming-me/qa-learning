@echo off
REM Requires Node.js + Newman: npm install -g newman newman-reporter-htmlextra
IF NOT EXIST reports (
    mkdir reports
)
newman run JSONPlaceholder.postman_collection.json -e JSONPlaceholder.postman_environment.json -r cli,htmlextra --reporter-htmlextra-export reports\postman-jsonplaceholder.html
echo Report: %CD%\reports\postman-jsonplaceholder.html
