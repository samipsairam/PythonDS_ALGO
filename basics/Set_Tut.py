# unordered collection of unique elements
# SET doesnot support indexing
my_set = {1,2,3,4,5,6,1,4}
my_set.add(100)
my_set.add(2)
print(my_set)

print(1 in my_set)
print(len(my_set))
print(list(my_set))
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)

my_list = [1,2,3,4,5,5]
my_new_list = list(set(my_list))
print(my_new_list)
print(type(my_new_list))

# METHODS in Sets
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
small_set = {6,7}
print(my_set.union(your_set))    # print(my_set | your_set) same as above
print(my_set.issubset((my_set | your_set)))
print(your_set.issuperset(small_set))
print(my_set.intersection(your_set))
print(my_set.isdisjoint(your_set))    # Checks if two sets have any elements common in them
print(my_set.difference(your_set))
print(my_set.difference_update(your_set))  # modifies my_set
print(my_set) # just takes difference from the view of my_set
print(my_set.discard(5))
print(my_set)