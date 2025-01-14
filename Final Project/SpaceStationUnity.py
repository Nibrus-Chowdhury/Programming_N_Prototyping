# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, Safari, and Edge.

import simplegui

x = 250
y = 250
startScreen = True
left = False
middle = False
right = False
current_key = ' '

# Handler
def start():
    global middle
    global startScreen
    startScreen = not startScreen
    middle = not middle

def keydown(key):
    """
    Key down handler
    """
    global current_key
    current_key = chr(key)
    

def keyup(key):
    """
    Key up handler
    """
    global current_key
    current_key = ' '

def newSceneLeft():
    global x
    global left
    global middle
    x = 900
    left = not left
    middle = not middle
    
def newSceneMiddleFromLeft():
    global x
    global left
    global middle
    x = 0
    left = not left
    middle = not middle   

def newSceneMiddleFromRight():
    global x
    global right
    global middle
    x = 900
    right = not right
    middle = not middle
    
def newSceneRight():
    global x
    global right
    global middle
    x = 0
    right = not right
    middle = not middle

# Handler to draw on canvas
def draw(canvas):
    if startScreen:
        canvas.draw_text('Controls:', (20, 30), 20, 'White')
        canvas.draw_text('W or Up Arrow - Go Up', (45, 55), 15, 'White')
        canvas.draw_text('A or Left Arrow - Go Left', (45, 75), 15, 'White')
        canvas.draw_text('S or Down Arrow  - Go Down', (45, 95), 15, 'White')
        canvas.draw_text('D or Right Arrow - Go Right', (45, 115), 15, 'White')
        canvas.draw_text('You are an astronaut aboard a spaceship, unfortunately the core of the ship has malfunctioned which leaves you in this spaceship ', (50, 200), 15, 'White')
        canvas.draw_text('without any way to get back home. You are a crew of 4 and you must split resources amongst yourselves whilst finding the', (50, 220), 15, 'White')
        canvas.draw_text('required materials outside the spaceship in space to fix the ship core and safely get back home.', (50, 240), 15, 'White')
    global x
    global y
    if current_key == "W" or current_key == "&":
        y -= 5
    elif current_key == "S" or current_key == "(":
        y += 5
    elif current_key == "A" or current_key == "%":
        x -= 5
    elif current_key == "D" or current_key == "'":
        x += 5
    if middle:
        canvas.draw_circle([x,y],30,1,"white","white")
        canvas.draw_line((0,300),(900,300),10,"green")
        if x < 0:
            newSceneLeft()
        if x > 900:
            newSceneRight()
    if left:
        canvas.draw_circle([x,y],30,1,"white","white")
        canvas.draw_line((900,300),(450,300),10,"green")
        if x > 900:
            newSceneMiddleFromLeft()
    if right:
        canvas.draw_circle([x,y],30,1,"white","white")
        canvas.draw_line((0,300),(450,300),10,"green")
        if x < 0:
            newSceneMiddleFromRight()
    

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 900, 600)
frame.add_button("Start Game", start)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
