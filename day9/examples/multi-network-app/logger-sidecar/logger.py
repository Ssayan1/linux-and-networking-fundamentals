from flask import Flask
import os

app = Flask(__name__)

SERVICE_NAME = os.getenv("SERVICE_NAME", "logger")

@app.route("/log")
def log():
    print(f"[LOGGER] Received log request from API service")
    return {"logged": True, "service": SERVICE_NAME}, 200

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
