from flask import Flask, request
import requests, os

app = Flask(__name__)

LOGGER_HOST = os.getenv("LOGGER_HOST", "logger")

@app.route("/")
def home():
    return {"message": "Hello from API Service"}

@app.route("/call-logger")
def call_logger():
    url = f"http://{LOGGER_HOST}:5002/log"
    try:
        requests.get(url)
        return {"status": "logged"}, 200
    except Exception as e:
        return {"error": str(e)}, 500

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
