# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python packages
RUN pip install paramiko

# Create a cron job to run the script every 30 minutes
RUN echo "*/30 * * * * /usr/bin/python /app/ubt-inform.py" > /etc/cron.d/your_cron_job
RUN chmod 0644 /etc/cron.d/your_cron_job
RUN crontab /etc/cron.d/your_cron_job

# Run the command on container startup
CMD ["cron", "-f"]
