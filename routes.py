from flask import Flask, request, render_template, redirect, url_for
import db

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello():
    return "olá esse é o sistema de login, vá para a '/login' para iniciar"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('template.html')
    
    if request.method =='POST':
        username = request.form.get("username")
        password = request.form.get("password")

        db.adicionar_usuario(username, password) 

        return redirect(url_for ('home'))
    
    
@app.route('/home', methods = ['GET'])
def home():
    return "Homepage acessada!"