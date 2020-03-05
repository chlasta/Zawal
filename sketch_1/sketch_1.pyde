def setup():
    size(800,800)
def draw():
    if mousePressed:
        rect(mouseX,mouseY,80,80)    
    else:
        line(mouseX,mouseY,70,50)
    
