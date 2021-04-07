import json
from queue import Queue
from mirror_networking import Networking

class D_Processing(object):

    def __init__(self, r_que ):
        print("data processing initialized")
        self.r_que = r_que

    def process(self, data):
        # frist we have to figure out where the data is from
        # I think we should use json as a format
        #parsed_data = json.loads(data)
        #print(parsed_data)
        print("ladilaa processing some data..")
        decoded_data = data.decode('utf-8')
        self.r_que.put(decoded_data)
