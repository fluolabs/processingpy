initialized = False

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
        fill(255, 0, 0)
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
