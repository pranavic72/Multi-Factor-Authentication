from flask import Flask,render_template,request 


app = Flask(__name__)

@app.route('/') 
def home():
    return render_template('login.html')

@app.route('/getotp',methods=['POST','GET'])
def getotp():
    if request.method == 'POST':
        phone = request.form['phone']
        # getotpapi(phone)
        return phone


if __name__ == '__main__':
    app.run(debug=True)

