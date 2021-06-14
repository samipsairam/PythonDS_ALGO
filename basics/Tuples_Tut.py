# Tuple are list but are IMMUTABLE
# cannot be reversed and changed is not resizable
my_tuple = (1,2,3,4,5)
print(5 in my_tuple)

new_tuple = my_tuple[1:4]
print(new_tuple)
x,y,z, *other = my_tuple
print(x)
print(y)
print(z)
print(other)
my_tuple = (1,2,3,4,5,6,5,7,4,5,6,5)
print(my_tuple.count(5))
print(len(my_tuple))
