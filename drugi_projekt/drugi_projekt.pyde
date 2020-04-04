x=0.0
y=200.0
speed=10.0
      

def setup():
    size(600,800)
    frameRate(5)
    global slownik
    global iteracja
    iteracja = 0

    slownik={'czerwony':(153,0,0), 'niebieski':(0,51,153),'zielony':(0,102,0)}
    global lista
    lista= []
    for klucz,wartosc in slownik.items():
        lista.append(wartosc)

def draw():
    move()
    display()

def move():
    global x
    global y
    global speed
    x = x + speed
    if x > width:
        speed=speed*-1
    if x < 0:
        speed=speed*-1
    
    y = y + speed
    if y > height:
        speed=speed*-1
    if y < 0:
        speed=speed*-1
def display():
    global iteracja
    iteracja+=10
    rect(x, y, 100, 100)
    fill(*lista[iteracja%len(lista)])
