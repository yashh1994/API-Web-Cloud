from flask import Flask
import os
import threading

app = Flask(__name__)

counter = 0

def increment_counter():
    global counter
    counter += 1
    threading.Timer(30.0, increment_counter).start()

increment_counter()

@app.route('/')
def hello_world():
    return f"Current Counter is {counter}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
