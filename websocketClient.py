import websocket
import time
wsList = []

def makeConnection():
    ws = websocket.WebSocket()
    ws.connect("ws://docker-nodejs-ws-dev.ap-southeast-2.elasticbeanstalk.com/")
    ws.send("Hello, World")
    wsList.append(ws)

def refrsh():
    for ws in wsList:
        ws.send("Hello, World")

for i in range(300):
    makeConnection()

while True:
    time.sleep(1)
    refrsh()
    wsList.pop(0)
    makeConnection()


