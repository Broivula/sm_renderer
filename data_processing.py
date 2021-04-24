import json
import datetime
import YLE_parser
from types import SimpleNamespace
from queue import Queue
from mirror_networking import Networking

class D_Processing(object):

    def __init__(self, r_que ):
        print("data processing initialized")
        self.r_que = r_que

    def jsonfy_data(self, data):
        print("bla")

        # basically we just want to get the latest data.
    def parse_weather_data(self, data):
        dt = list(data.data.keys())[-1]
        d = data.data.get(list(data.data.keys())[-1])["Mäntsälä Hirvihaara"]
        parsed_weather = str(d["Air temperature"]["value"]) + " C"
        print(parsed_weather)
        return json.dumps({"msg":parsed_weather, "date":dt.strftime("%d/%m/%Y,%H:%M:%S"),"sub_id":2}, indent = 2)


    # take the contents of an html page, 
    def parse_news_data(self, data):
        if data.get("src") == 0:
            parsed_news = YLE_parser.parse_webpage(data["content"])
            return json.dumps({"parsed_news":parsed_news, "sub_id":3})


    def process(self, data):
        # frist we have to figure out where the data is from
        # I think we should use json as a format
        case = data["pipe"]
        if case == 1:
            parsed_data = json.loads(data["content"].decode('utf-8'), object_hook=lambda d: SimpleNamespace(**d))
        elif case == 2:
            parsed_data = json.loads(self.parse_weather_data(data["content"]), object_hook=lambda d:SimpleNamespace(**d))
        elif case == 3:
            parsed_data = json.loads(self.parse_news_data(data), object_hook=lambda d:SimpleNamespace(**d))
        self.r_que.put(parsed_data)

