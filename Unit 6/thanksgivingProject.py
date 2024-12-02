'''
Nibrus Chowdhury
Period 5-6
12/1/24
Description: A thanksgiving scene created with the basic shape functions learned in class.
'''
import simplegui

# Frame setup
frame = simplegui.create_frame("Thanksgiving Drawing", 600, 400)

# Draw handler function
def draw(canvas):
    # Example: Drawing a circle
    canvas.draw_polygon([(0, 200), (0,400), (600, 400), (600, 200)], 1, "black", "green")

# Assign draw handler to the frame
frame.set_draw_handler(draw)

# Start the frame
frame.start()
