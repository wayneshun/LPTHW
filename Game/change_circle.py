#http://www.codeskulptor.org/#user38_m6p6F6M21S2HjYm.py

import simplegui
import random

ridius = 10
size =10


def increse():
    global size
    size += 1
    label1.set_text("Value: " + str(size))

def decrese():
    global size
    size -= 1
    label1.set_text("Value: " + str(size))

def change():
    global ridius
    ridius = size
    label2.set_text("Radius:" + str(ridius))
    

def draw(canvas):
    canvas.draw_circle((200, 200), ridius, 5, 'Red')



frame = simplegui.create_frame("Circle",400,500)
label1 = frame.add_label("Value: " + str(size))
button1 = frame.add_button("increse",increse,100)
button2 = frame.add_button("decrese",decrese,100)
label2 = frame.add_label("Radius:" + str(ridius))
button3 = frame.add_button("change",change,100)
frame.set_draw_handler(draw)

frame.start()
