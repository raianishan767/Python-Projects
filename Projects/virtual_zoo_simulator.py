class animals():
    def __init__(self,name):
        self.name=name

class lion(animals):

    def speak(self):
        return "Roar!"
    
    def species(self):
        return "LION"
    
class elephant(animals):
    
    def speak(self):
        return "Trumpet"
    
    def species(self):
        return "ELEPHANT"   
    
class penguin(animals):

    def speak(self):
        return "Honk!"
    
    def species(self):
        return "PENGUIN"

class zoo():
    def __init__(self,name):
        self.name=name
        self.animals=[]
    
    def addZoo(self,animal):

        self.animals.append(animal)
        print(f"{animal.name} the {animal.species()} added to the {self.name} Zoo.")

    def showAnimal(self):
        print(f"Welcome to the {self.name} zoo.Here ar the animals and their speaking nature:")

        for a in self.animals:
            print(f"{a.species()} speaks {a.speak()}")


my_zoo = zoo("Happy Valley")

my_zoo.addZoo(lion("Simba"))
my_zoo.addZoo(elephant("Dumbo"))
my_zoo.addZoo(penguin("Pingu"))
my_zoo.showAnimal()