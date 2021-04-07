import tkinter as tk
import sys
import os

class Renderer:

    text_elements = {}                          # holds our text labels
    master = None                               # placeholder for our window
    news_labels = []
    notes_labels = []

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

        # the function to draw notes
        # first it should check how many notes are already drawn
        # if max amount -> delete the one at the bottom, draw a new one on top
        # if < max, then draw it on top, move others down
    def create_notes(self):
        print("notes function")
        y_dat = round(len(self.notes_labels) * 0.1, 1)
        print("ydat : ", y_dat)
        data = {
            "pos": "ne",
            "relx": 1.0,
            "rely": y_dat
        }
        return data

        # the function to draw the weather
        # probably gets called once every hour? half hour? I don't know
        # draws a string indicating the amount of temperature
        # and a cute symbol next to it. :) :)
    def create_weather(self):
        print("weather function")

        # the function which draws the news strings
        # so basically as with every one of the other functions here, the
        # data (string) is already processed. The job of this function is only
        # to draw it on a certain location. (just reminding myself.)
        # Works in a similar fashion as the notes function
        # news get drawn every.. i don't know, 20 minutes?
    def create_news(self):
        print("news function")

        # the picture function is (hopefully) going to be fairly simple, or I don't know
        # some validation is needed, for sure. But idea is, that one could send a picture from their 
        # gallery, and it could get drawn. One picture at a time. 
        # maybe implement this last, since it's an extra anyway.
    def create_picture(self):
        print("picture function")

    def __start__(self):
        self.update_function = {
            0:self.create_clock,
            1:self.create_notes,
            2:self.create_weather,
            3:self.create_news,
            4:self.create_picture
        }
        self.master.update()

    def draw_label(self, data):
        # let's just start with the basics, first just render a text box here
        # or rather generate a new text box
        # this label thing is just a placeholder, ignore it later
        # we get the data here, and determine which function we draw. 
        # if the received data was news, we draw news etc.

        func = self.update_function.get(int(data))
        label_data = func()
        print("label positioning data: ", label_data)
        new_label = tk.Label(self.master,
                             text=data,
                             foreground="white",
                             background="black")
        new_label.place(relx=label_data.get("relx"),
                        rely=label_data.get("rely"),
                        anchor=label_data.get("pos"))
        self.notes_labels.append(new_label)
        #new_label.pack()
        print("# of notes: ", len(self.notes_labels))
        self.master.update()



    #   Update a single text label
    def update_label(self,data):
        print("update label")

    #   A function to create the placeholders for the text locations
#    def create_placeholders(self):



