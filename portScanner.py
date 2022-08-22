import socket
import sys 
import subprocess
from datetime import datetime
import threading


#Banner from termcolor import colored
from termcolor import colored
from pyfiglet import Figlet


#Blank your Screen
subprocess.call('cls', shell=True)

#   Code for the Uname Banner

f = Figlet(font='standard')
print(colored(f.renderText("Uname"),"green"))


print("-"*80)
print("Port Scanning using Theading method")
print("-"*80)
start_time=datetime.now()
remoteServer = input("Enter IP or address for Scanning: ")
try:
    target=socket.gethostbyname(remoteServer)
except socket.gaierror:
    print("Unable to reslove the given address {}".format(remoteServer))
    sys.exit()
except KeyboardInterrupt:
    print("You Pressed Ctrl + C")
    sys.exit()
except socket.error:
    print("Couldn't connect to the Server {}".format(remoteServer))

start_port=int(input("Enter the Starting port Number :"))
end_port=int(input("Enter the end port Number:"))

print("Scanning Target\t{}".format(target))

# This Scanning Function  for the ports
openPortList=[]
def scan_port(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1.8)
    conn =s.connect_ex((target,port))
    if(not conn):
        print("Port {}    is    Open".format(port))
        openPortList.append(port)
        #print(openPortList)
    s.close
    


#This is function which type of the port 

def Checking_port(openPortList):
    portList = {20:'FTP Data Port',21: 'FTP Control port', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 43: 'WHOIS', 53: 'DNS', 67: 'DHCP', 69: 'TFTP', 80: 'HTTP', 110: 'POP3', 115: 'SFTP',123:'NTP port', 
                143: 'IMAP', 161: 'SNMP',179:'BGP', 443: 'HTTPS',500:'ISAKMP',515: 'LPD', 873: 'rsync', 993: 'IMAP SSL', 955: 'POP3 SSL', 1080: 'SOCKS',1433:'Microsoft SQL server port',2082:'Cpanel default port',2083:'	Cpanel over SSL', 3128: 'Proxy', 
                2086:'Cpanel Webhost Manager (default)',2087:'Cpanel Webhost Manager (with https)',2095:'Cpanel WebMail',2096:'Cpanel secure webmail over SSL',2222:'DirectAdmin Server Control Panel',3306: 'MySQL', 3389: 'RDP', 5432: 'PostgreSQL', 5900: 'VNC', 
                5938: 'TeamViewer',8080:'HTTP port (alternative one for port 80)',8443:'Plesk Server Control Panel over SSL'}
    return(portList.get(openPortList,'Unknown'))
    
def port_details(openPortList):
    for port in openPortList:
        print("{} is ".format(port)+Checking_port(port)+" port")


for port in range(start_port,end_port+1):
    thread=threading.Thread(target=scan_port, args=(port,))
    thread.start()

end_time=datetime.now()
print("Time Spent :",end_time-start_time)

print("-"*80)
print("Details About the ports")
print("-"*80)

port_details(openPortList)

