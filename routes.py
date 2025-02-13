from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello():
    return "olá esse é o sistema de login, vá para a '/login' para iniciar"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    pass # página de login

@app.route('/home', methods = ['GET'])
def home():
    pass # página para acessar após o login