friends = ["edgar", "gago", "carrillo"]

# select the secon name
print(friends[1])

# select a range inside the array (matlab-like) 
# takes from 1 (included) up to 3 - 1
print(friends[1:3])


# select all after a certain index
print(friends[1:])

### more functions

# add a list
friends.extend([3,5,6])
print(friends)

# the push method of python (adds at the end)
friends.append("fsdf")
print(friends)

# insert element at a certaine index
friends.insert(2, "2")
print(friends)

# extract an element of the list
print(friends.pop(4))

# get and id by its elements
print(friends.index("2"))

# counting
print(friends.count("gago"))

## order-like

# not supported for non num types
# friends.sort()
# print(friends)

friends.reverse()
print(friends)

# Copy functionality

friends_copy = friends.copy()
print(friends_copy)