from abc import ABCMeta, abstractmethod
class Pet():
    __metaclass__=ABCMeta 
    @abstractmethod
    def speak(self): 
        super().__init__()
        return 'no sound'
class Bunny(Pet): # program sporo traci na usunięciu pozostałych zwierząt
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('tuptup', random(400,400), random(400,400))    
    def comehere(self):
        image(loadImage("indeks.jpg"), random(50, width-70), random(50, height-100))
    def __add__(self, other): # miało być odejmowanie
        return self.name[0]+ ' i ' + other.name[0]

def setup():
    size(800,800)
    textSize(20)
    tuptus = Bunny('Tuptus') 
    global list_of_pets
    list_of_pets = [tuptus]
    print(isinstance(tuptus, Pet)) 

def draw():
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak() 
        if isinstance(pet, Bunny):
            pet.comehere()
 
# 1pkt       
