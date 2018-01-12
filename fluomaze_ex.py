import fluo 

def setup():
    size(400, 400)
    fluo.showGrid(index=True)
    fluo.setSprite(7, 12)
    #fluo.xyToGrid(PVector(20, 20))
    fluo.setDestination(13, 12)
    fluo.addRoad(7, 12, 13, 12)
    fluo.addRoad(13, 12, 13, 7)
    fluo.drawRoads()
    fluo.drawSprite()
    fluo.drawDestination()
    #fluo.printSprite()
    #fluo.setTarget(8, 12)
    #fluo.printTarget()
    fluo.moveForward()
    #fluo.moveForward()
    #fluo.turnLeft()
    #fluo.moveForward()
    #fluo.moveForward()
    
    #fluo.turnLeft()
    #fluo.commands = [0, 1]
    #fluo.moveForward()
    #fluo.moveBackward()
    #fluo.moveForward()
    #fluo.test()
    
def draw():
    fluo.display()
    
    
def keyPressed():
    if (key == ' '):
        if (fluo.animStart):  # reset
            fluo.restart()
        fluo.start()
