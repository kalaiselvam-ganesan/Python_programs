# Tuple

# Accessing the tuple using index value start from 0,1,2..etc
thistuple=("apple",20,'kalai',40.6,True)
print(thistuple[0],thistuple[1],thistuple[2])

# Negative indexing in the tuple value
thistuple=("apple",20,'kalai',40.6,True)
print(thistuple[-2],thistuple[-1])

# Range can be used to access the tuple value
thistuple=("apple",20,'kalai',40.6,True)
print(thistuple[2:4])

# Range can be used to access the tuple value
thistuple=("apple",20,'kalai',40.6,True)
print(thistuple[:5])

# Range can be used to access the tuple value
thistuple=("apple",20,'kalai',40.6,True)
print(thistuple[1:])

#Negative indexing can be used to access the tuple value from -1,-2...etc
thistuple=("apple",20,'kalai',40.6,True)
print(thistuple[-3:-1])

#Negative indexing can be used to access the tuple value from -1,-2...etc
thistuple=("apple",20,'kalai',40.6,True)
print(thistuple[:-1])

#Negative indexing can be used to access the tuple value from -1,-2...etc
thistuple=("apple",20,'kalai',40.6,True)
print(thistuple[-3:])


#   output
#   apple 20 kalai
#   40.6 True
#   ('kalai', 40.6)
#   ('apple', 20, 'kalai', 40.6, True)
#   (20, 'kalai', 40.6, True)
#   ('kalai', 40.6)
#   ('apple', 20, 'kalai', 40.6)
#   ('kalai', 40.6, True)