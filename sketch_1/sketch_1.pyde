def setup():
    size(800,800)
def draw():
    if mousePressed:
        line(mouseX,mouseX, mouseY, mouseY)
    else:
        rect(mousePressed,50,100,100)
