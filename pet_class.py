

class Pet:

    def __init__(self, name, type, tricks, health=100, energy=100):
        self.name = name 
        self.type = type    
        self.tricks = tricks
        self.health = health
        self.energy = energy 
    

    def sleep(self):
        self.energy += 25       #100 + 25
        return self

    def eat(self):
        self.energy += 5        #125 + 5
        self.health += 10       #100 + 10
        return self

    def play(self):
        self.energy -= 20       #130 - 20
        self.health += 5        #110 + 5
        return self

    def noise(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    
# myAnimal = Pet("Tugg", "Snake", "Slither")
# print(myAnimal.energy)
# print(myAnimal.health)
# myAnimal.play().eat().sleep()
# print(myAnimal.energy)
# print(myAnimal.health)

class Dog(Pet):

    def sleep(self):
        self.energy += 25
        print(f"{self.name} decides to take a nap...+25 energy!" )
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} eats some food! +5 to energy, +10 to health!")
        return self

    def play(self):
        self.energy -= 20
        self.health += 5
        print(f"{self.name} goes outside to play! While playing, {self.name} {self.tricks}")
        print("-20 to energy, +5 to health")
        return self

    def noise(self):
        print("WOOF, WOOF!")
        return self

fido = Dog("Fido", "Dog", "Wags Tail")
# fido.play()
# fido.noise()
# fido.sleep()
# fido.eat()



