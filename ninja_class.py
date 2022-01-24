
from pet_class import Dog



class Ninja:
        
    def __init__(self, first_name, last_name, treats, pet_food, pet):
            self.first_name = first_name
            self.last_name = last_name
            self.treats = treats 
            self.pet_food = pet_food
            self.pet = pet

    def walk(self):
        print(f'{self.first_name} takes {self.pet.name} out for a walk.')
        self.pet.play()
        return self

    def feed(self):
        print(f'{self.first_name} feeds {self.pet.name} {self.treats} and {self.pet_food}.')
        self.pet.eat()
        return self

    def bathe(self):
        print(f'{self.first_name} gives {self.pet.name} a bathe! scrubba dub dub')
        self.pet.noise()
        


riko = Dog('Riko', 'Dog', 'Rolls Over')
jackson = Ninja('Jackson', 'Murphey', 'kibbles', 'Pup-Chow', riko)
trixy = Dog('Trixy', 'Dog', 'Skateboarding')
marco = Ninja('Marco','Madrid','hot dogs','meat from a can', trixy )



jackson.walk()
jackson.feed()
jackson.bathe()
print(trixy.energy)
print(trixy.health)
marco.walk()
print(trixy.energy)
print(trixy.health)
marco.bathe()

fave_color = input('What is your favorite color? ')
print(f'Your favorite color is: {fave_color}')
