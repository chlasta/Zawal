class BrakPlikuGraficznego(Exception): 
    def __init__(self):
        super(BrakPlikuGraficznego, self).__init__() 
        self.msg='Brak pliku'
    def __str__(self): 
        return self.msg

class Grafika ():
    grafika = ""
    def setGrafika(self, obrazek):
        self.grafika=obrazek
        if image not in self.grafika: 
            raise BrakPlikuGraficznego()

img = loadImage("piesek.jpg")
image(img, 0, 0)

# nie do końca o to chodziło
# nie stosujesz stworzonych klas
# nie zastosowałaś konstrukcji try
# informacja o nie wczytaniu pliku nie jest dostępna dla użytkownika aplikacji w oknie programu
# 0,5pkt
