from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "Backend from Multi-Service Example"
