##import library
import getpass
import base64, hashlib
from cryptography.fernet import Fernet
from colorama import init,Fore
from art import *
##colorama con
init(autoreset = True)
l_blue = Fore.BLUE
green = Fore.GREEN
red = Fore.RED
reset = Fore.RESET
##con
print(f"{l_blue}This Is A Simple G-Mail Sender So")
print(f"{red}Fill Your G-Mail Info Completely!!")
##generate key 
key = "Eagle"
key = hashlib.md5(key.encode()).hexdigest()
key = base64.urlsafe_b64encode(key.encode())
f = Fernet(key)
##get info
gmail = input("[Your G-Mail...] ")
gmail_pass = getpass.getpass("[PassWord...]")
##encrypt info
gmail = f.encrypt(gmail.encode())
gmail_pass = f.encrypt(gmail_pass.encode())
##write info
try:
    file = open("file",'wb')
    file.write(gmail)
    file.write("\n".encode())
    file.write(gmail_pass)
    file.close()
    print(f"{green}Successfuly!!")
    print(f"{l_blue}Open FSendFile This Is Your Id =>{reset} Eagle")
except Exception as e:
    print(f"{red}!!Error[Try Later]")