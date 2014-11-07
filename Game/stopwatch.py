#http://www.codeskulptor.org/#user38_TPzAc5HlW4oSOrs.py

# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 100
count = 0
total_times = 0
win_times = 0
stop = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    D = t % 10
    C = (t / 10) % 10
    B = (t / 100) % 6
    A = t / 600
    return str(A) + ":" +str(B) + str(C) + "." + str(D) 
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global count, stop
    stop = False
    timer.start()
    
def stop():
    global total_stops, succes_stops, stop
    if stop == False :
        if count % 10 == 0 and count != 0 :
            succes_stops += 1
            total_stops += 1
        elif count != 0 :
            total_stops += 1
    stopped = True
    timer.stop()
    
def reset():
    global count, succes_stops, total_stops
    count = 0
    stop = True
    total_stops = 0
    succes_stops = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count += 1


# define draw handler
def draw(canvas):
    text = format(count)
    canvas.draw_text(text, (40, 125), 42, "white")
    canvas.draw_text(str(win_times) + '/' + str(total_times), (30,30), 24, "White")
    

# create frame
frame = simplegui.create_frame('Stopwatch', 200, 200)
button1 = frame.add_button('Start', start,100)
button2 = frame.add_button('Stop', stop,100)
button2 = frame.add_button('Reset', reset,100)
timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw)
# register event handlers


# start frame
frame.start()
timer.start()
# Please remember to review the grading rubric
