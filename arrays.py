# Arrays are used to store multiple values in one single variable

cars =["GWagon", "BMW", "Toyota"]

cars.append("Honda") #You can use the append() method to add an element to an array.
# cars.pop(1) You can use the pop() method to remove an element from the array.
cars[0] = "Toyota"

print(f"{cars[0]}")
for x in cars:
    print(f"{x}")

