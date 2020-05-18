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
    def rusz(self, ruch): #metoda nie powinna się nazywać tak samo jak atrybut
        self.x += ruch
def setup():
    size(400, 400)
    global moja_pilka
    moja_pilka = Pilka(width/2, height/2, 50) #obiekty miały być dwa

def mouseWheel(event): 
    moja_pilka.obroc(5) 
    print(moja_pilka.obrot) 
    
def mousePressed(): # to na co ta akcja będzie się wykonywać to inna  bajka, mamy jakieś fizyczne elementy myszki czy klawiatury, które można fizycznie klikać i do tego są metody natomiast to jak reagują (upuszczenie/drag) trzeba już zaprogramować
    moja_pilka.rusz(5) # tu przesuwamy pozycję x o 5 jednostek w prawo, ale można tu użyć mp. mouseX i wówczas zależnie od intencji będzie reagować bardziej na mysz
    print(moja_pilka.ruch)
   
def draw(): 
    background(120)
    moja_pilka.rysuj()
    
# 1pkt, mało twórcze, dużo mocno inspirowanych moim kodem i widać niedogłębne zrozumienie; to ważny temat, spróbuj jeszcze coś wokół się na niego douczyć jak znajdziesz czas
