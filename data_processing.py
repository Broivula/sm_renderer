import json
class D_Processing:

    def __init__(self):
        print("data processing initialized")

    def process(data):
        # frist we have to figure out where the data is from
        # I think we should use json as a format
        parsed_data = json.loads(data)
        print(parsed_data)
