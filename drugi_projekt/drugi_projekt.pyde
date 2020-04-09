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
    # żeby mieć pewność, że kod wywołą się podczas startu programu, trzeba umieścić w setup, po za funkcjami to zła praktyka
    global x, y
    global speedX, speedY # wystarczyło dla każdej osi liczyć oddzielnie, wówczasbędzie zawracać niezależnie, a nie odbijać oba kierunki gdy natrafi na choć jedną ścianę.
    x=0.0
    y=0.0
    speedX=10.0
    speedY=10.0

def draw():
    move()
    display()

def move():
    global x, y, speedX, speedY
    x += speedX
    if x > width or x < 0:
        speedX*=-1
    
    y += speedY
    if y > height or y < 0:
        speedY*=-1
        
def display():
    global iteracja
    iteracja+=10
    rect(x, y, 100, 100)
    fill(*lista[iteracja%len(lista)])
    
#1,5pkt
