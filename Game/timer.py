#http://www.codeskulptor.org/#user38_HHRkeuzuArhPEY8.py


import simplegui

number = 1
position = [100, 100]

def time():
    global number
    number += 1


def draw(canvas):
    global number
    canvas.draw_text(str(number), position, 50, "White")



frame = simplegui.create_frame("Timer", 200, 200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(1000, time)



frame.start()
timer.start()
