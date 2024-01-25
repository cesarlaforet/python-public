#!/bin/bash

# Load environment variables from .env
set -a
source /app/.env
set +a

# Add your cron job to a temporary file
echo "*/30 * * * * /usr/local/bin/python /app/ubt-inform.py >> /app/cron.log 2>&1" > /app/cron.tmp

# Add the cron job and start the cron daemon
crontab /app/cron.tmp
cron -f
