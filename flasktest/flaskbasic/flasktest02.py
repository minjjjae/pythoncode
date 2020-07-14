from flask import Flask, request,render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("login.html")

@app.route('/method/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return 'Post'
    else:
        return 'Get'

@app.route('/login')
def login1():
    # user=request.args.get('name')
    username=request.args.get('username')
    pw=request.args.get('password')
    # return 'User %s'%user
    return 'Username :%s, pw:%s'%(username,pw)
    
@app.route('/login',methods=['POST'])
def login2():
    username=request.form['username']
    pw=request.form['password']
    return 'Username :%s, pw:%s'%(username,pw)
if __name__ == '__main__':
    app.run(debug=True,port=8089)