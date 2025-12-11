import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)
r.ping()
@app.get("/")
def index():
    r.incr("counter")
    return f"Visitors: {r.get('counter').decode()}"

app.run(host="0.0.0.0", port=5000)
