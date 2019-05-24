from tkinter import *
import random
from glob_var import *


# Functions
def add_trailer():
    """adds trailer to existing truck(2 positions on x axis, 2 positions on y axis)"""
    global BLOCK
    posy = SEG_SIZE * random.randint(1, (HEIGHT - SEG_SIZE) / SEG_SIZE)
    posx = SEG_SIZE * random.randint(1, (WIDTH - SEG_SIZE) / SEG_SIZE)
    BLOCK = c.create_oval(posx, posy,
                          posx + SEG_SIZE, posy + SEG_SIZE,
                          fill="white")


def main():
    # Operates the main part
    global GAME_ACTIVE
    # GAME_ACTIVE variable describes whether player still did not lose
    if GAME_ACTIVE:
        s.move()
        head_coords = c.coords(s.segments[-1].instance)
        x1, y1, x2, y2 = head_coords
        # Checks collisions
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            GAME_ACTIVE = False
        # Adding trailers
        elif head_coords == c.coords(BLOCK):
            s.add_segment()
            c.delete(BLOCK)
            add_trailer()
        # If crashes into itself
        else:
            for index in range(len(s.segments) - 1):
                if head_coords == c.coords(s.segments[index].instance):
                    GAME_ACTIVE = False
        root.after(100, main)
    else:
        c.create_text(WIDTH / 2, HEIGHT / 2,
                      text="You crashed.",
                      font="Arial 20",
                      fill="Yellow")


class Segment(object):
    # Describes the class of a single trailer/truck segment
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x + SEG_SIZE, y + SEG_SIZE,
                                           fill="white")

class Truck(object):
    # Truck class
    def __init__(self, segments):
        """так же зависит от сегментов из Сегмента,
        здесь описываем направления движения"""
        self.segments = segments
        # Possible moves
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        # Initial movement direction
        self.vector = self.mapping["Right"]

    def move(self):
        # Truck moves
        for index in range(len(self.segments) - 1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
            c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,
                 x1 + self.vector[0] * SEG_SIZE, y1 + self.vector[1] * SEG_SIZE,
                 x2 + self.vector[0] * SEG_SIZE, y2 + self.vector[1] * SEG_SIZE)

    def add_segment(self):
        # Plus one trailer
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.segments.insert(0, Segment(x, y))

    def change_direction(self, event):
        # The truck changes direction
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]


root = Tk()
root.title("Lorry driver")

c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
img = PhotoImage(file='image.png')
c.create_image(0, 0, anchor=NW, image=img)
label = Label(image=img)
label.image = img
c.grid()
# Keys pressing
c.focus_set()
# Creating trailers
segments = [Segment(SEG_SIZE, SEG_SIZE),
            Segment(SEG_SIZE * 2, SEG_SIZE),
            Segment(SEG_SIZE * 3, SEG_SIZE)]
s = Truck(segments)
c.bind("<KeyPress>", s.change_direction)
# Reaction on keypress
add_trailer()
main()
root.mainloop()
