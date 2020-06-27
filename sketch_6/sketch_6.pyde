class Kwadrat(): # nie byłopotrzeby zmieniać tej klasy..
    def __init__(self, bok): 
        self.bok = bok
    def sketch(self, x, y, z, a):
        self.x = x
        self.y = y
        self.z = z
        self.a = a
        rect(self.x, self.y, self.z, self.a) # mało kwadratowy ten kwadrat ;)
            
class KolorowyKwadrat(Kwadrat):
    def sketchKolorowy(self,x,y,z,a,kolor):
        Kwadrat.sketch(self,x,y,z,a)
        for kolor in range (0,kolor):
            fill(200,140,20)
            rect(30,11,78,21)
def setup():
    size(500, 500)
    malyKolorowyKwadrat=KolorowyKwadrat(200.30)
    malyKolorowyKwadrat.sketchKolorowy(29,51,48,21,45)
    
# 1 pkt
