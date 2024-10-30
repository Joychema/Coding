# A variable is a container used for storing variables.
# A variable is created the moment you first assign a value to it.
"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

myName = "Joy Kosgei"
print(myName)
print("My name is {}".format(myName))

num1 = 27
num2 = 10

print(f"The sum of {num1} and {num2} is {num1 + num2}")

num3 = 19
num4 = 6

print(f"The product of {num3} and {num4} is {num3 * num4}")
print(f"The difference of {num3} and {num4} is {num3 - num4}")

#Concatenation is the process of combining or joining two or more strings,
# text fragments, or variables together into a single string.

# If you want to specify the data type of a variable, this can be done with casting.
# x = str(3)
# y = int(3)
# z = float(3)
# print(x, y, z)

x= 4
y= "Joy Kosgei"

print(type(x))
print(type(y))

# Joy, Ezra, Elly = "Campus", "HighSchool", "Cbc"
# print(Joy)
# print(Ezra)
# print(Elly)

#Unpacking variables
# children = {"joy", "ezra", "ely"}
# x, y, z = children
# print(x)
# print(y)
# print(z)

#global variables

x = "Joy Kosgei"

def myfunction():
    x = "Elly"
    print("My name is " + x )

myfunction()
print("My name is " + x)
