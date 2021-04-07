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
    def create_clock(self):
        print("clock function")

        # the function to draw notes
        # first it should check how many notes are already drawn
        # if max amount -> delete the one at the bottom, draw a new one on top
        # if < max, then draw it on top, move others down
    def create_notes(self):
        print("notes function")

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
        new_label = tk.Label(self.master,
                             text=data,
                             foreground="white",
                             background="black")

        # we get the data here, and determine which function we draw. 
        # if the received data was news, we draw news etc.

        func = self.update_function.get(int(data))
        func()
        new_label.pack()
        self.master.update()



    #   Update a single text label
    def update_label(self,data):
        print("update label")

    #   A function to create the placeholders for the text locations
#    def create_placeholders(self):



