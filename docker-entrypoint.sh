#!/bin/bash
#

# to spacify the running env for the app
# 
# AK_APP_ENV='dev'
AK_APP_ENV='pro'
# AK_APP_ENV='staging'
export AK_APP_ENV


# Prepare log files and start outputting logs to stdout
mkdir -p /ak/logs/gunicorn
touch /ak/logs/gunicorn/gunicorn-ak_api.log
touch /ak/logs/gunicorn/access-ak_api.log
tail -n 0 -f /ak/logs/gunicorn/*.log &

# Start Gunicorn processes
echo Starting Gunicorn.
cd /app    #  or exec gunicorn MainApp.AKAppMain:app

exec gunicorn MainService.api.AKAppMain:app \
    --name AKAppMain \
    --bind 0.0.0.0:5000 \
    --workers 3 \
    --log-level=info \
    --log-file=/ak/logs/gunicorn/gunicorn-ak_api.log \
    --access-logfile=/ak/logs/gunicorn/access-ap_api.log \
    "$@"
