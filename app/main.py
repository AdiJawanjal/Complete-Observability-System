from flask import Flask
from prometheus_client import generate_latest, Counter

app = Flask(__name__)

# Sample metric
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    return 'Hello, World!'

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

