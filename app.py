import os
from flask import Flask

app = Flask(__name__)

print("Hello World")

@app.route('/')
def index():
    return "<h1>eat shit ^_^ !!</h1>"

def foo():
    print("searching for fleja bot...")
    r =requests.get('https://rainbow-gusty-icicle.glitch.me/')
    #r =requests.get('https://www.google.com/')
    print(r.status_code)
    print("searching for punisher bot...")
    r =requests.get('https://brindle-rattle-manager.glitch.me/')
    print(r.status_code)
    threading.Timer(300, foo).start()

import requests, time, threading

print("yea dude, let's rock")
foo()

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
