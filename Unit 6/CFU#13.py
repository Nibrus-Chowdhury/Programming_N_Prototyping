'''
Nibrus Chowdhury
Period 5-6
11/26/2024
Description: A smily face with eyes, nose, and mouth drawn with points
'''

import simplegui

def draw_handler(canvas):
    # all drawing happens here
    # canvas.draw_point(x,y)
    canvas.draw_point([100,100], "black")
    canvas.draw_point([100,101], "black")
    canvas.draw_point([100,99], "black")
    canvas.draw_point([101,100], "black")
    canvas.draw_point([99,100], "black")
    canvas.draw_point([150,100], "black")
    canvas.draw_point([150,101], "black")
    canvas.draw_point([150,99], "black")
    canvas.draw_point([151,100], "black")
    canvas.draw_point([149,100], "black")
    canvas.draw_point([85,130], "black")
    canvas.draw_point([95,140], "black")
    canvas.draw_point([105,145], "black")
    canvas.draw_point([125,150], "black")
    canvas.draw_point([145,145], "black")
    canvas.draw_point([155,140], "black")
    canvas.draw_point([165,130], "black")
    canvas.draw_point([125,125], "black")
    canvas.draw_point([126,125], "black")
    canvas.draw_point([124,125], "black")

#library.create_frame(title, width, height)

frame = simplegui.create_frame("CFU 13 Happy Dots",200,200)
frame.set_canvas_background("rgb(0,255,255)")
frame.set_draw_handler(draw_handler)
frame.start()
