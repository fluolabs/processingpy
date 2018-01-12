# constant values
dirUp = 0    # 0
dirRight = 1 # 90
dirDown = 2  # 180
dirLeft = 3  # 270 degrees

mForward = 0
mBackward = 1
tRight = 2
tLeft = 3

# configuration values
resolution = 20
nRows = 0
nCols = 0
initialized = False
debug = False
spriteDir = dirRight
spriteAngle = 90
targetAngle = 90

spriteLoc = PVector(0, 0)  # in grids
orgSpriteLoc = PVector(0, 0)
spriteXY = PVector(0, 0)   # in pixel

targetLoc = PVector(0, 0)  
targetXY = PVector(0, 0) 
destination = PVector(0, 0) 
destinationXY = PVector(0, 0) 

speed = 1
turnSpeed = 1
roads = []
commands = []
orgCommands = []
curCommand = None
spriteSet = False
targetSet = False
targetAngleSet = False
destinationSet = False
animStart = False

def start():
    global animStart
    animStart = True

def angleToDirection(angle):
    ang = angle % 360
     
    if (ang >= 0 and ang < 90):
        dir = dirUp
    elif(ang >= 90 and ang < 180):
        dir = dirRight
    elif(ang >= 180 and ang < 270):
        dir = dirDown
    else:
        dir = dirLeft

    return(dir)
                        
    
def restart():
    global commands, orgCommands
    commands = list(orgCommands) # https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
    animStart = True
    setSprite(spriteLoc.x, spriteLoc.y)
    #print(commands)
    
 
    
def showGrid(r=20, lineColor=155, lineWeight=1, index=False, w=None, h=None):
    """Display grid lines"""
    global nRows, nCols, resolution, initialized
    if (w == None):
        w = width
    if (h == None):
        h = height

    if (initialized == False):
        nRows = h/r
        nCols = w/r
        initialized = True
        resolution = r
    
    pushStyle()
    stroke(lineColor)
    strokeWeight(1)
    textSize(12)
    for i in range(nRows + 1):
        line(0, r*i, w, r*i)
    for i in range(nCols + 1):
        line(r*i, 0, r*i, h)
        
    if (index):
        fill(255, 0255, 0)
        for i in range(nRows):
            text(str(i), 0, r*(i+1))
        fill(0)
        for i in range(nCols):
            text(str(i), r*(i), 10)
    else:
        fill(150)
        text("   0", 0, 10)
        text(str(w), w - 20, 10)
        fill(255, 0, 0)
        text("0", 0, 10)
        text(str(h), 0, h)
        
    popStyle()
    
def addRoad(xg1, yg1, xg2, yg2):
    global roads
    roads.append((PVector(xg1, yg1), PVector(xg2, yg2)))
    
def printRoads():
    for i in range(len(roads)):
        print("road " + str(i+1) + ": " + str(roads[i][0].x) + " " + str(roads[i][0].y) + 
              " " + str(roads[i][1].x) + " " + str(roads[i][1].y)) 

def drawRoads():
    pushStyle()
    strokeWeight(20)
    stroke(255, 255, 0)
    #strokeCap(SQUARE)
    for i in range(len(roads)):
        rStart = gridToXY(roads[i][0])
        rEnd = gridToXY(roads[i][1])
        line(rStart.x, rStart.y, rEnd.x, rEnd.y)  
    popStyle()
 
def gridToXY(g):
    return (PVector(g.x*resolution + resolution/2, g.y*resolution + resolution/2))

def xyToGrid(loc):
    return (PVector(floor(loc.x / resolution), floor(loc.y / resolution)))
   
def setSprite(xg, yg, direction=dirRight):
    global spriteLoc, spriteXY, spriteSet, spriteAngle
    spriteLoc = PVector(xg, yg)
    spriteXY = gridToXY(spriteLoc)
    if (direction == dirUp):
        spriteAngle = 0
    elif (direction == dirRight):
        spriteAngle = 90
    elif (direction == dirDown):
        spriteAngle = 180
    elif (direction == dirLeft):
        spriteAngle = 270
    
    orgSpriteAngle = spriteAngle
    spriteSet = True

def printSprite():
    print("spriteLoc:" + str(spriteLoc.x) + " " + str(spriteLoc.y) + 
          "spriteXY:" + str(spriteXY.x) + " " + str(spriteXY.y))

def printTarget():
    print("targetLoc:" + str(targetLoc.x) + " " + str(targetLoc.y) + 
          " targetXY:" + str(targetXY.x) + " " + str(targetXY.y))

        
def setDestination(xg, yg):
    global destination, destinationXY, destinationSet
    destination = PVector(xg, yg)
    destinationXY = gridToXY(destination)
    destinationSet = True

def printDestination():
    print("destination:" + str(destination.x) + " " + str(destination.y))
    
    
def setTarget(xg, yg):
    global targetLoc, targetXY, targetSet
    targetLoc = PVector(xg, yg)
    targetXY = gridToXY(targetLoc)
    targetSet = True

def updateSprite():
    """ return true if reaching the target else return false"""
    global spriteLoc, sprintXY, targetSet,  commands 
    if (spriteXY == targetXY):  # reach the target
        print("reached target!")
        commands.pop(0)
        targetSet = False
        return True
    else:
        if (spriteDir == dirRight):
            spriteXY.x += speed
        elif (spriteDir == dirDown):
            spriteXY.y += speed
        elif (spriteDir == dirLeft):
            spriteXY.x -= speed
        else:
            spriteXY.y -= speed
            
        spriteLoc = xyToGrid(spriteXY)

def updateSpriteAngle():
    """ return true if reaching the target else return false"""
    global spriteAngle, targetAngleSet, commands, spriteDir 
    if (spriteAngle == targetAngle):  # reach the target
        print("reached target angle!")
        commands.pop(0)
        targetAngleSet = False
        spriteDir = angleToDirection(spriteAngle)
        return True
    else:
        spriteAngle += turnSpeed

def drawSprite():
    # Draw a triangle rotated in the direction of velocity
    if (spriteSet == False):
        print("Sprite is not set")
        return
    
    theta = radians(spriteAngle)

    r = 8        
    fill(0, 255, 0)
    stroke(0)
    pushMatrix()
    translate(spriteXY.x, spriteXY.y)
    rotate(theta)
    beginShape(PConstants.TRIANGLES)
    vertex(0, -r*2)
    vertex(-r, r)
    vertex(r, r)
    endShape()
    popMatrix()

def drawDestination():
    if (destinationSet == False):
        print("Destination is not set")
        return

    fill(255, 0, 0)
    ellipse(destinationXY.x, destinationXY.y, 15, 15)
    
 
def display(grid=True):
    if (animStart):
        if (len(commands) !=0):
            cur = commands[0]
            if (cur[0] == mForward):
                __move(mForward, cur[1])
            elif (cur[0] == mBackward):
                __move(mBackward, cur[1])
            elif (cur[0] == tRight):
                __turn(tRight, cur[1])
            elif (cur[0] == tLeft):
                __turn(tLeft, cur[1])
        
    background(220)
    if (grid):
        showGrid(index=True)
    drawRoads()
    drawDestination()
    drawSprite()

def turnRight(amount = 90):
    commands.append((tRight, amount))
    orgCommands.append((tRight, amount))

def turnLeft(amount = 90):
    commands.append((tLeft, amount))
    orgCommands.append((tLeft, amount))
    
def __turn(type = tRight, amount = 90):
    global targetAngle, targetAngleSet, turnSpeed
    if (targetAngleSet):
        updateSpriteAngle()
    else:
        if (type == tRight):
            turnSpeed = abs(turnSpeed)
        elif (type == tLeft):
            turnSpeed = -1 * abs(turnSpeed)
            amount *= -1
            
        targetAngle = spriteAngle + amount
        targetAngleSet = True

    
def moveForward(amount = 3):
    commands.append((mForward, amount))
    orgCommands.append((mForward, amount))
    
def moveBackward(amount = 3):
    commands.append((mBackward, amount))
    orgCommands.append((mBackward, amount))

def __move(type = mForward, amount = 3):
    """ return True if the move forward is done, otherwise return false"""
    global spriteLoc, targetLoc, targetXY, targetSet, speed
    if (targetSet):
        updateSprite()
    else:
        if (type == mForward):
            speed = abs(speed)
        if (type == mBackward):
            speed = -1 * abs(speed)
            amount *= -1
        print(spriteDir)
        targetLoc = spriteLoc.get()
        if (spriteDir == dirRight):
            targetLoc.x += amount
        elif (spriteDir == dirDown):
            targetLoc.y += amount
        elif (spriteDir == dirLeft):
            targetLoc.x -= amount
        else:
            targetLoc.y -= amount
            
        targetXY = gridToXY(targetLoc)
        targetSet = True

        
# Renders a vector object 'v' as an arrow and a position 'loc'
def drawVector(v, pos, scayl):
    pushMatrix()
    arrowsize = 6
    # Translate to position to render vector
    translate(pos.x, pos.y)
    stroke(0)
    strokeWeight(2)
    # Call vector heading function to get direction (pointing up is a heading of 0)
    rotate(v.heading2D())
    # Calculate length of vector & scale it to be bigger or smaller if necessary
    len = v.mag()*scayl
    # Draw three lines to make an arrow 
    line(0, 0, len, 0)
    line(len, 0, len-arrowsize, +arrowsize/2)
    line(len, 0, len-arrowsize, -arrowsize/2)
    popMatrix()
