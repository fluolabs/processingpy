import fluo 

def setup():
    size(400, 400)
    fluo.showGrid(index=True)
    fluo.setSprite(7, 12)
    
    fluo.xyToGrid(PVector(20, 20))
    fluo.setDestination(13, 12)
    fluo.addRoad(7, 12, 13, 12)
    fluo.drawRoads()
    fluo.drawSprite()
    fluo.drawDestination()
    #fluo.printSprite()
    #fluo.setTarget(8, 12)
    #fluo.printTarget()
    fluo.turnRight()
    #fluo.commands = [0, 1]
    #fluo.test()
    
def draw():
    
    #fluo.printSprite()
    fluo.display()
    #fluo.moveForward()
    #fluo.moveForward()
    #pass
    #background(220)

    #fluo.showGrid(grid=True)
    #print(fluo.nRows, fluo.nCols)
    
    #fluo.drawRoad(7, 12, 13, 12)
    #fluo.setSprite(7, 12)
    #fluo.drawSprite()
    #fluo.drawTarget(13, 12)
    
    
def keyPressed():
    if (key == ' '):
        if (fluo.animStart):  # reset
            fluo.restart()
        fluo.start()
