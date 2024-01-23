# SSH Auto-Inform Script

The SSH Auto-Inform Script is designed to automate interactions with a remote SSH server, particularly useful for managing Ubiquiti routers. This script performs the following actions:

1. Connects to a remote SSH server.
2. Executes the 'info' command to retrieve device information.
3. Checks the 'Status' from the output.
4. If the 'Status' is not 'Connected,' it sends the 'set-inform' command to attempt to connect to a specified inform URL.

## Prerequisites

Before using this script, ensure you have the following:

- Python installed on your machine.
- The Paramiko library installed. You can install it using pip:
  ```
  pip install paramiko
  ```

## Configuration

Sensitive data such as the SSH server details, username, password, and inform URL should be stored in a `config.ini` file. The script will create this file if it doesn't exist. Edit the `config.ini` file to include your SSH server details and inform URL.

Example `config.ini`:
```ini
[SSH]
hostname = 
port = 
username = 
password = 

[URL]
inform_url = 
```

## Usage

1. Clone or download this script to your local machine.

2. Ensure that Python and the Paramiko library are installed as per the prerequisites.

3. Edit the `config.ini` file to include your SSH server details and inform URL.

4. Open a terminal and navigate to the directory containing the script.

5. Run the script by executing the following command:
   ```
   python ubt-inform.py
   ```

6. The script will connect to the SSH server, execute the 'info' command, and check the 'Status.'

7. If the 'Status' is not 'Connected,' the script will attempt to set the inform URL.

8. Review the script output to see the results.

## License

This script is provided under the MIT License.

Feel free to contribute or report issues on GitHub.

---

**Note:** Ensure you respect the terms of use of the SSH server and follow all applicable laws and regulations when using this script. This script is intended for legitimate use cases and should not be used for any malicious purposes.
```

You can save this Markdown content as `README.md` in the same directory as your script, and it will provide clear instructions on how to use your script along with some background information.