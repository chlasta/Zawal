def setup():
    size(800,800)
def draw():
    if mousePressed:
        rect(mouseX,mouseY,80,80) # lepiej byłoby użyć wartości relatywnych (height, width), zamiast sztywnych  
    else:
        line(mouseX,mouseY,70,50)
#1,75p
    
