import os, requests, time, threading
from flask import Flask

app = Flask(__name__)

@app.route('/')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

def foo():
    print("searching...")
    #r =requests.get('https://chess-dude-v1.glitch.me/')
    r =requests.get('https://www.google.com/')
    print(r.status_code)
    threading.Timer(300, foo).start()

print("yea dude, let's rock")
foo()
