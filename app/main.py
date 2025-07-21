from flask import Flask
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello():
    app.logger.info("Hello endpoint was hit")
    return "Hello, Loki Logs!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
