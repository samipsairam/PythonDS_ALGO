x = "Hi hello there 24!"
print(type(x))
print(dir(x))

username = "supercoder"
password = "supersecret"
long_string = """
WOW
O O 
---
"""
print(long_string)

first_name = "Samip"
last_name = "Pandey"

# string concatenation
full_name = first_name + " " + last_name
print(first_name + " " + last_name)

# Type Conversion
print(type(int(str(100))))

# Escape Sequence
weather = "It\'s \"kind of\" sunny!"
print(weather)

# Formatted strings
name = "Johnny"
age = 55
# dynamic pass
print(f"hi {name}. You are {age} years old")
print("hi {0}. You are {1} years old".format(name, age))


# string indexes
selfish = 'me me me'
print(selfish[7])
print(selfish)

# [start:stop:stepover] SLICING
print(selfish[0:8:1])
print(selfish[1:])
print(selfish[::-1])

# IMMUTABILITY
greet = "hello mr. hor are you"
print(greet[0:len(greet)])

quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.partition(" "))
print(quote.find("be"))
print(quote.split(" "))
print(type(quote.split(" ")))
print(quote.replace("be","been",1))
