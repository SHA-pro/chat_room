import socket
from colorama import Fore
import pyfiglet
from datetime import *
import os
green = Fore.GREEN
blue = Fore.BLUE
print(blue)
os.system("pyfiglet ChatRoom")
print("This program was made by Swam Htet Aung")

now = datetime.now()
now_time = now.strftime("%H:%M:%S")
print(f"{green}Chat room created! at {now_time}")



s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1024))
s.listen(5)
while True:

    server, usr_adr = s.accept()
    s_user = input('Enter User Name: ')
    print(f"{green}ip {usr_adr} connected")


    while 1 > 0:
        message = input(f"{blue}{s_user} : ")
        message.encode("utf-8")
        s_user.encode("utf-8")
        space = ' : '
        m = s_user + space + message

        server.send(bytes(m, "utf-8"))
        msg = server.recv(1024)

        print(msg.decode("utf-8"))
