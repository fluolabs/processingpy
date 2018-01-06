import fluo 

def setup():
    size(400, 400)
    fluo.showGrid(grid=True)
    fluo.setSprite(7, 12)
    fluo.setFinalTarget(13, 12)
    fluo.addRoad(7, 12, 13, 12)
    #fluo.drawRoads()
    #fluo.drawSprite()
    #fluo.drawFinalTarget()
    
def draw():
    fluo.moveForward()
    fluo.moveForward()
    #pass
    #background(220)

    #fluo.showGrid(grid=True)
    #print(fluo.nRows, fluo.nCols)
    
    #fluo.drawRoad(7, 12, 13, 12)
    #fluo.setSprite(7, 12)
    #fluo.drawSprite()
    #fluo.drawTarget(13, 12)
