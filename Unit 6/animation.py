'''
Nibrus Chowdhury
12/16/24
Period 5-6
Description: An animation of a snowman rolling a snowball down a hill and the snowball gets bigger as it goes down the hill until it covers the snowman at the bottom which sneaks back up on top of the large snowball at the end.
'''

import simplegui
import math

# Global Variables

width = 1000
height = 500
face1 = False
x = 425
y = 0
z = 10
xscale = 550
yscale = 150
y2 = 0
o = 0
f = 0
# Event Handlers

def draw(canvas):
    global x
    global y
    global z
    global xscale
    global y2
    global o
    global f
    # Snow Mound
    canvas.draw_polygon([(0,500),(200,350),(200,500)], 1, "white", "white")
    canvas.draw_polygon([(200,500),(200,350),(400,350),(400,500)], 1, "white", "white")
    canvas.draw_polygon([(400,350),(400,500),(800,500)], 1, "white", "white")
    # Snowman 1
    canvas.draw_polygon([(300,350),(375,350),(375,300),(300,300)], 1, "black", "white")
    canvas.draw_polygon([(310,300),(365,300),(365,260),(310,260)], 1, "black", "white")
    canvas.draw_line((310,280),(280,270),2, "black")
    canvas.draw_circle((280,270),1,5,"black","black")
    canvas.draw_line((365,280),(395,270),2, "black")
    canvas.draw_circle((395,270),1,5,"black","black")
    canvas.draw_polygon([(320,260),(355,260),(355,230),(320,230)], 1, "black", "white")
    canvas.draw_circle((330,240),1,5,"black","black")
    canvas.draw_circle((345,240),1,5,"black","black")
    canvas.draw_line((330,251),(345,251),2,"black")
    canvas.draw_polygon([(300,230),(375,230),(337.5,200)], 1, "black", "black")
    # Snowman 2
    canvas.draw_polygon([(300+xscale,350+yscale-y2),(375+xscale,350+yscale-y2),(375+xscale,300+yscale-y2),(300+xscale,300+yscale-y2)], 1, "black", "white")
    canvas.draw_polygon([(310+xscale,300+yscale-y2),(365+xscale,300+yscale-y2),(365+xscale,260+yscale-y2),(310+xscale,260+yscale-y2)], 1, "black", "white")
    canvas.draw_line((310+xscale,280+yscale-y2),(280+xscale,270+yscale-y2),2, "black")
    canvas.draw_circle((280+xscale,270+yscale-y2),1,5,"black","black")
    canvas.draw_line((365+xscale,280+yscale-y2),(395+xscale,270+yscale-y2),2, "black")
    canvas.draw_circle((395+xscale,270+yscale-y2),1,5,"black","black")
    canvas.draw_polygon([(320+xscale,260+yscale-y2),(355+xscale,260+yscale-y2),(355+xscale,230+yscale-y2),(320+xscale,230+yscale-y2)], 1, "black", "white")
    canvas.draw_circle((330+xscale,240+yscale-y2),1,5,"black","black")
    canvas.draw_circle((345+xscale,240+yscale-y2),1,5,"black","black")
    canvas.draw_line((330+xscale,251+yscale-y2),(345+xscale,251+yscale-y2),2,"black")
    canvas.draw_polygon([(300+xscale,230+yscale-y2),(375+xscale,230+yscale-y2),(337.5+xscale,200+yscale-y2)], 1, "black", "black")
    # Snowball
    canvas.draw_circle((x,y), z, 1, "black", "white")
    if x < 900:
        x+=1
        y = 273+0.175*x
        z += 0.2
    else:
        x = x
        y = y
        z = z
    if x >= 900 and y2 < 100:
        y2 += 1
    else:
        y2 = y2
    for i in range(1,10):
        o+=1
    for i in range(1,10):
        f+=1
frame = simplegui.create_frame("Animation", width, height) 
frame.set_canvas_background("cyan")
frame.set_draw_handler(draw)

# Frame Start
frame.start()
