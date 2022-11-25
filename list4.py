# Insert the value in the list without replaceing the existing value
thislist=["apple","suji",'kalai',40.6,True]
thislist.insert(2,"cricket")
print(thislist)

# Insert the value in the list without replaceing the existing value using Negative index value
thislist=["apple","suji",'kalai',40.6,True]
thislist.insert(-2,"cricket")
print(thislist)

# Append() function used to append the value in the list at last
thislist=["apple","suji",'kalai',40.6,True]
thislist.append("orange")
print(thislist)

# Extend() method is used extend the list value and it will be added at the end of the list value 
thislist=["apple","suji",'kalai',40.6,True]
tropical=["stump","ball","bat"]
thislist.extend(tropical)
print(thislist)

# Extend() Method does not habve the append() method. so we can use the tuple,set,dict etc to extend the list 
thislist=["apple","suji",'kalai',40.6,True]
tropical=("stump","ball","bat")
thislist.extend(tropical)
print(thislist)



#   output
#   ['apple', 'suji', 'cricket', 'kalai', 40.6, True]
#   ['apple', 'suji', 'kalai', 'cricket', 40.6, True]
#   ['apple', 'suji', 'kalai', 40.6, True, 'orange']
#   ['apple', 'suji', 'kalai', 40.6, True, 'stump', 'ball', 'bat']
#   ['apple', 'suji', 'kalai', 40.6, True, 'stump', 'ball', 'bat']
    