from flask import Flask,render_template,request,url_for,redirect
import os
import math
import random
import smtplib
import hashlib
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cyber"    
    )

@app.route('/')
def index():
    return render_template('login.html')
    
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        login = request.form
        username=login['username']
        password=login['password']
        cursor = mydb.cursor()
        salt = 'c#2}'
        saltedpass = password+salt
        encodepass = hashlib.md5(saltedpass.encode()).hexdigest()

        cursor.execute("select email from registration where username=%s and password=%s",(username,encodepass))
        account = cursor.fetchone()

        sendotp(account[0])
    return redirect(url_for('verify'))



@app.route('/verify',methods=['POST','GET'])
def verify():
    msg=""
    if request.method == 'POST':
        otp = request.form['otp']
        
        f = open("otp.txt","r")
        ootp = f.read()
        f.close()
        if otp == ootp:
            msg="Successfully logged in!"
        else:
            msg="Failed to log in! Try again."
    return render_template('verify.html',msg=msg)
def sendotp(email):
    digits = "0123456789"
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
        otp = OTP + " is your OTP"
        msg = otp
    file1 = open('otp.txt',"w")
    file1.write(OTP)
    file1.close()
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("pranavi.c@somaiya.edu","kzvkafllanjjqogu")
    s.sendmail('pranavi.c@somaiya.edu',email,msg)
    return OTP


if __name__=="__main__": #to check we only run the page
    app.run(debug=True)
