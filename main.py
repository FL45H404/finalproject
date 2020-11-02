from flask import Flask,render_template,redirect, url_for,request,session,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

import youtube_dl

with open('config.json','r') as c:
    param=json.load(c)['params']

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = param['local_url']
db = SQLAlchemy(app)
class contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    mobile = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String(120),  nullable=False)
    date = db.Column(db.DateTime, nullable=True,default=datetime.utcnow)

    

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def not_found(error):
    return "404 error",404
@app.route('/contacts',methods=['GET','POST'])
def contacts():
    if (request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        mobile=request.form.get('mobile')
        message=request.form.get('message')
        entry=contact(name=name,email=email,mobile=mobile,message=message,date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        flash("details send succesfully!")
    return render_template('contact.html')

@app.route('/')
def download():
    return render_template('download.html')
@app.route('/link',methods=['GET','POST'])
def links():
    link=request.form.get('name')
    with youtube_dl.YoutubeDL() as ydl:

        url=ydl.extract_info(link,download=False)
        data=url
        flash("Video details..")
        return render_template('yt.html',data=data)

if __name__ == "__main__":
    app.config['SECRET_KEY'] = "e5ac358c-f0bf-11e5-9e39-d3b532c10a28"
    app.run(debug=True)
