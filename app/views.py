from flask import Flask,g,request,render_template,redirect,escape,Markup
from re import template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/message')
def message():
	return render_template('message.html')
    
@app.route('/article')
def article():
    return render_template('article.html')

@app.route('/personnal')
def personnal():
    return render_template('personnal.html')


@app.route('/post',methods=['POST'])
def post():
    #Comment's target url
    #get the comment data
    name=request.form.get('name')
    words=request.form.get('comments')
    create_at=datetime.now()
    #save the data
    save_data(name,words,create_at)
    return redirect('/')

@app.template_filter('nl2br')
def nl2br_filters(s):
    #tranform the new line in comment to </br> tag
    return escape(s).replace('\n', Markup('</br>'))

@app.template_filter('datetime_fmt')
def datetime_fmt_filter(dt):
    #make the datetime to be shown friendly
    return dt.strftime('%Y-%m-%d %H:%M:%S')