from netmiko import ConnectHandler
from getpass import getpass

user = input('enter your name')
secret = getpass('enter your password')

ciscoDevice = {
    'device_type' : 'cisco_ios',
    'host':'192.168.1.9',
    'username':user,
    'password':secret
}

try:
    connection = ConnectHandler(**ciscoDevice)
except(NetMikoTimeoutException):
    print('The following device time out: ' + ciscoDevice['host'])
except(SSHException):
    print('could not connect to device. check your settings on: ' + ciscoDevice['host'])
except(EOFError):
    print('Enf of file while attempting ' + ciscoDevice['host'])
except Exception as other_error:
    print('The error' + str(other_error)+ 'occured while connecting to: ' + ciscoDevice['host'])

configVlan = ['vlan 10' , 'name NetmikoVLAN']
output = connection.send_command('show ip int brief')
vlanBrief=connection.send_command('show vlan brief')
print('The script has completed')