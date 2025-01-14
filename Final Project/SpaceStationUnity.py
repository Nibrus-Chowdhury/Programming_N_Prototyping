# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, Safari, and Edge.

import simplegui

cmdCenter = False
outside = False
shipCore = False

def all_false():
    global cmdCenter
    global outside
    global shipCore
    cmdCenter = False
    outside = False
    shipCore = False

def screenCmdCenter():
    global cmdCenter
    all_false()
    cmdCenter = not cmdCenter
def screenOutside():
    global outside
    all_false()
    outside = not outside
def screenShipCore():
    global shipCore
    all_false()
    shipCore = not shipCore

# Handler for mouse click
def start():
    pass

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text("You are aboard a broken spaceship.", [15,15], 20, "Red")
    canvas.draw_circle([450,300], 30, 1, "white", "white")
    

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 900, 600)
frame.add_button("Start Game", start)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
