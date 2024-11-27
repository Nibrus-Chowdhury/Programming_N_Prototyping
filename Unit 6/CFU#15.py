'''
Nibrus Chowdhury
Period 5-6
11/26/2024
Description: A smily face with eyes, nose, and mouth drawn with shapes
'''

import simplegui

def draw_handler(canvas):
    # all drawing happens here
    #canvas.draw_polygon([(x1,y1),(x2,y2),(x3,y3)], line_width, color)
    canvas.draw_polygon([(50,50),(50,150),(150,150),(150,50)], 5, "yellow")
    canvas.draw_polygon([(80,75),(80,77),(82,77),(82,75)], 5, "yellow")
    canvas.draw_polygon([(120,75),(120,77),(122,77),(122,75)], 5, "yellow")
    canvas.draw_polygon([(101,90),(101,105)], 1, "yellow")
    canvas.draw_polygon([(70,125),(80,135),(127,135),(137,125)], 1, "yellow")
    
    
#library.create_frame(title, width, height)
frame = simplegui.create_frame("CFU 15 Happy Shapes",200,200)
frame.set_canvas_background("rgb(0,0,0)")
frame.set_draw_handler(draw_handler)
frame.start()
