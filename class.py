# A Class is like an object constructor, or a "blueprint" for creating objects.

# class MyClass:
#     x=5

# p1 = MyClass()
# print(p1.x)

class Person:
    def __init__(self, name, age):   # The __init__() function is called automatically
                                    # every time the class is being used to create a new object.
        self.name = name
        self.age = age

    # def __str__(self):
    #         return f"{self.name}({self.age})"
    # def myfunc(self):
    #     pass


# p1 = Person("John", 35)
# print(p1)

#Object Methods
# Methods in objects are functions that belong to the object.
# All method def statements should start  at the same indentation level as __init__
# otherwise they are not part of the class.

    def myfunc(self):
        print("Hello,my name is " + self.name)

p1 = Person("John", 35)
p1.myfunc()