import websocket
import time
wsList = []

def makeConnection():
    ws = websocket.WebSocket()
    ws.connect("ws://docker-nodejs-ws-dev2.ap-southeast-2.elasticbeanstalk.com/socket.io/?EIO=3&transport=websocket")
    ws.send("Hello, World")
    wsList.append(ws)

def refrsh():
    pass
    #for ws in wsList:
    #    ws.send("Hello, World")
    #print("refreshed")

if __name__ == "__main__":
    for i in range(300):
        makeConnection()

    while True:
        time.sleep(0.01)
        #refrsh()
        wsList[0].close()
        wsList.pop(0)
        makeConnection()


