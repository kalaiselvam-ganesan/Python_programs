# List

# changing the list values using the index values
thislist=["apple",20,'kalai',40.6,True]
thislist[1]=["selvam"]
print(thislist)

# changing the list values using the index values
thislist=["apple",20,'kalai',40.6,True]
thislist[1],thislist[2]=["selvam","suji"]
print(thislist)

# changing the list values using the range values
thislist=["apple",20,'kalai',40.6,True]
thislist[1:3]="cricket","ball"
print(thislist)

# changing the list values using the range values
thislist=["apple",20,'kalai',40.6,True]
thislist[1:2]="cricket","ball"
print(thislist)

# changing the list values using the range values
thislist=["apple","suji",'kalai',40.6,True]
thislist[1:3]=["cricket"]
print(thislist)

# Negative indexing can be used to changing the list values  
thislist=["apple","suji",'kalai',40.6,True]
thislist[-3:-1]=["cricket"]
print(thislist)


#   output
#   ['apple', ['selvam'], 'kalai', 40.6, True]
#   ['apple', 'selvam', 'suji', 40.6, True]
#   ['apple', 'cricket', 'ball', 40.6, True]
#   ['apple', 'cricket', 'ball', 'kalai', 40.6, True]
#   ['apple', 'cricket', 40.6, True]
#   ['apple', 'suji', 'cricket', True]