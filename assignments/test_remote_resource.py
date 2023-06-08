from paramiko.client import SSHClient
from scp import SCPClient
import pytest

SSH_USER = "gs-3922"
SSH_PASSWORD = "root"
SSH_HOST = "192.168.56.101"
SSH_PORT = 22

client = SSHClient()

client.load_system_host_keys()
try:
    client.connect(SSH_HOST, port=SSH_PORT,
                   username=SSH_USER,
                   password=SSH_PASSWORD,
                   look_for_keys=False)
    print("Connected successfully!")

    with SCPClient(client.get_transport()) as scp:
        scp.put("test_usage.py", "/home/gs-3922")
        scp.put("..\conftest.py", "/home/gs-3922")

    comm = "pytest test_usage.py -v"
    client.exec_command("cd /home/gs-3922")
    stdin, stdout, stderr = client.exec_command(comm)

    with open("./resource.txt", mode="w") as resource_file:
        for line in stdout.readlines():
            resource_file.writelines(line)

except Exception:
    print("Failed to establish connection.")

finally:
    client.close()
