#list datastructures, it is also mutable(changes)
#list is indexed
# trees=["pine", "cedar", "cove"]
# trees[0]="cypress"
# trees.remove(trees[0]) #to remove an item from a list
# trees[1]="Cactus"  #to change an item in the list
# trees.append("oak") #used to add an item to a list
# trees.insert(0, "Coconut")
# print(trees)
# print(f"I planted {trees[0]} in our backyard")

# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
#tuple is indexed
# color=("red", "yellow", "orange")

# print(color[-1])
# print(f"A banana is {color[1]} in colour")

#set is unordered, unchangeable, un-indexed, non-duplicate
shapes={"circle", "triangle", "oval","pentagon", "square"}
print(shapes)

if "triangle" in shapes:
    print("Triangle")

#dictionaries
data={"name: Joy", "age: 21", "course: Engineering"}

print(data)
# print(f"She is {data["age"]} years old")
