def foo():
    print("searching...")
    #r =requests.get('https://chess-dude-v1.glitch.me/')
   r =requests.get('https://www.google.com/')
    print(r.status_code)
    threading.Timer(300, foo).start()

foo()
