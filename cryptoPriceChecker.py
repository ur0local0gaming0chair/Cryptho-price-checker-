import time
import requests 
from bs4 import BeautifulSoup
import smtplib
from tkinter import *
import tkinter.messagebox
from twilio.rest import Client
import winsound

URL = 'https://crypto.com/price/cardano' 

headers = {"User-Agent": 'your user agent'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

cryptoPrice = soup.find(class_='chakra-text css-urtgp9').get_text()
cryptoName = soup.find(class_='chakra-heading css-13uytcw').get_text()
cryptoPriceExact = cryptoPrice[1:5]

account_sid = "account sid for twilio"
auth_token = "token from twilio"
client = Client(account_sid, auth_token)

def send():
    client.messages.create(to="your phone number", from_="your twilio user phone number", body=cryptoName + " is now at " + cryptoPrice)

def warning_1():
    title = cryptoName + ' price warning'
    msg = cryptoName + ' is now at ' + cryptoPrice
    tkinter.messagebox.showinfo(title,  msg)

def warning_2():
    print('phone signal is being sent')
    send()

def warning_3():
    winsound.PlaySound("beep.wav", winsound.SND_FILENAME)

while True:
    if cryptoPriceExact >= '2.22':
        print("WARNING\n" + cryptoName + " is now at " + cryptoPrice)
        warning_2()
        warning_3()
        warning_1()




    






