from tkinter import *
import random
from glob_var import *

# functions
def add_trailer():
    """adds trailer to existing truck(2 positions on x axis, 2 positions on y axis)"""
    #PASS


def main():
    """main part"""
    #PASS

class Segment(object):
    """ Single trailer/truck segment """
    #PASS

class Truck(object):
    """ Truck class """
    def __init__(self):
        """так же зависит от сегментов из Сегмента, здесь описываем направления движения"""
        #PASS
    def move(self):
        """ Truck moves"""
        #PASS
    def add_segment(self):
        """ Plus trailer """
        #PASS
    def change_direction(self, event):
        """ truck changes direction """


root = Tk()
root.title("Lorry driver")

c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
c.grid()

# Keys pressing
c.focus_set()

# creating segments and snake
segments = [] """list of trailers attached initially"""
truck1 = Truck(segments)

# Reaction on keypress
c.bind("<KeyPress>", s.change_direction)

add_trailernull()
main()
root.mainloop()
