def showGrid(s=20, black=155, num=True):
    """Display grid lines"""
    rows = height/s
    cols = width/s
    stroke(black)
    for i in range(rows):
        line(0, s*i, width, s*i)
    for i in range(cols):
        line(s*i, 0, s*i, height)
        
    if (num):
        text("   0", 0, 10)
        text(str(width), width - 20, 10)
        
        fill(255, 0, 0)
        text("0", 0, 10)
        text(str(height), 0, height)
        fill(0)
    
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
