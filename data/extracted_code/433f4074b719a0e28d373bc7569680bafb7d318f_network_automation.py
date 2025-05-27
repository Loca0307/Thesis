# Connect to a linux server using ssh and execute commands  

import paramiko
import time

def connect_and_run_command(hostname, username, password, command):
    # Create a new SSH client object
    client = paramiko.SSHClient()

    # Automatically add the server's host key
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server
    client.connect(hostname, username=username, password=password)
    shell = client.invoke_shell()
    shell.send(command)
    time.sleep(2)
    output = shell.recv(65535)
    print(output.decode('utf-8'))
    client.close()

if __name__ == "__main__":
    IP_ADDRESS='xxx.xx.xxx.xxx'
    PASSWORD='xxxxxx'
    USERNAME='xxxxxx'
    connect_and_run_command(IP_ADDRESS, USERNAME, PASSWORD, 'who;ip address\n')