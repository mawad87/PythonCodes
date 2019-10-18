import paramiko
import getpass
import time

HOST = "172.168.10.111"
USER = "cisco"
PASS = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(HOST,username=USER,password=PASS,look_for_keys=False)

ssh_connecion = ssh_client.invoke_shell()

ssh_connecion.send("show ip route\n")

output = ssh_connecion.recv(11111).decode(encodings="utf-8")

print(output)

ssh_connecion.close