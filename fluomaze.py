
resolution = 20
nRows = 0
nCols = 0
initialized = False
debug = False
spriteDirection = "Right"
spriteLoc_g = PVector(0, 0)
targetLoc_g = PVector(0, 0)
finalTarget_g = PVector(0, 0)
spriteLoc = PVector(0, 0)
target = PVector(0, 0)
finalTarget = PVector(0, 0)


speed = 1
roads = []
spriteSet = False
targetSet = False
finalTargetSet = False

def initGrid(r=20):
    global nRows, nCols, resolution, initialized
    nRows = height/r
    nCols = width/r
    initialized = True
    resolution = r
    
def showGrid(r=20, lineColor=155, lineWeight=1, dimension=False, grid=True):
    global nRows, nCols, resolution, initialized
    """Display grid lines"""
    if (initialized == False):
        initGrid(r)
        
    pushStyle()
    stroke(lineColor)
    strokeWeight(1)
    for i in range(nRows):
        line(0, r*i, width, r*i)
    for i in range(nCols):
        line(r*i, 0, r*i, height)
        
    if (dimension):
        fill(0)
        text("   0", 0, 10)
        text(str(width), width - 20, 10)
        fill(255, 0, 0)
        text("0", 0, 10)
        text(str(height), 0, height)
    else:
        if (grid):
            fill(255, 0, 0)
            for i in range(nRows):
                text(str(i), 0, r*(i+1))
            fill(0)
            for i in range(nCols):
                text(str(i), r*(i), 10)
    popStyle()
    
def addRoad(xg1=4, yg1=4, xg2=10, yg2=10):
    global roads
    roads.append((PVector(xg1*resolution + resolution/2, yg1*resolution + resolution/2),
                  PVector(xg2*resolution + resolution/2, yg2*resolution + resolution/2)))
    
def drawRoads():
    """ xg1, yg1: starting grid number,
    xg2, yg2: ending grid number"""
    global nRows, nCols, resolution, initialized
    pushStyle()
    strokeWeight(20)
    stroke(255, 255, 0)
    #strokeCap(SQUARE)
    for i in range(len(roads)):
        #print(roads[i][0])
        #print(roads[i][1])
        line(roads[i][0].x,roads[i][0].y, roads[i][1].x,roads[i][1].y)  
        #line(xg1*resolution + resolution/2, yg1*resolution + resolution/2,
        #xg2*resolution + resolution/2, yg2*resolution + resolution/2)
    popStyle()
    
def setSprite(xg, yg, direction="right"):
    global nRows, nCols, resolution, initialized, spriteLoc, spriteLoc_g, spriteDirection, spriteSet
    x = xg*resolution + resolution/2
    y = yg*resolution + resolution/2
    spriteLoc_g = PVector(xg, yg)
    spriteLoc = PVector(x, y)
    spriteDirection = direction
    spriteSet = True


def setTarget(xg, yg):
    global target, target_g, targetSet, resolution
    x = xg*resolution + resolution/2
    y = yg*resolution + resolution/2
    target_g = PVector(xg, yg)
    target = PVector(x, y)
    targetSet = True

def setFinalTarget(xg, yg):
    global finalTarget, finalTarget_g, finalTargetSet
    x = xg*resolution + resolution/2
    y = yg*resolution + resolution/2
    finalTarget_g = PVector(xg, yg)
    finalTarget = PVector(x, y)
    finalTargetSet = True

def updateSprite():
    global spriteLoc, target, targetSet, spriteDirection, speed
    dir = spriteDirection
    if (spriteLoc == target):
        targetSet = False
        print(targetSet)
    else:
        if (dir == "right"):
            spriteLoc.x += speed
        elif (dir == "bottom"):
            spriteLoc.y += speed
        elif (dir == "left"):
            spriteLoc.x -= speed
        else:
            spriteLoc.y -= speed
            
def drawSprite():
    # Draw a triangle rotated in the direction of velocity
    if (spriteSet == False):
        print("Sprite is not set")
        return
    
    dir = spriteDirection
    if (dir == "right"):
        theta = radians(90)
    elif (dir == "bottom"):
        theta = radians(180)
    elif (dir == "left"):
        theta = radians(270)
    else:
        theta = radians(0)

    r = 8        
    fill(0, 255, 0)
    stroke(0)
    pushMatrix()
    translate(spriteLoc.x, spriteLoc.y)
    rotate(theta)
    beginShape(PConstants.TRIANGLES)
    vertex(0, -r*2)
    vertex(-r, r)
    vertex(r, r)
    endShape()
    popMatrix()

def drawFinalTarget():
    """xg, yg: location in grid,
    direction: right, left, top, bottom"""
    global finalTarget, finalTargetSet
    if (finalTargetSet == False):
        print("Final target is not set")
        return
    
    fill(255, 0, 0)
    ellipse(finalTarget.x, finalTarget.y, 15, 15)
    
 
def display():
    background(220)
    showGrid(grid=True)
    drawRoads()
    drawTarget()
    drawSprite()
    
def moveForward(gridDist = 3):
    """ Move gridDist at a time in the sprite direction"""
    global spriteLoc, spriteDirection, speed, target_g, target, targetSet
    if (targetSet == False):
        dir = spriteDirection
        next_g = PVector(spriteLoc_g.x, spriteLoc_g.y) 
        if (dir == "right"):
            next_g.x += gridDist
        elif (dir == "bottom"):
            next_g.y += gridDist
        elif (dir == "left"):
            next_g.x -= gridDist
        else:
            next_g.y -= gridDist
            
        x = next_g.x*resolution + resolution/2
        y = next_g.y*resolution + resolution/2
        
        next = PVector(x, y)
        target_g = next_g
        target = next
       
        targetSet = True
        print(target)
    
    

    background(220)
    showGrid(grid=True)
    drawRoads()
    drawFinalTarget()
    drawSprite()
    updateSprite()
    

    
        
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
