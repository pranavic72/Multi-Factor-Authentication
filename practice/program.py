#1. first we will create a 6 digit random number
#2. store this number to a variable 
#3. then we need to write a program to send email 
#4. when sending the email we need to use the otp as a message 
#5. finally we need to request 2 user input, first for the user email and then for the otp that the user has recieved 

import os 
import math 
import random 
import smtplib 

digits = "0123456789"
OTP = ""

for i in range(6):
    OTP+= digits[math.floor(random.random()*10)]
    otp = OTP + " is your OTP"
    msg = otp

s = smtplib.SMTP('smtp.gmail.com',587)

s.starttls()

s.login("pranavi.c@somaiya.edu","qoeopwzaddqavudn")

email=input("please enter your email:")

s.sendmail('hello my name is navi',email,msg)

a = input("please enter your otp:>>")

if a == OTP:
    print("you are verified")
else:
    print("please check your otp again")
