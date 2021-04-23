import time
import json
from types import SimpleNamespace
from threading import Thread
from datetime import datetime
from queue import Queue

def start_clock(r_que):
    clock_thread = Thread(target = run_clock, args=(r_que,))
    clock_thread.setDaemon(True)
    clock_thread.start()
    print("clock started.")

def get_date_time_str(d_t):
    dt = datetime.now()
    if d_t == 1:
        return dt.strftime("%d/%m/%Y")
    else:
        return dt.strftime("%H:%M:%S")

def get_date_time_data():
    _data = json.dumps({"msg":(get_date_time_str(0),get_date_time_str(1)), "sub_id":0})
    return json.loads(_data, object_hook=lambda d:SimpleNamespace(**d))

def run_clock(r_que):
    while 1:
        time.sleep(1)
        r_que.put(get_date_time_data())


