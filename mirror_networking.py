import socket
import time
import asyncio
from threading import Thread
host = '127.0.0.1'
port = 8929
test_data = "I'm here, bitch!!"

class Networking():

    def __init__(self):
        self.initialize_socket()
        asyncio.run(self.fetch_weather())

    def socket_listener_thread(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
                print("socket connection successfull")
                s.send(test_data.encode())
                while True:
                    data = s.recv(1024)
                    if len(data) > 0:
                        print(data)
                    else:
                        self.test_socket_connection(s)
                    if not data: break
        except Exception as err:
            print("error on socket creation thread")
            print ("most likely server having issues")
            print ("re-trying in 10 seconds")
            print(err)
            time.sleep(10)
            self.socket_listener_thread()

    def test_socket_connection(self, socket):
        try:
            socket.send("are you still there?")
        except:
            print("error, socket connection interrupted.")
            self.socket_listener_thread()

    def initialize_socket(self):
        try:
            s_thread = Thread(target = self.socket_listener_thread, args=())
            s_thread.start()
        except:
            print("error on socket creation")

    async def data_fetcher(self):
        asyncio.run(self.fetch_weather())
        asyncio.run(self.fetch_news())

    async def fetch_weather(self):
        await asyncio.sleep(2)
        print("weather fetched")

    async def fetch_news(self):
        await asyncio.sleep(4)
        print("news fetched")
