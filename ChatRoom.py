#!/usr/bin/python3


# import
import socket
from colorama import Fore
from datetime import *
import os
import sys
import time

# color

green = Fore.GREEN
blue = Fore.BLUE
# clear
if sys.platform in ["linux", "linux2"]:
    os.system('clear')
else:
    os.system('')
# intro all
intro_all = """

 
 .---. .-. .-.  .--.  .---. .----.  .----.  .----. .-.   .-.
/  ___}| {_} | / {} \{_   _}| {}  }/  {}  \/  {}  \|  `.'  |
\     }| { } |/  /\  \ | |  | .-. \\       /\      /| |\ /| |
 `---' `-' `-'`-'  `-' `-'  `-' `-' `----'  `----' `-' ` `-'



"""

print(green)
print(intro_all)

def create():
    # create

    # intro
    print(blue)
    print(intro_all)
    print(f"{green}This program was made by Swam Htet Aung")

    now = datetime.now()
    now_time = now.strftime("%H:%M:%S")
    # /intro
    print(blue)
    # host & port
    host = input("Enter Host: ")
    port = int(input("Enter Port: "))
    print(f"{green}Chat room created! at {now_time}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect
    s.bind((host, port))
    s.listen(5)
    while True:
        # connection accept
        server, usr_adr = s.accept()
        s_user = input('Enter User Name: ')
        print(f"{green}ip {usr_adr} connected")

        while 1 > 0:
            # decode and send
            message = input(f"{blue}{s_user} : ")
            message.encode("utf-8")
            s_user.encode("utf-8")
            space = ' : '
            m = s_user + space + message

            server.send(bytes(m, "utf-8"))
            msg = server.recv(1024)

            print(msg.decode("utf-8"))


def join():
    # join

    # intro
    print(blue)
    print(intro_all)
    print("This program was made by Swam Htet Aung")
    now = datetime.now()
    now_time = now.strftime("%H:%M:%S")
    print(green)
    print(now_time)
    # /intro

    # host & port
    host = input("Enter Host: ")
    port = int(input("Enter Port: "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect
    s.connect((host, port))

    # online host
    print(f"server {socket.gethostname()} is online")

    # user name
    c_user = input("Enter User Name: ")
    while True:
        print(f"{green}connected to server {socket.gethostname()}")

        while 1 > 0:
            # decode & send
            msg = s.recv(1024)
            print(msg.decode("utf-8"))
            message = input(f"{blue}{c_user} : ")
            message.encode("utf-8")
            c_user.encode("utf-8")
            space = ' : '
            m = c_user + space + message
            s.send(bytes(m, "utf-8"))


user = ''
while user != "quit":
    user = input(">")
    if user == "help":
        print(f"""{blue}
create : create chat room
join   : join chat room
help   : show help message
quit   : exit the program
{green}                """)
    if user == "create":
        create()
    if user == "join":
        join()
else:
    print(f"{green}Bye... :)")
    time.sleep(3)
