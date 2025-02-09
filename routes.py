from main import app

@app.route('/')
def home():
    return "Construindo algo teste!"