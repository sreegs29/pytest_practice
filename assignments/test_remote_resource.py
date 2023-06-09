from paramiko.client import SSHClient
from scp import SCPClient
import ssl
import smtplib
from email.message import EmailMessage

SSH_USER = "gs-3922"
SSH_PASSWORD = "root"
SSH_HOST = "192.168.56.101"
SSH_PORT = 22


def send_email(subject, body):

    email_sender = "nairsanju98@gmail.com"
    email_password = 'qdcdmqplggiriljo'
    email_receiver = "nairsreejish@gmail.com"

    subject = subject
    body = body

    em = EmailMessage()

    em['Subject'] = subject
    em['From'] = email_sender
    em['To'] = email_receiver
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    s = smtplib.SMTP('localhost')
    s.sendmail(email_sender, [email_receiver], em.as_string())
    s.quit()


def test_remote_resource():
    client = SSHClient()
    client.load_system_host_keys()

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
    res = stdout.read().decode()
    # print(res)

    resource = res.splitlines()[13]
    # print("Resource==>", resource)

    cpu = float(resource.split(" ")[2].strip(","))
    ram = float(resource.split(" ")[5])
    # print(cpu,ram)

    with open("./resource.txt", mode="w") as resource_file:
        file = res.splitlines()
        for line in file:
            resource_file.writelines(f"{line}\n")
        print("Output generated on the file 'resource.txt'")

    if cpu > 20 or ram > 20:
        subject = "Resource Usage Alert"
        body = f"Alert: CPU Usage: {cpu}%\nRAM Usage: {ram}%"
        send_email(subject, body)

    client.close()


test_remote_resource()

