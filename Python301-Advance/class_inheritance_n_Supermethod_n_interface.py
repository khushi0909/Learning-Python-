class Animal:
    fur_color = "Orange"

    def speak(self):
        print("Raawwwwrr")

    def eat(self):
        pass

    def chase(self):
        pass

class Tiger(Animal):
    pass

class HouseCat(Animal):
    def speak(self):
        print("Meow")
tiger = Tiger()
tiger.speak()
cat = HouseCat()
cat.speak()

# Raawwwwrr
# Meow

#^ point to be noted is when both main class and inherited class have same method irst the class called that is inherited class method gets the preference as in Housecat

class Animal:
    fur_color = "Orange"

    def speak(self):
        raise NotImplementedError

    def eat(self):
        pass

    def chase(self):
        pass

class HouseCat(Animal):
    def speak(self):
        print("Meeeeowwww")

cat = HouseCat()
cat.speak()



  #^      ------- CLASS SUPER METHOD ---------

 # ^ now we we write its own method in inherited class that has same name in main class i.e parent class ,preference is given to method of a inherited class and is executed ,but what if we want to execute methods of both parent and inherited class (they have same name) 

#^ In this case we need to bubble up 

class Animal:
    fur_color = "Orange"

    def speak(self):
        raise NotImplementedError

    def eat(self):
        print("I am eating yum yum yum")

    def chase(self, animal="Gazelle"):
        print("I am chasing a", animal)


class HouseCat(Animal):

    def speak(self):
        print("Meeeeowwww")

    def eat(self):
        super().eat()
        print("I am eating salmon")

    def chase(self, animal):
        super().chase(animal)
        print(animal, "was caught")

cat = HouseCat()
cat.chase("mouse")
cat.eat()
#I am chasing a mouse
# mouse was caught
# I am eating yum yum yum
# I am eating salmon