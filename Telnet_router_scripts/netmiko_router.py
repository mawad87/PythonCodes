from netmiko import ConnectHandler

IOU1 = {
	'device_type': 'cisco_ios',
	'host': '172.168.10.111',
	'username': 'cisco',
	'password': 'cisco',
	'secret':'cisco'
}

net_connect = ConnectHandler(**IOU1)

net_connect.enable()

output = net_connect.send_command("show ip route")

print (output)