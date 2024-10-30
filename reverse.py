# The slicing method (s[::-1]) is the most concise and efficient way to reverse a string.
# The reversed() function is easy to use and maintains readability.
# Looping & List comprehension provides more control over the reversal process.

txt = "Hello World" [::-1]
print(txt)

def my_func(x):
    return x [::-1]

my_text = my_func("Today is on Wednesday")
print(my_text)

def rev(k):
    return k[::-1]
tdy= rev("Reversed")
print(tdy)