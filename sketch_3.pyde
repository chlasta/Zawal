def setup():
    size(400, 400)
    textSize(70)
def draw():
    clear()
    text("Z",200,200)
    fill(22,127,173)
    
    text ("J", 170,200)
    fill(22,27,73)
    if keyPressed: 
        if key == 'z' or key == 'Z':
          fill(221,43,65)
    else:
         fill(22,27,73)
    s = createShape()
    s.beginShape()
    s.fill(216,65,132)
    s.stroke(21,65,32)
    s.vertex(50,height/2*4)
    s.vertex(80,height/2*4-30)
    s.vertex(width/3,height/2)
    s.endShape(CLOSE)
    shape(s,50,10)
