import paramiko
import time
import re
import configparser
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the config.ini file
config_file = os.path.join(script_dir, 'config.ini')

# Check if config.ini exists, and create a template if not
if not os.path.exists(config_file):
    with open(config_file, 'w') as config_template:
        config_template.write('[SSH]\n')
        config_template.write('hostname = \n')
        config_template.write('port = \n')
        config_template.write('username = \n')
        config_template.write('password = \n')
        config_template.write('\n')
        config_template.write('[URL]\n')
        config_template.write('inform_url = \n')
    print("A template config.ini file has been created. Please fill in the details.")
    exit(1)

# Read sensitive data from the configuration file
config = configparser.ConfigParser()
config.read(config_file)

hostname = config['SSH']['hostname']
port = int(config['SSH']['port'])
username = config['SSH']['username']
password = config['SSH']['password']
inform_url = config['URL']['inform_url']

# SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the SSH server
    print("Connecting to SSH server...")
    client.connect(hostname, port, username, password)
    print("Connected to SSH server")

    # Open an SSH shell
    shell = client.invoke_shell()

    # Send the 'info' command
    shell.send("info\n")

    # Wait for a short moment to allow the response to arrive
    time.sleep(2)

    # Receive and process the output
    output = shell.recv(65535).decode("utf-8")
    print(output)

    # Use a regular expression to extract the Status
    status_match = re.search(r"Status:\s+(.*)", output)

    if status_match:
        status = status_match.group(1)
        if "Connected" in status:
            print("Status: Connected")
        else:
            print("Status is not Connected")

            # Send the 'set-inform' command
            shell.send("set-inform http://10.0.0.140:8080/inform\n")

            # Wait for a short moment to allow the response to arrive
            time.sleep(2)

            output2 = shell.recv(65535).decode("utf-8")
            print(output2)
    else:
        print("Status not found in the output")

    # Close the SSH shell
    shell.close()

    # Close the SSH client
    client.close()

except paramiko.AuthenticationException:
    print("Authentication failed, please check your credentials.")
except paramiko.SSHException as e:
    print(f"SSH connection failed: {str(e)}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
