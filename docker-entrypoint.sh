#!/bin/bash
#

# to spacify the running env for the app
# 
# AK_APP_ENV='dev'
AK_APP_ENV='pro'
# AK_APP_ENV='staging'
export AK_APP_ENV


# setup django-json rpc
RUN cd /app/django-json-rpc
RUN python setup.py install
RUN cd /app

# Prepare log files and start outputting logs to stdout
mkdir -p /ak/logs/gunicorn
touch /ak/logs/gunicorn/gunicorn-ak_api.log
touch /ak/logs/gunicorn/access-ak_api.log
tail -n 0 -f /ak/logs/gunicorn/*.log &

# Start Gunicorn processes
echo Starting Gunicorn.
cd /app/MainApp    #  or exec gunicorn MainApp.AKAppMain:app

exec gunicorn AKAppMain:app \
    --name AKAppMain \
    --bind 0.0.0.0:5005 \
    --workers 3 \
    --log-level=info \
    --log-file=/ak/logs/gunicorn/gunicorn-ak_api.log \
    --access-logfile=/ak/logs/gunicorn/access-ap_api.log \
    "$@"