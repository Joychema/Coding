
#while loops
#incremental
# num=5

# while num<=15:
#     print(num)
#     num+=1

# num=100

# while num>=0:
#     print(f"loop: {num}")
#     num-=5

i = 20
while i<25:
    print(f"loop: {i}")

    i+=2


#for loop
#a for loop is used for iterating over a sequence, be it a list,set,dictionary,string

#the break statement stops the loop before it can loop through all the items
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for day in days:
    if day == "Wednesday":
        break
print(f"{day}")

#the continue statement stops the current iteration of the loop,
#and continues with the next
nums =["1","2","3","4","5","6","7","8","9"]
for num in nums:
    if num == "3":
        continue
    print(f"{num}")

#range function
for a in range(1, 9, 2):
    print(f"{a}")
else:                   #the else statement prints out a message when the loop has ended
    print(f"The loop has ended.")
