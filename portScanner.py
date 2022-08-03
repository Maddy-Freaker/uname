import socket
import sys 
import subprocess
from datetime import datetime
import threading
#Blank your Screen
subprocess.call('cls', shell=True)

#Banner from termcolor import colored
from termcolor import colored
from pyfiglet import Figlet
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

def scan_port(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1.8)
    conn =s.connect_ex((target,port))
    if(not conn):
        print("Port {}    is    Open".format(port))
    s.close


for port in range(start_port,end_port+1):
    thread=threading.Thread(target=scan_port, args=(port,))
    thread.start()

end_time=datetime.now()
print("Time Spent :",end_time-start_time)

