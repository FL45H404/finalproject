from flask import Flask,render_template,redirect, url_for,request,session,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

import youtube_dl

with open('config.json','r') as c:
    param=json.load(c)['params']

app = Flask(__name__) 

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def not_found(error):
    return "404 error",404

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
    
    app.secret_key = 'dh8nbsv/sjewo#sjk12fg'
    app.run(debug=True)
