import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import sqlite3

import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
import pandas as pd
import numpy as np
import pickle
import sqlite3
import random

import smtplib 
from email.message import EmailMessage
from datetime import datetime

warnings.filterwarnings('ignore')



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/home')
def home():
	return render_template('home.html')


@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('signin.html')


@app.route('/home1')
def home1():
	return render_template('home1.html')


@app.route("/signup")
def signup():
    global otp, username, name, email, number, password
    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')
    otp = random.randint(1000,5000)
    print(otp)
    msg = EmailMessage()
    msg.set_content("Your OTP is : "+str(otp))
    msg['Subject'] = 'OTP'
    msg['From'] = "evotingotp4@gmail.com"
    msg['To'] = email
    
    
   # s = smtplib.SMTP('smtp.gmail.com', 587)
   # s.starttls()
    #s.login("evotingotp4@gmail.com", "xowpojqyiygprhgr")
    #s.send_message(msg)
    #s.quit()
    return render_template("val.html")

@app.route('/predict_lo', methods=['POST'])
def predict_lo():
    global otp, username, name, email, number, password
    if request.method == 'POST':
        message = request.form['message']
        print(message)
        if int(message) == otp:
            print("TRUE")
            con = sqlite3.connect(r'C:\Users\chikk\Downloads\DDOS project\Extension\signup.db')
            cur = con.cursor()
            cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
            con.commit()
            con.close()
            return render_template("signin.html")
    return render_template("signup.html")

@app.route("/signin")
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect(r'C:\Users\chikk\Downloads\DDOS project\Extension\signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("signin.html")    

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("home.html")
    else:
        return render_template("signin.html")

@app.route("/notebook1")
def notebook1():
    return render_template("NSLKDD.html")

@app.route("/notebook2")
def notebook2():
    return render_template("NBaIOT.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features= [float(x) for x in request.form.values()]
    print(int_features,len(int_features))
    final4=[np.array(int_features)]
    model = joblib.load(r'C:\Users\chikk\Downloads\DDOS project\Extension\model_vot.sav')
    predict = model.predict(final4)
    val = str(predict).replace('[', '').replace(']', '').replace("'", "")

    if val == '0' or val == 'Dos':
        output = 'There is an Attack Detected, Attack Type is DoS!'
    elif val == '1' or val == 'Probe':
        output = 'There is an Attack Detected, Attack Type is Probe!'
    elif val == '2' or val == 'R2L':
        output = 'There is an Attack Detected, Attack Type is R2L!'
    elif val == '3' or val == 'U2R':
        output = 'There is an Attack Detected, Attack Type is U2R!'
    elif val == '9':
        output = 'There is an Attack Detected, Attack Type is Neptune (DoS)!'
    elif val == '4' or val == 'normal' or val == '11':
        output = 'There is no Attack Detected, it is Normal!'
    else:
        output = 'There is an Attack Detected! (Attack Code: ' + val + ')'
    
    

    return render_template('prediction.html', output=output)


@app.route('/predict1',methods=['POST'])
def predict1():
    int_features= [float(x) for x in request.form.values()]
    print(int_features,len(int_features))
    final4=[np.array(int_features)]
    model = joblib.load(r'C:\Users\chikk\Downloads\DDOS project\Extension\model_nbaiot.sav')
    predict = model.predict(final4)

    if predict == 0:
        output='There is no Attack Detected, it is Benign!'
   
    elif predict == 1:
        output = 'There is an Attack Detected, Attack Type is Gafgyt Combo!'

    elif predict == 2:
         output = 'There is an Attack Detected, Attack Type is Gafgyt Junk!'

    elif predict == 3:
         output = 'There is an Attack Detected, Attack Type is Gafgyt Scan!'
    
    elif predict == 4:
         output = 'There is an Attack Detected, Attack Type is Gafgyt TCP!'

    elif predict == 5:
        output = 'There is an Attack Detected, Attack Type is Gafgyt UDP!'

    elif predict == 6:
         output = 'There is an Attack Detected, Attack Type is Mirai ACK!'

    elif predict == 7:
         output = 'There is an Attack Detected, Attack Type is Mirai Scan!'
    
    elif predict == 8:
         output = 'There is an Attack Detected, Attack Type is Mirai SYN!'
    
    elif predict == 9:
         output = 'There is an Attack Detected, Attack Type is Mirai UDP!'
    
    elif predict == 10:
         output = 'There is an Attack Detected, Attack Type is Mirai Udpplain!'
    
    

    return render_template('prediction1.html', output=output)



if __name__ == "__main__":
    app.run(debug=True)
