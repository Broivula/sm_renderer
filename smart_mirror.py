import time
import asyncio
import clock
from queue import Queue
from threading import Thread
from mirror_renderer import Renderer
from data_processing import D_Processing
from mirror_networking import Networking
import json

socket_port = 8928
rend = Renderer()

def networking_thread(p_que):
	# do networking stuff
	# some data arrives
	net = Networking(p_que)

def data_processing_thread(p_que, r_que):
	d_processor = D_Processing(r_que)
	while True:
		data = p_que.get()
		# process the incoming data
		# spit out the processed data to be rendered
		# -> processed data gets queued inside the class
		d_processor.process(data)

async def async_rendering(r_que):
    global rend
    rend.__start__()
    while True:
        data = r_que.get()
        rend.draw_label(data)


def main():
    rendering_que = Queue()
    processing_que = Queue()
    thread_1 = Thread(target = networking_thread, args=(processing_que, ))
    thread_2 = Thread(target = data_processing_thread, args=(processing_que,rendering_que))
    thread_1.setDaemon(True)
    thread_2.setDaemon(True)
    thread_1.start()
    thread_2.start()
    clock.start_clock(rendering_que)
    rendering_que.join()
    processing_que.join()
    asyncio.run(async_rendering(rendering_que))
    rend.__start__()

if __name__=="__main__":
    main()
