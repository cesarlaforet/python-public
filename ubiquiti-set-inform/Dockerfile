FROM python:3.11

# Install cron (if not already installed)
RUN apt-get update && apt-get install -y cron

# Set the working directory
WORKDIR /app

# Copy your script and .env file into the container
COPY ubt-inform.py .
COPY requirements.txt .
COPY .env .

# Copy the wrapper script into the container
COPY wrapper.sh .

# Make the wrapper script executable
RUN chmod +x wrapper.sh

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Define environment variables for sensitive data
ENV SSH_HOSTNAME=your_ssh_hostname \
    SSH_PORT=your_ssh_port \
    SSH_USERNAME=your_ssh_username \
    SSH_PASSWORD=your_ssh_password \
    INFORM_URL=your_inform_url

# Set the entry point to the wrapper script
ENTRYPOINT ["./wrapper.sh"]
