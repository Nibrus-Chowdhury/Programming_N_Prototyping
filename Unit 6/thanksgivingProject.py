'''
Nibrus Chowdhury
Period 5-6
12/2/24
Description: A thanksgiving scene created with the basic shape functions learned in class. Scene includes
a turkey and trees in a gradient going from the outside green leaves to the inside fall colored leaves. The
turkey is in the middle with grass that is swaying in the wind, hence why it keeps moving. The turkey and the
trees are strong however and do not budge to wind. Turkeys name is Arnold.
'''
import simplegui
import random

# Frame setup
frame = simplegui.create_frame("Thanksgiving Drawing", 600, 400)

# Variables
redishBrown = "#de5714"
brown = "#a65c12"
yellowishBrown = "#e8d138"
orange = "#f29e0c"

# Draw handler function
def draw(canvas):
    # Background
    canvas.draw_polygon([(0, 200), (0,400), (600, 400), (600, 200)], 1, "black", "green")
    canvas.draw_polygon([(0, 0), (0,200), (600, 200), (600, 0)], 1, "black", "cyan")
    # Grass
    for i in range(100):
        grassX = random.randint(0,600)
        grassY = random.randint(200,400)
        canvas.draw_point((grassX,grassY), "lightgreen")
    # Trees
        # Central Tree
    canvas.draw_polygon([(267.5, 255), (267.5, 105), (292.5, 105,), (292.5, 255)], 1, "black",brown)
    canvas.draw_circle((280, 90), 60, 1, "black", orange)
        # Variable Initialization
    x = 0
    x2 = 0
    x3 = 0
        # Loop that repeats twice to create two of the same trees off-set by a certain x value
    while x<=200:
        canvas.draw_polygon([(170+x, 275), (170+x, 125), (195+x, 125,), (195+x, 275)], 1, "black",brown)
        canvas.draw_circle((182.5+x, 105), 60, 1, "black", yellowishBrown)
        canvas.draw_polygon([(100+x2, 150), (100+x2,300), (125+x2, 300), (125+x2, 150)], 1, "black", brown)
        canvas.draw_circle((112.5+x2, 112.5), 60, 1, "black", redishBrown)
        canvas.draw_polygon([(55+x3, 175), (55+x3, 325), (80+x3, 325), (80+x3, 175)], 1, "black", brown)
        canvas.draw_circle((67.5+x3, 160), 60, 1, "black", "#606c38")
        x = x + 200
        x2 = x2+350
        x3 = x3+440
    # Turkey Legs
    canvas.draw_line((260,330),(260,355), 3, "black")
    canvas.draw_line((300,330),(300,355), 3, "black")
    canvas.draw_line((254,360),(259,355), 1, "black")
    canvas.draw_line((260,363),(260,355), 1, "black")
    canvas.draw_line((266,360),(261,355), 1, "black")
    canvas.draw_line((294,360),(299,355), 1, "black")
    canvas.draw_line((300,363),(300,355), 1, "black")
    canvas.draw_line((306,360),(301,355), 1, "black")
    
    # Turkey Body
    canvas.draw_circle((250, 275), 20, 1, "black", "#9a4606")
    canvas.draw_circle((260, 265), 20, 1, "black", "#9a4606")
    canvas.draw_circle((270, 260), 20, 1, "black", "#9a4606")
    canvas.draw_circle((280, 260), 20, 1, "black", "#9a4606")
    canvas.draw_circle((290, 265), 20, 1, "black", "#9a4606")
    canvas.draw_circle((300, 275), 20, 1, "black", "#9a4606")
    canvas.draw_circle((280, 300), 40, 1, "black", "grey")
    
    # Turkey Head & Neck
    canvas.draw_polygon([(300,280),(310,290),(335,265),(325,255)], 1, "grey", "grey")
    canvas.draw_circle((330,260), 20, 1, "grey", "grey")
    
    # Turkey Eyes & Beak
    canvas.draw_circle((345,260), 2, 1, "black", "black")
    canvas.draw_polygon([(345, 275),(355,285),(350,270)], 1, "yellow", "yellow")
    
# Assign draw handler to the frame
frame.set_draw_handler(draw)

# Start the frame
frame.start()
