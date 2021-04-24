import tkinter as tk
import sys
from datetime import datetime
import os
import json
import asyncio
import clock
from types import SimpleNamespace

class Renderer:

    text_elements = {}                          # holds our text labels
    master = None                               # placeholder for our window
    news_labels = []
    notes_labels = []
    weather_label = None
    digital_clock_label = None
    date_label = None
    date_base_y_pos = 0.05
    date_base_x_pos = 0.95
    notes_base_y_pos = 0.5
    notes_base_x_pos = 0.95
    clock_base_y_pos = 0.1
    clock_base_x_pos = 0.95
    weather_base_y_pos = 0.1
    weather_base_x_pos = 0.05
    news_base_y_pos = 0.95
    news_base_x_pos = 0.1
    last_updated_note = 0
    last_updated_news = 0


    update_function = {}

    # initialize the window
    def __init__(self):

       if os.environ.get('DISPLAY', '') == '':
           print('no display found. Using :0.0')
           os.environ.__setitem__('DISPLAY', ':0.0')

       self.master = tk.Tk()
       self.master.title("smart_mirror")
       self.master.geometry("400x800")               # just some initial values, will be fullscreen
       self.master.configure(bg="black")             # set the background black

       # the function to draw the clock
        # hopefully only gets called once, althought I'm already wondering about how should it be updated
        # how all of the following functions work, is that they return a dictionary (or json) of data, 
        # which then contains all the information how draw_label function should draw it.
        # So this is the flow: draw_label function gets called -> it checks which label it's updating
        # then it calls the updating function (the ones below), which do all the nitty gritty
        # the updating function returns a data structure, which then the draw_label function draws.


    def create_clock(self):
        print("clock function")
        self.create_empty_labels(0, 1, self.clock_base_x_pos, self.clock_base_y_pos, "ne")

        # the function to draw notes
        # first it should check how many notes are already drawn
        # if max amount -> delete the one at the bottom, draw a new one on top
        # if < max, then draw it on top, move others down
    def create_notes(self):
        print("notes function")
    #def create_empty_lables(sub_id, amount, x_pos, y_pos, anchor):
        self.create_empty_labels(1, 5, self.notes_base_x_pos, self.notes_base_y_pos, "e")


        # the function to draw the weather
        # probably gets called once every hour? half hour? I don't know
        # draws a string indicating the amount of temperature
        # and a cute symbol next to it. :) :)
    def create_weather(self):
        print("weather function")
        self.create_empty_labels(2, 1, self.weather_base_x_pos, self.weather_base_y_pos, "nw")


        # the function which draws the news strings
        # so basically as with every one of the other functions here, the
        # data (string) is already processed. The job of this function is only
        # to draw it on a certain location. (just reminding myself.)
        # Works in a similar fashion as the notes function
        # news get drawn every.. i don't know, 20 minutes?
    def create_news(self):
        print("news function")
        self.create_empty_labels(3, 5, self.news_base_x_pos, self.news_base_y_pos, "sw")

    def create_date(self):
        print("date function")
        self.create_empty_labels(4, 1, self.date_base_x_pos, self.date_base_y_pos, "ne")


        # the picture function is (hopefully) going to be fairly simple, or I don't know
        # some validation is needed, for sure. But idea is, that one could send a picture from their 
        # gallery, and it could get drawn. One picture at a time. 
        # maybe implement this last, since it's an extra anyway.
    def create_picture(self):
        print("picture function")

    def create_empty_labels(self, sub_id, amount, x_pos, y_pos, anchor):
        for x in range(amount):
            new_label = tk.Label(self.master,
                                 text="",
                                 foreground="white",
                                 background="black")
            if sub_id == 0:
                self.clock_label = new_label
            elif sub_id == 1:
                y_pos = round(len(self.notes_labels) * 0.02, 2) + self.notes_base_y_pos
                self.notes_labels.append(new_label)
            elif sub_id == 2:
                self.weather_label = new_label
            elif sub_id == 3:
                y_pos = self.news_base_y_pos - round(len(self.news_labels) * 0.02, 2)
                self.news_labels.append(new_label)
            elif sub_id == 4:
                self.date_label = new_label

            new_label.place(relx=x_pos,
                            rely=y_pos,
                            anchor=anchor)

    def check_if_label_empty(self, label):
        t_input = label["text"]
        if t_input == "":
            print("there is no text!")
            return True
        else:
            print("found some text.")
            return False

# so this current implementation is fucking shit and I just came back here to comment
# that this better be changed in the future.
# it's not pretty, it's clunky and there is no trace of fucking elegance to be found
# Most of this ugly shit I can blame on my hunger - I should've fucking eaten before
# continuing this with an empty stomach.

    def get_writeable_label(self, sub_id):

        if sub_id == 0:
            return (self.clock_label, self.date_label)
        elif sub_id == 1:
            if self.last_updated_note < 4:
                temp = self.last_updated_note
                self.last_updated_note += 1
                return self.notes_labels[temp]
            else:
                temp = self.last_updated_note
                self.last_updated_note = 0
                return self.notes_labels[temp]
        elif sub_id == 2:
            return self.weather_label
        elif sub_id == 3:
            if self.last_updated_news < 4:
                temp = self.last_updated_news
                self.last_updated_news += 1
                return self.news_labels[temp]
            else:
                temp = self.last_updated_news
                self.last_updated_news = 0
                return self.news_labels[temp]

    def update_label(self, data):
        label = self.get_writeable_label(data.sub_id)
        if type(label) == tuple:
            label[0].config(text=data.msg[0])
            label[1].config(text=data.msg[1])
        else:
            label.config(text=data.msg)


    def __start__(self):
        self.update_function = {
            0:self.create_clock,
            1:self.create_notes,
            2:self.create_weather,
            3:self.create_news,
            4:self.create_date,
            5:self.create_picture
        }
        for x in range(5):
            func = self.update_function.get(x)
            func()
        self.master.update()

    def draw_label(self, data):
        # let's just start with the basics, first just render a text box here
        # or rather generate a new text box
        # this label thing is just a placeholder, ignore it later
        # we get the data here, and determine which function we draw. 
        # if the received data was news, we draw news etc.

        if data.sub_id == 3:
            for news in data.parsed_news:
                self.update_label(json.loads(news, object_hook= lambda d: SimpleNamespace(**d)))
        else:self.update_label(data)

        self.master.update()


    #   A function to create the placeholders for the text locations
#    def create_placeholders(self):



