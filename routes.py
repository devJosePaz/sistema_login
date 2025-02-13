from flask import Flask, request, render_template
import db

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello():
    return "olá esse é o sistema de login, vá para a '/login' para iniciar"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('template.html')
    
    
@app.route('/home', methods = ['GET'])
def home():
    pass # página para acessar após o login