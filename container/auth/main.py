import os
from flask import Flask
from flask import request, url_for, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        args_mail = request.args.get('email', type=str)
        args_pwd = request.args.get('password', type=str)
        user = auth.create_user(email=args_mail, password =args_pwd)
        return render_template('index.html', uid = user.uid,)
    return render_template('login.html')
    pass

@app.route('/my-route', methods=['GET'])
def my_route():
    args_id = request.args.get('id', type=int)
    args_from = request.args.get('from', type=int)
    args_until = request.args.get('until', type=int)
    args_load = request.args.get('load', type=int)
    url_for('static', filename='style.css')
    return 'ID: {}, From: {}, Until: {}, Load: {}.'.format(args_id, args_from, args_until, args_load)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
