import paramiko
import getpass
import time

HOST = "172.168.10.111"
username = input("Please enter your username: ")
password = getpass.getpass()

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(HOST,username=username,password=password,look_for_keys=False)

ssh_connecion = ssh_client.invoke_shell()

ssh_connecion.send("show ip route\n")

output = ssh_connecion.recv(65535).decode(encoding="utf-8")

print (output)

ssh_connecion.send("show ip int brief\n")
time.sleep(.5)
output = ssh_connecion.recv(65535)
print (output)

ssh_connecion.close