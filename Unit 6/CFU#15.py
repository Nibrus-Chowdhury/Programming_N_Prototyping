'''
Nibrus Chowdhury
Period 5-6
11/26/2024
Description: A smily face with eyes, nose, and mouth drawn with shapes
'''

import simplegui

def draw_handler(canvas):
    # all drawing happens here
    # canvas.draw_point(x,y)
    canvas.draw_point([100,100], "black")
    # canvas.draw_line([x1,y2],[x2,y2], line_width, line_color)
    canvas.draw_line([40,50],[50,50], 20, "black")
    #canvas.draw_polygon([(x1,y1),(x2,y2),(x3,y3)], line_width, color)
    canvas.draw_polygon([(50,50),(50,150),(150,150),(150,50)], 5, "yellow")
    canvas.draw_polygon([(85,75),()], 5, "yellow")
    
#library.create_frame(title, width, height)
frame = simplegui.create_frame("CFU 15 Happy Shapes",200,200)
frame.set_canvas_background("rgb(0,0,0)")
frame.set_draw_handler(draw_handler)
frame.start()
