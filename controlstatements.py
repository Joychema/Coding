num=int(input("Enter a number: "))

if num%2==0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")


#a program that checks whether someone is permitted to vote or not based on their age
age=int(input("Enter your age: "))

if age<18:
    print("You are not permitted to vote")
else:
    print("You are permitted to vote")

#create a program that grades students from A to F

grade=int(input("Enter your grade: "))

if grade<=100 and grade>=80:
    print("You have an A")
elif grade<=79 and grade>=60:
    print("You have a B")
elif grade<=40 and grade>=29:
    print("You have a C")
elif grade<=10 and grade>=19:
    print("You have a D")
else:
    print("Invalid input")


#the NOT logical operator
a=12
b=90
if not a > b:
    print(f"{a} is greater than {b}")

#Nested if
p = 56
if p > 10:
    print(f"{p} is greater than 10")
    if p > 20:
        print(f"{p} is also greater than 20")
    else:
        print(f"{p}not above 20")



