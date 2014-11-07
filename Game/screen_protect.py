#http://www.codeskulptor.org/#user38_F5qDivX4TGRlId3.py

import simplegui
import random

message = "Hello Python!"
position = [50,50]


def switch():
    global message
    message = "Welcome!"

def draw(canvas):
    canvas.draw_text(message, position, 40, "Red")

def input(text):
    global message
    message = text
    
def tick():
    x = random.randrange(0,400)
    y = random.randrange(0,500)
    position[0] = x
    position[1] = y


    

frame = simplegui.create_frame("Python",400,500)
button = frame.add_button("Switch",switch,100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(200,tick)
text = frame.add_input("Message:",input,50)


frame.start()
timer.start()
