import getpass
import smtplib
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

class SendMail:
    def readfile(self):
        try:
            with open("file","rb") as f:
                l = f.read().decode().split("\n")
                self.gmail = l[0]
                self.gmail_pass = l[1]
            print(f"{green}SuccessFully Done!!!")
            return self.gmail , self.gmail_pass , self.generatekey()
        except Exception as e:
            print(f"{red}{e}")
            exit()
    def generatekey(self):
        try:
            self.key = getpass.getpass("[Enter Your ID To Encrypt Info...] ")
            self.key = hashlib.md5(self.key.encode()).hexdigest()
            self.key = base64.urlsafe_b64encode(self.key.encode())
            print(f"{green}Key SuccessFully Generated!!!")
            self.decrypt(self.key)
        except Exception as e:
            print(f"{red}{e}")
            exit()
    def decrypt(self,key):
        try:
            self.f = Fernet(self.key)
            self.gmail = self.f.decrypt(self.gmail.encode())
            self.gmail_pass = self.f.decrypt(self.gmail_pass.encode())
            print(f"{green}Welcome {reset}{self.gmail.decode()}")
            self.login(self.gmail,self.gmail_pass)
        except Exception as e:
            print(f"{red}Error!!![Maybe Wrong Key]")
            exit()
    def login(self,gmail,gmail_pass):
        try:
            Host = 'smtp.gmail.com'
            Port = 587
            print("Connecting To Host")
            self.server = smtplib.SMTP(Host, Port)
            self.server.ehlo()
            self.server.starttls()
            self.server.login(self.gmail.decode(), self.gmail_pass.decode())
            print(f"{green}LoggedIn SuccessFully")
            self.sendmail()
        except Exception as e:
            print(f"{red}{e}")
            exit()
    def sendmail(self):
        while 1:
            print(f"{l_blue}Sender{reset} {self.gmail.decode()}")
            msg = input("Type AnyThing To Send...")
            reciver = input("Reciver...")
            try:
                self.server.sendmail(self.gmail.decode(), reciver, msg)
                print(f"{green}Sent!!!")
            except:
                print("Error!!!!")
                exit()

sm = SendMail()
sm.readfile()