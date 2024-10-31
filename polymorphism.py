#polymorphism

class dog():
    def __init__(self,type,sound):
        self.type = type
        self.sound = sound

    def ani(self):
        return f"{self.type} makes {self.sound} sound"

class cat(dog):
    def ani(self):
        return f"{self.type} makes {self.sound} sound"


Dog = dog("German Shepherd", "woooh")
Cat = cat("Ginger", "meow")
print(Dog.ani())
print(Cat.ani())