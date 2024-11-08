# our Cat Entity
#Constructor creates an instance of a class
import random
class Cat:
    def __init__(self,given_name,given_colour):
        self.name=given_name
        self.colour= given_colour
        self.age=1
        self.energy=50
        self.intelligence=5
        self.weight=5
    
    def train(self):
        print(f"{self.name} is training..")
        self.energy -=5
        self.intelligence +=1

    def sleep(self):
        print(f"{self.name}is sleeping...")
        self.energy +=10
        self.age +=1

    def eat(self):
        print(f"{self.name}is eating...")
        self.weight +=3
        self.energy +=4
        food=input("what fruit apple, banana or orange?")
        if food=="apple":
            self.colour="red"
            print("nooo your cat has gone to Red due to apple consumption")
        elif food=="banana":
            self.color="yellow":
            print("noooo your cat has turned yellow due to banana consumption")
        elif food=="orange":
            self.color="orange"
            print("nooo your cat has turned orange due to banana consumption")
    
    def play(self):
        print(f"{self.name}is playing...")
        chance=int(input("pick a number between 1 and 100")
        correct=random.randrange(1,100)
        if chance==correct:
            self.energy==self.energy-self.energy
            print("nooooo your cat broke its legs and is now unable to play")
        else:
            self.energy -=3
            self.weight -=3

        
    
# An instance of a cat
# An instance is a specific occurence of a class
options=int(input("what would you like to do with the cat? 1.Play,2.Train,3.Sleep,4.Eat,5.print stats"))

