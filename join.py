import socket
import os
import pyfiglet
from colorama import Fore
from datetime import *

green = Fore.GREEN
blue = Fore.BLUE
print(blue)

os.system("pyfiglet ChatRoom")
print("This program was made by Swam Htet Aung")
now = datetime.now()
now_time = now.strftime("%H:%M:%S")
print(green)
print(now_time)

host = input("Enter Host: ")
port = int(input("Enter Port: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print(f"server {socket.gethostname()} is online")

c_user = input("Enter User Name: ")
while True:
    print(f"{green}connected to server {socket.gethostname()}")
    
    


    while 1 > 0:
        msg = s.recv(1024)
        print(msg.decode("utf-8"))
        message = input(f"{blue}{c_user} : ")
        message.encode("utf-8")
        c_user.encode("utf-8")
        space = ' : '
        m = c_user + space + message
        s.send(bytes(m, "utf-8"))
