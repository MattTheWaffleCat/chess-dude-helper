from os import environ
from flask import Flask

PORT = process.env.PORT || 3000

app = Flask(__name__)
app.run(environ.get(PORT))

def foo():
    print("searching...")
    #r =requests.get('https://chess-dude-v1.glitch.me/')
    r =requests.get('https://www.google.com/')
    print(r.status_code)
    threading.Timer(300, foo).start()

print("yea dude, let's rock")
foo()
