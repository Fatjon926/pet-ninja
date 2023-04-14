class Ninja:
    def __init__( self,first_name , last_name , treats , pet_food , petName, petType, petSkills, nois ):
        self.first_name=first_name
        self.last_name=last_name
        self.treats=treats
        self.pet_food=pet_food
        self.pet=Pet(petName, petType, petSkills, nois)

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Oh no!!! you need more pet food!")
        return self

    def bathe(self):
        self.pet.noise()
        return self

class Pet:
    def __init__(self,name,type,tricks, nois):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=100
        self.energy=50
        self.nois=nois 

    def sleep(self):
        self.energy+=25
        return self

    def eat(self):
        self.energy+=5
        self.health+=10
        return self

    def play(self):
        self.health+=5
        self.energy -= 15 
        return self
    

    def noise(self):
        print(self.noise)

ninja1=Ninja("bubi","kacurrel",['Snausage','Bacon',"Trash Bag"],['Pizza','Burger'], 'Lesi','qen', ['trick 1', 'trick 2'], 'ham ham')


ninja1.feed()
ninja1.feed()
ninja1.feed()




        	
    
