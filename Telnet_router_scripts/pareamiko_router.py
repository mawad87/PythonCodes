import paramiko
import getpass
import time

HOST = "172.168.10.111"
USR = input("Enter your Username: ")
PASS = getpass.getpass()

ssh_client = paramiko.SSHClient()
ssh_connecion = ssh_client.invoke_shell()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=HOST,username=USR,password=PASS)

ssh_connecion.send("show ip route\n")

output = ssh_connecion.recv(11111).decode(encodings="utf-8")

print(output)

ssh_connecion.close