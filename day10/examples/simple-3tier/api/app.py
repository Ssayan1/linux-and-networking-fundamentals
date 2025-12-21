from flask import Flask
import redis
import socket
import os

app = Flask(__name__)

# Connect to Redis service named "redis" in the same compose/stack network
redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def root():
    return "Backend API v2 is running"

@app.route("/api")
def api():
    hostname = socket.gethostname()
    try:
        count = r.incr("counter")
    except Exception as e:
        return f"Backend {hostname} (redis error: {e})", 500
    return f"Hello from backend {hostname}. API hits: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
