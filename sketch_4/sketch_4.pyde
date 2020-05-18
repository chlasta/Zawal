add_library('pdf')
def setup():
    global img 
    size (400,400) # to nie jest proporcja zdjęcia dokumentowego
    img=loadImage ('jj.jpg')
    beginRecord(PDF, "outjj.pdf")

def draw():
    global img
    image(img, 0,0, height, width)
    if mousePressed:
        fill(0,0,0,30) #1
        circle(145,200, 80) #1
        circle(260,200,80) #1
        fill(255,204,255,120) #1
        circle(145,200,79) #1
        circle(260,200,79) #1
        fill(0,0,0) #1
        rect(185, 190, 35, 1) #1
        rect(70,190,35,1) #1
        rect(300,190,35,1) #1
    else:
        fill(204,229,255,100) #2
        rect(110,170,70,50) #2
        rect(220,170,70,50) #2
        fill(0,0,0)
        rect(180,190,40,1) #2
        rect(70,190,40,1) #2
        rect(290,190,40,1) #2
    endRecord() # teraz zapisze na końcu pierwszej klatki, więc nie bardzo mamy szansę kliknąć myszą i zapisać wariant pierwszy

# 1,5pkt
