# Remove the value in the list using remove() method
thislist=["apple","suji",'kalai',40.6,True]
thislist.remove("kalai")
print(thislist)

# Remove the value in the list using remove() method with index
thislist=["apple","suji",'kalai',40.6,True]
thislist.remove(thislist[1])
print(thislist)

# Remove the value in the list using remove() method with Negative index
thislist=["apple","suji",'kalai',40.6,True]
thislist.remove(thislist[-2])
print(thislist)

# Pop() Method used to remove the particular value in the list using the index
thislist=["apple","suji",'kalai',40.6,True]
thislist.pop(2)
print(thislist)

# pop() method used to remove the particular value in the list using the index 
# suppose the index will not be mention in the pop it removes the last element in the list value.
thislist=["apple","suji",'kalai',40.6,True]
thislist.pop()
print(thislist)


#   ouput
#   ['apple', 'suji', 40.6, True]
#   ['apple', 'kalai', 40.6, True]
#   ['apple', 'suji', 'kalai', True]
#   ['apple', 'suji', 40.6, True]
#   ['apple', 'suji', 'kalai', 40.6]

