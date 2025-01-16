# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, Safari, and Edge.

import simplegui
import random
import math

health = 100
inventory = []
food = 0

x = 250
y = 250
startScreen = True
left = False
middle = False
right = False
endScreen = False
astX = []
astY = []
astRotation = []
for i in range(7):
    astX.append(random.randint(10,450))
    astY.append(random.randint(0,600))
    astRotation.append(random.randint(0,360))
foodX = []
foodY = []
foodRotation = []
for i in range(4):
    foodX.append(random.randint(10,450))
    foodY.append(random.randint(0,600))
    foodRotation.append(random.randint(0,360))
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
    
def endScene():
    global left
    global endScreen
    left = not left
    endScreen = not endScreen

# Handler to draw on canvas
def draw(canvas):
    global x
    global y
    
    
    # Start Screen Code
    if startScreen:
        canvas.draw_image(startSceneBackground, (900 // 2, 600 // 2), (900, 600), (450, 300), (900, 600))
        canvas.draw_text('Controls:', (20, 30), 20, 'White')
        canvas.draw_text('W or Up Arrow - Go Up', (45, 55), 15, 'White')
        canvas.draw_text('A or Left Arrow - Go Left', (45, 75), 15, 'White')
        canvas.draw_text('S or Down Arrow  - Go Down', (45, 95), 15, 'White')
        canvas.draw_text('D or Right Arrow - Go Right', (45, 115), 15, 'White')
        canvas.draw_text('You are an astronaut aboard a spaceship, unfortunately the core of the ship has malfunctioned which leaves you in this spaceship ', (50, 200), 15, 'White')
        canvas.draw_text('without any way to get back home. You are a crew of 4 and you must split resources amongst yourselves whilst finding the', (50, 220), 15, 'White')
        canvas.draw_text('required materials outside the spaceship in space to fix the ship core and safely get back home.', (50, 240), 15, 'White')
    if current_key == "W" or current_key == "&":
        y -= 5
    elif current_key == "S" or current_key == "(":
        y += 5
    elif current_key == "A" or current_key == "%":
        x -= 5
    elif current_key == "D" or current_key == "'":
        x += 5
    
    
    # Middle Screen Code
    if middle:
        canvas.draw_image(shipBackground, (900 // 2, 600 // 2), (900, 600), (450, 300), (900, 600))
        canvas.draw_circle([x,y],30,1,"white","white")
        if x < 0:
            newSceneLeft()
        if x > 900:
            newSceneRight()
    
    
    # Variables for left screen
    global astX
    global astY
    global astRotation
    astDistance = 0
    astDistances = [0,0,0,0,0,0,0]
    global food
    global foodX
    global foodY
    global foodRotation
    foodDistance = 0
    foodDistances = [0,0,0,0]
    global health
    
    # Left Screen Code
    if left:
        canvas.draw_text(f'Health: {health}', (20, 30), 30, 'green')
        canvas.draw_image(leftSceneBackground, (900 // 2, 600 // 2), (900, 600), (450, 300), (900, 600))
        canvas.draw_circle([x,y],30,1,"white","white")
        canvas.draw_text(f'Health: {health}', (20, 580), 20, 'green')
        if x > 900:
            newSceneMiddleFromLeft()
            
        # Asteroids
        for i in range(7):    
            canvas.draw_image(asteroid, (96 / 2, 96 / 2), (96, 96), (astX[i], astY[i]), (96, 96), astRotation[i])
            astY[i] += 1
            astRotation[i] += 0.01
            if astY[i] == 650:
                astY[i] = -30
                astX[i] = random.randint(0,450)
            astDistance = math.sqrt((astX[i]-x)**2+(astY[i]-y)**2)
            astDistances[i] = astDistance
            if astDistances[i] < 50:
                health -= 5
                astY[i] = -30
                astX[i] = random.randint(0,450)
            if health == 0:
                endScene()
        # Food
        for j in range(4):    
            canvas.draw_image(foodImg, (96 / 2, 96 / 2), (96, 96), (foodX[j], foodY[j]), (35, 35), foodRotation[j])
            foodY[j] += 1
            foodRotation[j] += 0.01
            if foodY[j] == 650:
                foodY[j] = -30
                foodX[j] = random.randint(0,450)
            foodDistance = math.sqrt((foodX[j]-x)**2+(foodY[j]-y)**2)
            foodDistances[j] = foodDistance
            if foodDistances[j] < 50:
                food += 1
                foodY[j] = -30
                foodX[j] = random.randint(0,450)
    
    
    # Right Screen Code
    if right:
        canvas.draw_image(shipBackground, (900 // 2, 600 // 2), (900, 600), (450, 300), (900, 600))
        canvas.draw_circle([x,y],30,1,"white","white")
        if x < 0:
            newSceneMiddleFromRight()
    
    
    if endScreen:
        canvas.draw_text('Game Over', (300, 300), 50, 'white')



startSceneBackground = simplegui.load_image("https://media-hosting.imagekit.io//612c534ad2274622/file.png?Expires=1831565242&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=Tz4vRvNrS8C2E92Jz0~Cll4xceTCP9Hb0-va8BotgR3XcX2FFz7yAzNsr4fUMZR-XKhBJBtlEQ~7RyNSm-4ab0~zy2QNgxy40s5c74InVpLYvQqth2mWHaNKIJzVXhg8UPYOfu29IROF6c~8LFdK9c1a8HH0nMqtZAoAj0R-RuBq9Bu3-7gItJIyJVjwOrIk3BESBsB3p8ZIEVeZNBYvNg9gGM63aC-6T2a~DYUFHczTUksVzW8JJi5dJouqDVzvsTCmzu4wusT~87bSjqqmoicwNd9tzpektMupc26dbmwlZmEA-SH-lTFrJeVzX8fGBCRyI0gKN87sVAbtqfsaZQ__")
shipBackground = simplegui.load_image("https://media-hosting.imagekit.io//e84af1c9d95447a5/file.png?Expires=1831650822&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=ULYuhB6qey8f7EWTJDJlsThKMEJhMyl56saQQgYBJ6zT~LfGPzTnDrLhrok7OVg1WHO-a7StXIukoiv-Xw-77zbnT7MECFF9IV3AG11uFqwbHX76mvDqCr6tbWNNsLxB6cxO8QO8Bl0zZq9Me6TEru5jTVsv00MX~sEg5KAIF8ic2RsIKeVkgtYZPpsEcds5UDPBEQIg1kB7XznRBjS6q3li~VWwMeA70aBBjpCukcYWGRGVryWZG4W3VlPdnLkrV-vEnke23Ux7lT~xV6hWLoKPsWdVVsEVevCAJdZe0MS07Z808~ny5Lne7iS-Jb5UpgPcIZU-WbAFyzqBQUQHag__")
leftSceneBackground = simplegui.load_image("https://media-hosting.imagekit.io//849e3ae783fd488a/Screenshot%202025-01-16%20at%2011-00-30%20Images%20for%20Project%20-%20Google%20Slides(1).png?Expires=1831651536&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=TiRzumfMDR8ZfdqDQBdR0CLy~nQT~r3sq1JweMaGOcuv1IWRnMSiV5aAsQ~jGek08~il5~JbMnahUD-IupGamdz3eyL5soNXz0LkDd5dkH8SrcoGOtv8U1V6tHfmKe0svkM1LCNhXY94be~jyHggD6~hJwhMt7g3lAmE6MOOjoofWIH6zLLewXYGTOdirHW2UQWScALSbfVbQ~Onv1ECEI1AfYR55Av-XYLiTsLKuN07nmb~n~6BEfulumZlNcrTXC7V4kLI1pKaUbFnuulja2tINElDQeze5iVoNU-w6rqkuxJPML9pkefBAOdWsn0uCPJIqes0yscQLsX49Y4u0Q__")
asteroid = simplegui.load_image("https://media-hosting.imagekit.io//d32f66fb284d4efb/Asteroid%2001%20-%20Base.png?Expires=1831652413&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=S5BHK8sgNLqun6Urfp5e4gkWZXlclrC6qoUZQ6iLR-StUDvgJpGfzTam3qwtSIlrTuT5tp7cLzoUjD6Fpu37hi7veeOd9K-EiHGZ607W2oz-xpa2o52JsYgoDV~2sWXZH9qzBnUU~cutV5EmWW4k~4k7YtUdgU5DcBKin-anEx2lyTnxu5D7knuwB596GdlCbGYHw6wYmDzfuJM6xHj2rZUL7P4Hr7hEdO~SeDMSl7xbORxxoSy1vfVffcze0t~~8L75xm5N8uipglP-eDl7JAsKLDHGGE0O-T717m5pztn4qi4gbb7xMICxQcx5uibstCdTSGMezaT69VhmrbhqVA__")
foodImg = simplegui.load_image("https://media-hosting.imagekit.io//c2e2671ce14440a6/Apple.png?Expires=1831660587&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=p4kJBKpF8PcKmNYh8uuQwDqbk08dpWtSRy2orA2HhXrawYZD7WxIG3tihQBqd-ZloMM8wj6mZGVVrNrUwbhSD-CZ4Cc1y9kBTukXYWToFovIUf0GOO5neGc3jqBuTa~P3zoNrASYbKImJeTMZ7faCAVCZFuWJIOvwAjSOzNuWiaPDdcCDpCm09a~Ms523KGKlusHVtdcKrtp6MQ7v4LvMN8APZdH6Y-Fx3x6bifjFgi3t-ULUaUuh5kQ7nNHDnOGxmWBT-x3~k72JMfESmuYDYBgdi1TUjxf9~A9wwnnuBlGgmH-MOT2V7L0Y5WmhewWYFfyjHdfw4V3NELLHbPoBQ__")
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 900, 600)
frame.add_button("Start Game", start)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
