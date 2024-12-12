import simplegui
import math

# Global Variables

width = 1000
height = 500
face1 = False
x = 425
y = 350
# Event Handlers

def all_false():
    global face1
    face1 = False
    
def run():
    all_false()
    global face1
    face1 = not face1
    
def toggle_topRight():
    all_false()
    global face2
    face2 = not face2
      
def toggle_bottomLeft():
    all_false()
    global face3
    face3 = not face3
    
def toggle_bottomRight():
    all_false()
    global face4
    face4 = not face4

def draw(canvas):
    if face1:
        global x
        global y
        canvas.draw_polygon([(0,500),(200,350),(200,500)], 1, "white", "white")
        canvas.draw_polygon([(200,500),(200,350),(400,350),(400,500)], 1, "white", "white")
        canvas.draw_polygon([(400,350),(400,500),(800,500)], 1, "white", "white")
        canvas.draw_polygon([(300,350),(375,350),(375,300),(300,300)], 1, "black", "white")
        canvas.draw_polygon([(310,300),(365,300),(365,260),(310,260)], 1, "black", "white")
        canvas.draw_polygon([(320,260),(355,260),(355,230),(320,230)], 1, "black", "white")
        canvas.draw_circle((x,y), 10, 1, "black", "white")
        x = x + 0.1
        y = -0.375*x
        
frame = simplegui.create_frame("Animation", width, height) 
frame.set_canvas_background("cyan")
frame.set_draw_handler(draw)
frame.add_button("Run", run, 200, )

# Frame Start
frame.start()
