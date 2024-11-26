'''
Nibrus Chowdhury
Period 5-6
11/26/2024
Description: A smily face with eyes, nose, and mouth drawn with lines
'''

import simplegui

def draw_handler(canvas):
    # all drawing happens here
    # canvas.draw_point(x,y)
    canvas.draw_point([100,100], "black")
    # canvas.draw_line([x1,y2],[x2,y2], line_width, line_color)
    canvas.draw_line([40,50],[50,50], 20, "yellow")
    canvas.draw_line([90,50],[100,50], 20, "yellow")
    canvas.draw_line([70,75],[70,80], 2, "yellow")
    canvas.draw_line([30,80],[75,100], 10, "yellow")
    canvas.draw_line([65,100],[115,80], 10, "yellow")
    canvas.draw_line([20,20],[20,125], 5, "yellow")
    canvas.draw_line([20,125],[130,125], 5, "yellow")
    canvas.draw_line([130,125],[130,20], 5, "yellow")
    canvas.draw_line([130,20],[20,20], 5, "yellow")
    #library.create_frame(title, width, height)

frame = simplegui.create_frame("CFU 14 Happy Lines",200,200)
frame.set_canvas_background("rgb(0,0,0)")
frame.set_draw_handler(draw_handler)
frame.start()
