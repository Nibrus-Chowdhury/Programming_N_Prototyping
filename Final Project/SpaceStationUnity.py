# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, Safari, and Edge.

import simplegui
import random
import math

z = 0
g = 0
# Resources
health = 100
inventory = ["No Blue Gem","No Pink Gem","No Purple Gem","No Pink Gem"]
food = 0
water = 0

# Player Movement
x = 250
y = 250

# All Screens
startScreen = True
left = False
middle = False
right = False
endScreen = False

# Asteroid Variables
astX = []
astY = []
astRotation = []
for i in range(7):
    astX.append(random.randint(10,450))
    astY.append(random.randint(0,600))
    astRotation.append(random.randint(0,360))
# Gem Variables
gemX = 250
gemY = -30
gemRotation = 0
spawn = 0
# Food Variables
foodX = []
foodY = []
foodRotation = []
for i in range(4):
    foodX.append(random.randint(10,450))
    foodY.append(random.randint(0,600))
    foodRotation.append(random.randint(0,360))

# Water Variables
waterX = []
waterY = []
waterRotation = []
for i in range(4):
    waterX.append(random.randint(10,450))
    waterY.append(random.randint(0,600))
    waterRotation.append(random.randint(0,360))
current_key = ' '

# Middle Screen Initialization Variables
satisfaction = [100,100,100]
foodRequest = [12,24,15]
waterRequest = [8, 12, 13]

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

def satisfactionLevel():
    global satisfaction
    global right
    global middle
    global left
    global endScene
    for i in range(3):
        satisfaction[i] -= random.randint(1,5)
        if satisfaction[i] <= 0:
            right = False
            left = False
            middle = False
            endScene = True
        if satisfaction[i] > 100:
            satisfaction[i] = 100
            
def gemSpawn():
    global z
    global spawn
    z = 0
    z += 1
    spawn = random.randint(0,3)
    print(z)
            

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
    
    # Variables for middle screen
    global food
    global water
    global satisfaction
    global foodRequest
    global waterRequest
    pressurePlateX = [200,425,650]
    pressurePlateY = 300
    pPDistance = 0
    pPDistances = [0,0,0]
    global g
    # Middle Screen Code
    if middle:
        canvas.draw_image(shipBackground, (900 // 2, 600 // 2), (900, 600), (450, 300), (900, 600))
        canvas.draw_image(pressurePlate, (44 // 2, 34 // 2), (44, 34), (pressurePlateX[0], pressurePlateY), (44, 34))
        canvas.draw_image(pressurePlate, (44 // 2, 34 // 2), (44, 34), (pressurePlateX[1], pressurePlateY), (44, 34))
        canvas.draw_image(pressurePlate, (44 // 2, 34 // 2), (44, 34), (pressurePlateX[2], pressurePlateY), (44, 34))
        for i in range(3):
            pPDistance = math.sqrt((pressurePlateX[i]-x)**2+(pressurePlateY-y)**2)
            pPDistances[i] = pPDistance
            if pPDistances[i] < 50:
                if food >= foodRequest[i] and water >= waterRequest[i]:
                    food = food - foodRequest[i]
                    water = water - waterRequest[i]
                    satisfaction[i] += 10
                    foodRequest[i] = random.randint(10,20)
                    waterRequest[i] = random.randint(10,20)
        
        # Character Movement
        if current_key == "W" or current_key == "&":
            g = 1
            canvas.draw_image(characterUp, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
            y -= 2
        elif current_key == "S" or current_key == "(":
            g = 2
            canvas.draw_image(characterDown, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
            y += 2
        elif current_key == "A" or current_key == "%":
            g = 3
            canvas.draw_image(characterLeft, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
            x -= 2
        elif current_key == "D" or current_key == "'":
            g = 4
            canvas.draw_image(characterRight, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
            x += 2
        if g == 1:
            canvas.draw_image(characterUp, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
        elif g == 2:
            canvas.draw_image(characterDown, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
        elif g == 3:
            canvas.draw_image(characterLeft, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
        elif g == 4:
            canvas.draw_image(characterRight, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
            
        if x < 0:
            newSceneLeft()
        if x > 900:
            newSceneRight()
        
        # Satisfaction
        canvas.draw_text(f'Satisfaction: {satisfaction[0]}%', (150, 125), 20, 'White')
        canvas.draw_text(f'Request: {foodRequest[0]} Food', (150, 250), 20, 'White')
        canvas.draw_text(f'{waterRequest[0]} Water', (225, 275), 20, 'White')
        canvas.draw_image(yellowAstro, (146 // 2, 263 // 2), (146, 263), (225, 180), (55, 85))
        canvas.draw_text(f'Adam', (250, 175), 20, 'White')
        canvas.draw_text(f'Satisfaction: {satisfaction[1]}%', (375, 125), 20, 'White')
        canvas.draw_text(f'Request: {foodRequest[1]} Food', (375, 250), 20, 'White')
        canvas.draw_text(f'{waterRequest[1]} Water', (450, 275), 20, 'White')
        canvas.draw_text(f'Emma', (475, 175), 20, 'White')
        canvas.draw_image(blueAstro, (153 // 2, 272 // 2), (153, 272), (450, 180), (55, 85))
        canvas.draw_text(f'Satisfaction: {satisfaction[2]}%', (600, 125), 20, 'White')
        canvas.draw_text(f'Request: {foodRequest[2]} Food', (600, 250), 20, 'White')
        canvas.draw_text(f'{waterRequest[2]} Water', (675, 275), 20, 'White')
        canvas.draw_image(redAstro, (123 // 2, 243 // 2), (123, 243), (680, 180), (50, 80))
        canvas.draw_text(f'Levi', (705, 175), 20, 'White')
        canvas.draw_text(f'Total Food: {food}', (100, 500), 20, 'White')
        canvas.draw_text(f'Total Water: {water}', (100, 525), 20, 'White')
    
    
    # Variables for left screen
        # Asteroid Variables
    global astX
    global astY
    global astRotation
    astDistance = 0
    astDistances = [0,0,0,0,0,0,0]
        # Food Variables
    global foodX
    global foodY
    global foodRotation
    foodDistance = 0
    foodDistances = [0,0,0,0]
        # Water Variables
    global waterX
    global waterY
    global waterRotation
    waterDistance = 0
    waterDistances = [0,0,0,0]
    global health
        # Gem Variables
    global z
    global gemX
    global gemY
    global gemRotation
    global spawn
    gemDistance = 0
    
    # Left Screen Code
    if left:
        canvas.draw_text(f'Health: {health}', (20, 30), 30, 'green')
        canvas.draw_image(leftSceneBackground, (900 // 2, 600 // 2), (900, 600), (450, 300), (900, 600))
        canvas.draw_text(f'Health: {health}', (20, 580), 20, 'green')
        # Character Movement
        if current_key == "W" or current_key == "&":
            g = 1
            canvas.draw_image(characterUp, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
            y -= 2
        elif current_key == "S" or current_key == "(":
            g = 2
            canvas.draw_image(characterDown, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
            y += 2
        elif current_key == "A" or current_key == "%":
            g = 3
            canvas.draw_image(characterLeft, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
            x -= 2
        elif current_key == "D" or current_key == "'":
            g = 4
            canvas.draw_image(characterRight, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
            x += 2
        if g == 1:
            canvas.draw_image(characterUp, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
        elif g == 2:
            canvas.draw_image(characterDown, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
        elif g == 3:
            canvas.draw_image(characterLeft, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
        elif g == 4:
            canvas.draw_image(characterRight, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
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
        
        # Gems
        if z == 1:
            canvas.draw_image(gems[spawn], (96 // 2, 96 // 2), (96, 96), (gemX, gemY), (30, 30), gemRotation)
            gemY += 1
            gemRotation += 0.01
            gemDistance = math.sqrt((gemX-x)**2+(gemY-y)**2)
            if gemDistance < 50:
                if spawn == 0:
                    inventory[spawn] = "Blue Gem Acquired"
                elif spawn == 1:
                    inventory[spawn] = "Pink Gem Acquired"
                elif spawn == 2:
                    inventory[spawn] = "Purple Gem Acquired"
                elif spawn == 3:
                    inventory[spawn] = "Red Gem Acquired"
                z = 0
                gemX = random.randint(0,450)
                gemY = -30
                print(inventory[spawn])
            if gemY > 650:
                z = 0
                gemX = random.randint(0,450)
                gemY = -30
            
                
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
       
        # Water
        for w in range(4):    
            canvas.draw_image(waterImg, (96 / 2, 96 / 2), (96, 96), (waterX[w], waterY[w]), (35, 35), waterRotation[w])
            waterY[w] += 1
            waterRotation[w] += 0.01
            if waterY[w] == 650:
                waterY[w] = -30
                waterX[w] = random.randint(0,450)
            waterDistance = math.sqrt((waterX[w]-x)**2+(waterY[w]-y)**2)
            waterDistances[w] = waterDistance
            if waterDistances[w] < 50:
                water += 1
                waterY[w] = -30
                waterX[w] = random.randint(0,450)
    
    # Right Screen Code
    if right:
        canvas.draw_image(shipBackground, (900 // 2, 600 // 2), (900, 600), (450, 300), (900, 600))
        canvas.draw_image(shipCore, (677 // 2, 369 // 2), (677, 369), (450, 300), (400, 200))
        canvas.draw_text(f'Inventory: {inventory[0]} | {inventory[1]} | {inventory[2]} | {inventory[3]}', (100, 500), 15, 'White')
        # Character Movement
        if current_key == "W" or current_key == "&":
            g = 1
            canvas.draw_image(characterUp, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
            y -= 2
        elif current_key == "S" or current_key == "(":
            g = 2
            canvas.draw_image(characterDown, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
            y += 2
        elif current_key == "A" or current_key == "%":
            g = 3
            canvas.draw_image(characterLeft, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
            x -= 2
        elif current_key == "D" or current_key == "'":
            g = 4
            canvas.draw_image(characterRight, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
            x += 2
        if g == 1:
            canvas.draw_image(characterUp, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
        elif g == 2:
            canvas.draw_image(characterDown, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
        elif g == 3:
            canvas.draw_image(characterLeft, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
        elif g == 4:
            canvas.draw_image(characterRight, (315 // 2, 315 // 2), (315, 315), (x, y), (85, 85))
        if x < 0:
            newSceneMiddleFromRight()
        if inventory[0] == "Blue Gem Acquired" and inventory[1] == "Pink Gem Acquired" and inventory[2] == "Purple Gem Acquired" and inventory[3] == "Red Gem Acquired":
            canvas.draw_polygon([(0,0),(900,0),(900,600),(0,600)],1,'black','black')
            canvas.draw_text('You Fixed the Engine!', (300, 300), 50, 'white')
    
    
    if endScreen:
        canvas.draw_text('Game Over', (300, 300), 50, 'white')



startSceneBackground = simplegui.load_image("https://media-hosting.imagekit.io//612c534ad2274622/file.png?Expires=1831565242&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=Tz4vRvNrS8C2E92Jz0~Cll4xceTCP9Hb0-va8BotgR3XcX2FFz7yAzNsr4fUMZR-XKhBJBtlEQ~7RyNSm-4ab0~zy2QNgxy40s5c74InVpLYvQqth2mWHaNKIJzVXhg8UPYOfu29IROF6c~8LFdK9c1a8HH0nMqtZAoAj0R-RuBq9Bu3-7gItJIyJVjwOrIk3BESBsB3p8ZIEVeZNBYvNg9gGM63aC-6T2a~DYUFHczTUksVzW8JJi5dJouqDVzvsTCmzu4wusT~87bSjqqmoicwNd9tzpektMupc26dbmwlZmEA-SH-lTFrJeVzX8fGBCRyI0gKN87sVAbtqfsaZQ__")
shipBackground = simplegui.load_image("https://media-hosting.imagekit.io//e84af1c9d95447a5/file.png?Expires=1831650822&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=ULYuhB6qey8f7EWTJDJlsThKMEJhMyl56saQQgYBJ6zT~LfGPzTnDrLhrok7OVg1WHO-a7StXIukoiv-Xw-77zbnT7MECFF9IV3AG11uFqwbHX76mvDqCr6tbWNNsLxB6cxO8QO8Bl0zZq9Me6TEru5jTVsv00MX~sEg5KAIF8ic2RsIKeVkgtYZPpsEcds5UDPBEQIg1kB7XznRBjS6q3li~VWwMeA70aBBjpCukcYWGRGVryWZG4W3VlPdnLkrV-vEnke23Ux7lT~xV6hWLoKPsWdVVsEVevCAJdZe0MS07Z808~ny5Lne7iS-Jb5UpgPcIZU-WbAFyzqBQUQHag__")
leftSceneBackground = simplegui.load_image("https://media-hosting.imagekit.io//849e3ae783fd488a/Screenshot%202025-01-16%20at%2011-00-30%20Images%20for%20Project%20-%20Google%20Slides(1).png?Expires=1831651536&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=TiRzumfMDR8ZfdqDQBdR0CLy~nQT~r3sq1JweMaGOcuv1IWRnMSiV5aAsQ~jGek08~il5~JbMnahUD-IupGamdz3eyL5soNXz0LkDd5dkH8SrcoGOtv8U1V6tHfmKe0svkM1LCNhXY94be~jyHggD6~hJwhMt7g3lAmE6MOOjoofWIH6zLLewXYGTOdirHW2UQWScALSbfVbQ~Onv1ECEI1AfYR55Av-XYLiTsLKuN07nmb~n~6BEfulumZlNcrTXC7V4kLI1pKaUbFnuulja2tINElDQeze5iVoNU-w6rqkuxJPML9pkefBAOdWsn0uCPJIqes0yscQLsX49Y4u0Q__")
asteroid = simplegui.load_image("https://media-hosting.imagekit.io//d32f66fb284d4efb/Asteroid%2001%20-%20Base.png?Expires=1831652413&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=S5BHK8sgNLqun6Urfp5e4gkWZXlclrC6qoUZQ6iLR-StUDvgJpGfzTam3qwtSIlrTuT5tp7cLzoUjD6Fpu37hi7veeOd9K-EiHGZ607W2oz-xpa2o52JsYgoDV~2sWXZH9qzBnUU~cutV5EmWW4k~4k7YtUdgU5DcBKin-anEx2lyTnxu5D7knuwB596GdlCbGYHw6wYmDzfuJM6xHj2rZUL7P4Hr7hEdO~SeDMSl7xbORxxoSy1vfVffcze0t~~8L75xm5N8uipglP-eDl7JAsKLDHGGE0O-T717m5pztn4qi4gbb7xMICxQcx5uibstCdTSGMezaT69VhmrbhqVA__")
foodImg = simplegui.load_image("https://media-hosting.imagekit.io//c2e2671ce14440a6/Apple.png?Expires=1831660587&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=p4kJBKpF8PcKmNYh8uuQwDqbk08dpWtSRy2orA2HhXrawYZD7WxIG3tihQBqd-ZloMM8wj6mZGVVrNrUwbhSD-CZ4Cc1y9kBTukXYWToFovIUf0GOO5neGc3jqBuTa~P3zoNrASYbKImJeTMZ7faCAVCZFuWJIOvwAjSOzNuWiaPDdcCDpCm09a~Ms523KGKlusHVtdcKrtp6MQ7v4LvMN8APZdH6Y-Fx3x6bifjFgi3t-ULUaUuh5kQ7nNHDnOGxmWBT-x3~k72JMfESmuYDYBgdi1TUjxf9~A9wwnnuBlGgmH-MOT2V7L0Y5WmhewWYFfyjHdfw4V3NELLHbPoBQ__")
waterImg = simplegui.load_image("https://media-hosting.imagekit.io//aa0be2c619154052/bottle_1_-removebg-preview.png?Expires=1831683845&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=vXa5oAE~Y6fRw8qS7RTD1Rt~xNc3ErWNCUBra0SJZ-Xk9ajGQ1HG2HidADT-rLUaPud~xJ4DFCJPbhvVYhpq0JEFQfETZCnsW88eyYPiD4B0C0aqW2-y4mSoXHOhiXsp5tvf286OVQ3YP8ZMnzUHfzaGhPulYyTi6DbPl30Rw23GYjuHad8UJQD9mlXFTalFI9Jxax~NxHntu-JCJs9k4EZjxdH~qXURqYailmDg1Dd39aIbtEm3N2AdDcs6b1m8zj00kRpIMJIqsOBMF1yQWrRYYh-i~z3WoGBKEiABAL5kTNNpVeaWQM2KdUe1CvWlQW-c2Fv2QMZ8bkl-ydZC9Q__")
pressurePlate = simplegui.load_image("https://media-hosting.imagekit.io//921ad7c09e1e4d36/Screenshot%202025-01-16%20203741.png?Expires=1831685882&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=QBvOH3~a5b9ypgDAOZyfDpAbk3Ve0UgguITWVp6mGIW167at5cAfYaB3IBLa327TFyENLEdJD9HFwR3gTcsTCvj7mVg1-kP7t-G7yBpPfHzQzml4z1c3PjKbrGN1ViMfVhtWp6AKDr-FE8gpmqlVreSkc-Gl4-DxMMaIRx3O0I1RQm3Imt4jluKudPTdGKBLvD3hXvgqXIGCrgas9bK~jTeUCF3m7LrxygYYC8L5OMoQZKAef4bb9dujskBwQNd3kQXYxsj1u0CqJLNSxozvleZhp9UOWrJL2L0gTXgJ4JZ59kPqWROQ4j5ZH8NpN1nnmjICTqnxPdZpo7jz1wl3yw__")
gem1 = simplegui.load_image("https://media-hosting.imagekit.io//fe916b26bb5f4f70/gem1(1).png?Expires=1831689618&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=hq4g14o5yI79Uv5ktvHt-S~2ZNLB46iOGofQjzh~hIrbnZCeA8qGCwIfen9NrzchbjM91yjTP8olgx7fW2K4oH3qNMhWet8b9n~LGN1it0WvRNf-VJ6gEJriGynhtxbHljs7Bu64BPJ6SVybNjQMNFtysP0ZnW6fcammGosYtygblByaqn8tX0zri3uaJ1m3G~x0i6o-qOuLWisE~uo4tyD0qTXIQp3AoLUe73ow6lzuIBXpuApb85S02PIYe0K3chgAFuaB2ESB1VRtjkGW9kS2O--X6TfniZ661nCEcHa0MGDY4OMDmRpWbWreFQXrqMI1fawtXP54hZ1oPWtDHg__")
gem2 = simplegui.load_image("https://media-hosting.imagekit.io//aaa3e92b84e64c27/gem2(1).png?Expires=1831689618&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=O0ONIJI7iMwI9hgHoQvLlKvXueUkviQhfABRNRBksV8ARzGaOSlwdvEwUXFRjto8bQCo1rvfjSeCokjBbyogizepckyWajQloyZ4plKMdmeIm82T0e97Ds5aX2S9MOzu5mnU0Q2X1K1a8eJ5B6OPpiBK4~wMfPx8nyKXvaAkansNKMNQHFY8Z4bsBQjwyOZTrvS8FLBLfx88WQUJjuhHBETjXuz2RjU1v-tSme~Ct7yqtYP8RKWxjqMOXnsIhxXG0-HAIMe2CI8ei4Y497m60cEPCGHs728cXhaUPBF8~3OTZu5kjhxX9syhkYDt5cAUIIM9bNz-PMnUrf9P-z-fvg__")
gem3 = simplegui.load_image("https://media-hosting.imagekit.io//48cb938aba554f01/gem3(1).png?Expires=1831689618&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=1i0ZvNedr8qN3JOnK3wTd5w3qf1Ho9HWWB60geT~aSBLSUAwSkgypviyY6Z22aGjJNajgzCWEGm00BnnCV4It1b~KQl3zK-1Dms~TQEzq8q5g-gvTHWYtmK7EiDn1NOqPS910pjmzWS-CSLOPo8A1CzjvsTaaTwaw4apQ~NdvihNqfcLho4KJftCbk4da1qZMuNkAq3PJqA4Aio876RerIKLGnuZzWMUTc~pGdLWvYN9WGZJgJbs08qJWnkarcCewtqg6DsmvhBmUa1KFsI0eykjHjN~NzFvY1fDFXQDjSKTl-gETxN4gnTCXcG68-LZOOSYJpCQrk86j2x7lwEstA__")
gem4 = simplegui.load_image("https://media-hosting.imagekit.io//24613d44ecaf49d8/gem4(1).png?Expires=1831689618&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=xM8xthDR~Jbumf6Ek0CC1QSAvrr654ciPjtDjIecLwf0ByJ8GZ1dN1AswHYrNtNb3JyKJL1U6f5z~aLjcosJSZv4Eg-sWWqwwffC7s4WATHO~Cue9ifLI-KzX7lR0-Jh5XC~0WPIBK6Qqhrh-pixQqEFeklf1optqrbJp05uNvkzTS-oc39slcmjSf8xy77N6IWM7jNpbXJB0eVNtNCCGIDOofTEA8~6aJo8QwYhtJFqk~G6Fqt4LIS9FW6BOX2Do5NgiH-dUfVa8r~0yjeH3-BvDSRtwTmaHX7oXFuA22zMVHe5h~bt-y8To3gqeMKQzl92-blzYkyIyVeS5kyIpQ__")
gems = [gem1,gem2,gem3,gem4]
yellowAstro = simplegui.load_image("https://media-hosting.imagekit.io//3772cfe9cbfe4ce1/yellowAstronaut-removebg-preview.png?Expires=1831694135&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=fZEkDpBHksu8noiHRmRzcdJ2bfCRKofAtDuv8k7bra8ixHXkRYAg5jvnN91cebJTUJqaBIMB8ZPH2pwdbUj3TiBeiFwIS5B~3VJyNl2mH9ExAEzR--jzRQ3gS~xfumOcA5RlnIr7tpPSVI3zfQRmTtV2oupVAA85CmDOrLg-reDz0MlArYfOUbu0dAK~MWGyjCrjKtfdSiNRyBLs0NMWf0LtSeMLh0A0pM9nBt-q~LaNIjc9BORsMRORGxOzjmRcIgvQwvMAZMyRlt-NmnHwHoNMmeUzDYKV-Z9gP2feRoogSxbLoyxSGYOYrz96UVZZx5dyrdyfUKUYGzRG~qBbxw__")
blueAstro = simplegui.load_image("https://media-hosting.imagekit.io//20516db3d84b476c/blueAstronaut-removebg-preview.png?Expires=1831694135&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=N2OnPpYEGg0oTES0ydzuoecGW6auuA~cu-7Md1uedAMgTMjgX1kec9YYmieAZJp35Axv3E8CmZsrTWFrHwz4zwk9b~t40BTMA3N40bVe7bKDZJgcNTgXiqtRymPH5Itn2ZaDL7ssyrG4KPY8ZBkegEW9An0emeOIsXZnirbcmCkxvnASye~D14y~O0Z425PauI2Am9r5RDuswUW3BZhNe82GgHXIz2zmWo-KHBhzWlQyvQf0BK1CY6pgvPZmXXEBVe6GL7hRjgCcro4v2-z3c6dJdH9iFsCJaRu5D2SgVPBAzbAhrQkGy3Y1ux6jVcou5Qn1k3Q1MbSFuhl4A6RXJw__")
redAstro = simplegui.load_image("https://media-hosting.imagekit.io//6139a780c7024de3/redAstronaut-removebg-preview.png?Expires=1831694135&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=cLbFBFstSekvB6XDD12GupNcG0wHvqw~uYlprrHslqhJsIxdXWdBOzIeoIbAjm9icN0pLdSKEeY~PRFgBw-ibsydC06Zk-FUn2575oYG0eJeR~zeNu8ukyhn3cBT8WtYtZA74wibGJQv94oeTDPBX-irIz-arElr3u9RZ6~O71Rsa1Xskc~4OedPZXibw1jkDtrbLt~Z~8uwbdOitgEaLocBFRceYdwcuQDkmZPo2WAqaE7lq7UNQTqiKXrXp-HzNp5r-04aSmY1mEmO~FZm6mW1Dz7niyB1ipU2nBFORCVPWZKs0DOZZYwhvju6cmyfUyTgRJRBQ-5JXga6LI3sZQ__")
characterUp = simplegui.load_image("https://media-hosting.imagekit.io//29b244212c774ba4/upspaceman.png?Expires=1831694745&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=eBp2tteXeTKV2-Abt13b0pQYDryiCdqrQAxrILJKfH1jsbWsjCq4pNmmUcuulH5IkiImGc2lQxpLWGEWgdXnLjMT2HnAbuXF8W2-uEGMmyBSKUIDW-a~rg7GeDKHv~I3~cYaUd-bL7CLIkh2zd2K-lQsiqQO9g6-N0nin6~ynjKk0dhH-HEmLMC64GddAIOTtXAy~TIpwEgUklOuPidIcGxrzZaw3qKV3oQqqZWRjDNQUQkuhNPiR3xJFxKU-bBQ7N-SfbSE9olikf1Bi7hULMTGzvPbZs698Pl-GUf-uFf5B5xUOf1NOvdw2eApVdXkC9fcRE~e-B5JJpA9hT9GYA__")
characterDown = simplegui.load_image("https://media-hosting.imagekit.io//50ab470f5f9f476e/downspaceman.png?Expires=1831694745&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=PIuROY9HLqZF9V4EyPQWCY1NVXhHhf2J-jjUm0l3leRcvHY0Y4MPD46-0TQ~mypnZ7bEaslJiy~TyyEZ5Ta8veJkSLWRwJugtbKf6~Q1p4yz74qQcg6eO54JI71K889VVQzofBag~bT-j9Sn-Z0sCBg4D3A~7nlFn-74C5tDFUO81KVbyeSDIG2lScazGc9np0PpOhbC7o0DC7KtBRxjFmOHnayA~26s-Grkzsq1WFO7-a~aOZ9EPSGSwAwocuMLQveD-b~VItyhGZtEV6I6B0QxPRlpd5TCtJfpsGJFEqMUpyGN1kwmlW8zMMoi69wdY7k5SO~5aKrAuiV2f0gt8g__")
characterLeft = simplegui.load_image("https://media-hosting.imagekit.io//8653378712664045/leftspaceman.png?Expires=1831694745&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=zPing5FKemyXYzSldDsXRAbQNfyfOVlfv89UDiq9XsJpjQ6LxIJzvteh2HBcgPZ4qavD9FP3auzAE8rI6YSclekexNLFuMfkzUuv1NeKYZvrOuKByPeCZ1QsEYhZqAkW~p-J7P~cEmGjzgs70t8YH5FIsNZUnRsGPZitPdHDETA13Wu5U04cGH0qGc4LwMcYmbOdSqupFtfesdSua7-vFT~00eMNNtf4mY97D6YuxWfCsRIGVl1GqLpC~yTozs2eXDTlFm4tIKUdhBIVN8t1T4VC7wg17Kr5X4NWA1p9QTOFhQ5chnVKCZFqaTGcvgVfjyI0PVQ~vXpZzPLV9T1G0w__")
characterRight = simplegui.load_image("https://media-hosting.imagekit.io//6160d96ef85a422c/rightspaceman.png?Expires=1831694745&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=nAXYnOobUOTVXuJt2B3zoUTdYgkHhmsx0AxAofr3o-s2tAD9kzoP~L-BspuJPbfIfCPBLARzqTb6QIvvJSpXjr~RdSRXPHGSoQfmDZdHvxn96PSAhCDO41xu3Klq5DxvLDZWJ7Cu301tjN-06wmJBORzZDdqetVAaJZ-qGclJX8wEKG~FMYvHF~Q9Aatd2TD86LZB7szMHnm7MMUQcxpabTdSUuuyQOB~Jpa9cvUvudPQ5qmECKCNzZWd-kXg~BaKzuItZco0~gRqvFoZSR72EPHkM24krILYE6nF-OHVbrBYYV7AJzxyo5HbZjuKdf2wBBW19ENOzSVBJykkT2G1Q__")
shipCore = simplegui.load_image("https://media-hosting.imagekit.io//6cb3fd9fcfa64c69/image_fx__2_-removebg-preview.png?Expires=1831697123&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=HbCts4GOusERHTq7pAFcEB08OTlStmqhrRibXQkQ1qMcsimX02eBwJNd2sc8-U6nXBDCE5GTBqG45yz8ZvyjkiBGk6Gt-I97mpyon-N1okSNLAjjDoUWnR91udTuUIhsP6~XyeJKteqg5TuwrIWycQNyNfOgB3IP2IxWxj1qDyK-G-0~wc0fe5K~DlgjP3YIYXaFzqUMa1rdzA87IH3NWRmAE8KdpyUDjR0HXFw5p3RzdLilS7A08ccsb2KZ5E0bm-YsvqCD-DSRrah0XSmSN7I14aEv-EtCr9ta6BpCZKc3Xg~FsitEIMYX9dx3r4jYxg-VCaKQiRTH5PRNj6tgTg__")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 900, 600)
timer = simplegui.create_timer(random.randint(5000,15000), satisfactionLevel)
gemTimer = simplegui.create_timer(random.randint(25000,45000), gemSpawn)
frame.add_button("Start Game", start)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)



# Start the frame animation
frame.start()
timer.start()
gemTimer.start()
