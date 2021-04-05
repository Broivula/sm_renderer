import tkinter as tk
import sys
import os

class Renderer:

    text_elements = {}                          # holds our text labels
    master = None                               # placeholder for our window

    # initialize the window
    def __init__(self):

       if os.environ.get('DISPLAY', '') == '':
           print('no display found. Using :0.0')
           os.environ.__setitem__('DISPLAY', ':0.0')

       self.master = tk.Tk()
       self.master.title("smart_mirror")
       self.master.geometry("400x800")               # just some initial values, will be fullscreen
       self.master.configure(bg="black")             # set the background black

    def __start__(self):
        self.master.mainloop()

    def draw_label(self, data):
        # let's just start with the basics, first just render a text box here
        # or rather generate a new text box
        new_label = tk.Label(self.master,
                             text=data,
                             foreground="white",
                             background="black")
        new_label.pack()
        self.master.update()

    def update_label(data):
        print("update label")


