from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "Backend API is working!"

@app.get("/hello")
def hello():
    return "Hello from API!"
