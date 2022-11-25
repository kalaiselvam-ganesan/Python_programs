#list

# Accessing the list using index value start from 0,1,2..etc
thislist=["apple",20,'kalai',40.6,True]
print(thislist[0],thislist[1])

# Negative indexing in the list value
thislist=["apple",20,'kalai',40.6,True]
print(thislist[-2],thislist[-1])

# Range can be used to access the list value
thislist=["apple",20,'kalai',40.6,True]
print(thislist[2:4])

# Range can be used to access the list value
thislist=["apple",20,'kalai',40.6,True]
print(thislist[:5])

# Range can be used to access the list value
thislist=["apple",20,'kalai',40.6,True]
print(thislist[1:])

#Negative indexing can be used to access the list value from -1,-2...etc
thislist=["apple",20,'kalai',40.6,True]
print(thislist[-3:-1])

#Negative indexing can be used to access the list value from -1,-2...etc
thislist=["apple",20,'kalai',40.6,True]
print(thislist[:-1])

#Negative indexing can be used to access the list value from -1,-2...etc
thislist=["apple",20,'kalai',40.6,True]
print(thislist[-3:])


#   output
#   apple 20
#   40.6 True
#   ['kalai', 40.6]
#   ['apple', 20, 'kalai', 40.6, True]
#   [20, 'kalai', 40.6, True]
#   ['kalai', 40.6]
#   ['apple', 20, 'kalai', 40.6]
#   ['kalai', 40.6, True]
