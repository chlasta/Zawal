value=0
class Pilka(): 
    def __init__(self, arg_x, arg_y, arg_r):
        self.obrot = 0
        self.ruch=0
        self.x = arg_x 
        self.y = arg_y 
        self.r = arg_r 
    def rysuj(self):
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+45), PI+ radians(self.obrot+45), PIE)
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+90), PI+ radians(self.obrot+90), PIE) 
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+135), PI+ radians(self.obrot+135), PIE)
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+180), PI+ radians(self.obrot+180), PIE)
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+225), PI+ radians(self.obrot+225), PIE)
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+270), PI+ radians(self.obrot+270), PIE) 
    def obroc(self, stopnie): 
        self.obrot += stopnie
    def ruch(self, ):
        self.poruszone += 
def setup():
    size(400, 400)
    global moja_pilka
    moja_pilka = Pilka(width/2, height/2, 50) 

def mouseWheel(event): 
    moja_pilka.obroc(5) 
    print(moja_pilka.obrot) 
    
def mouseDragged(): 
    moja_piłka.ruch(5)
    print(moja_pilka.poruszona)
    
def draw(): 
    background(120)
    moja_pilka.rysuj() 
