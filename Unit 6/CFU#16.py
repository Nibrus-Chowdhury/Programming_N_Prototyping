'''
Nibrus Chowdhury
Period 5-6
11/27/2024
Description: A smily face with eyes, nose, and mouth drawn with circles
'''

import simplegui

def draw_handler(canvas):
    # all drawing happens here
    # canvas.draw_circle(centerXY, radius, line_width, color)
    canvas.draw_circle((65,75), 10, 5, "white")
    canvas.draw_circle((135,75), 10, 5, "white")
    canvas.draw_circle((100,100), 100, 2, "white")
    canvas.draw_circle((100,100), 5, 10, "red")
    canvas.draw_circle((100,150), 10, 20, "white")
    canvas.draw_circle((100,135), 10, 20, "black")
#library.create_frame(title, width, height)
frame = simplegui.create_frame("CFU 15 Happy Circles",200,200)
frame.set_canvas_background("rgb(0,0,0)")
frame.set_draw_handler(draw_handler)
frame.start()
