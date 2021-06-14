# Lists are mutable unlike strings
li = [1, 2, 3, 5, 6]
lib2 = ['a', 'b', 'c']
li3 = [1, 2.5, 'a', True]  # can consist heterogeneous data types

amazon_cart = ['notebooks', 'sunglasses']

# list slicing
amazon_cart.append('toys')
amazon_cart.append('grapes')

print(amazon_cart)
print(amazon_cart[3])
print(amazon_cart[0:3])   # does not change lists

new_cart = amazon_cart   # address remains same
print(id(new_cart), id(amazon_cart) )

new_cart[0] = 'gum'
print(amazon_cart)

# copying list without modificaiton
other_cart = amazon_cart[:]
print(id(other_cart), id(amazon_cart))
print(other_cart)

# Matrix
matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9]
]

print(matrix[0][1])

# LIST METHODS
basket = [1, 2, 3, 4, 5, 6]
print(len(basket))

new_list = basket.append(100)  # append method to add element in list
print(basket)   # returns None as it just appends and produces nothing
print(new_list)
# to show result best way is to append and re-assign list
basket.append(500)
n_list = basket
print(n_list)

# insert method to certain location
basket.insert(4, 50)
print(basket)

# extend takes iterable
new_list = basket.extend([1000,2000])
print(basket)
print(new_list)

# removing items
basket.pop()
print(basket)
basket.pop(0)
print(basket)

basket.remove(50)
print(basket)

# clear
basket.clear()
print(basket)

# index method
basket = ['a', 'b', 'c', 'd', 'e', 'a']
print(basket.index('d', 0 , 4))

# looking for items in list
print('a' in basket)
print('k' in basket)
print('i' in "My name is Gopal")
print(basket.count('a'))

# sort method modifies list by sorting element
print(basket.sort())
basket.sort()
print(basket)

# sorted method only sorts but doesnot modify list which produces new array
# sorted(basket) is like: new_basket =  basket.sort
print(sorted(basket))

basket.reverse()
print(basket)

# sorted reverse list
bucket = ['fox', 'apple', 'zillo', 'fork']
bucket.sort()
bucket.reverse()
sorted_reversed_basket = bucket
print(sorted_reversed_basket)
print(len(bucket))

# reverse the list
print(bucket)
print(bucket[::-1])     # list slicing creates a new list

# range
l1 = list(range(1,100))  # starts from 1 to 99
print(l1)

# .join() method in string
# emptystring.join([Iterable])
sentence = "!"
new_sentence = sentence.join(['This', 'is', 'journey', 'towards', 'production'])
print(sentence)
print(new_sentence)

# shorthand for .join()
naya_sent = ' @ '.join(['Welcome', 'to', 'coding', 'club'])
print(naya_sent)


# LIST UNPACKING
l1 = [1, 'a', True]
a, b, c = l1
print(a)
print(b)
print(c)

l2 = [1,2,3,'a','b','c',False, True, False, 10, 20.4]
x, y, z, *extra = l2
print(x, y, z)
print(extra)

a1, a2, a3, *other = l2[0:3], l2[3:6], l2[6:9], l2[9:]
print(a1)
print(a2)
print(a3)
print(other)