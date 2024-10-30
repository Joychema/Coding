class Person:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname

    def printname(self):
        print(f"Hello my name is {self.first_name} {self.last_name}")

p1= Person(fname="Margret", lname="Njoki")
p1.printname()

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduation_year= year

    def welcome(self):
        print(f"Welcome {self.first_name} {self.last_name}, to the graduation of the class of {self.graduation_year}")

s1= Student(fname="Mary", lname="Njoki", year=1999)
s1.welcome()

#Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
#parent class
class Vehicle:
    def __init__(self, brand ,model):
        self.brand = brand
        self.name=model

    def move(self):
        print(f"Many variety of vehicles!")

class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand,model)

    def move(self):
        print(f"Drive!")

class Plane(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand,model)

    def move(self):
        print(f"Fly!")

class Boat(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand,model)

    def move(self):
        print(f"Sail!")

veh1 = Vehicle(f"All types", "All")
car1 = Car(f"Mercedes", "Toyota")
plane1 = Plane(f"KQ254", "Kenya Airways")
boat1 = Boat(f"Cruise", "SeaWaves")

for x in (veh1, car1, plane1, boat1):
    x.move()