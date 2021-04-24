import socket
import time
import asyncio
import requests
from threading import Thread
from queue import Queue
host = '127.0.0.1'
port = 8929
test_data = "I'm here, bitch!!"
from fmiopendata.wfs import download_stored_query
w_query = "fmi::observations::weather::multipointcoverage"


class Networking(object):
    location = "Mäntsälä"
    cycle_time = 300
    news_src = 0
    news_urls = {0:"https://www.yle.fi/uutiset"}

    def __init__(self, p_que):
        self.initialize_socket()
        self.p_que = p_que
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        future = asyncio.ensure_future(self.data_fetcher())
        loop.run_until_complete(future)

    def socket_listener_thread(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
                print("socket connection successfull")
                s.send(test_data.encode())
                while True:
                    data = s.recv(1024)
                    if len(data) > 0:
                        print("data entering pipeline:")
                        print(data)
                        # so we received some data via the sockets
                        # it's either a note, or a picture
                        # either way, let's send the data to be processed
                        _data = {"content":data, "pipe":1}
                        self.send_data_to_be_processed(_data)
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

    def fetch_new_picture(self):
        print("new picture fetched.")

    def send_data_to_be_processed(self, data):
        print("sending data to be processed...")
        self.p_que.put(data)

    async def data_fetcher(self):
        while 1:
            asyncio.ensure_future(self.fetch_weather())
            asyncio.ensure_future(self.fetch_news())
            await asyncio.sleep(self.cycle_time)
        #asyncio.run(self.fetch_weather())
        #await asyncio.sleep(60)
        #asyncio.run(self.data_fetcher())


    async def fetch_weather(self):
        d = download_stored_query(w_query, ["place="+self.location])
        print("weather fetched")
        _data = {"content":d, "pipe":2}
        self.send_data_to_be_processed(_data)

    async def fetch_news(self):
        await asyncio.sleep(4)
        response = requests.get(self.news_urls[self.news_src])
        _data = {"content":response.content.decode('utf-8'), "pipe":3, "src":self.news_src}
        self.send_data_to_be_processed(_data)
        print("news fetched")

