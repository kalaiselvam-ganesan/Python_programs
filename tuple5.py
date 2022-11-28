# Tuple

# tuple has been created.
thistuple=("apple",20,'kalai',40.6,True)
print(thistuple)

# We can add tuple to tuple. 
# For that create two tuple and add with it.
thistuple=("apple",20,'kalai',40.6,True)
tuple1=("ball","stump")
thistuple+=tuple1
print(thistuple)

# we can remove the tuple value using list covertion 
thistuple=("apple",20,'kalai',40.6,True)
list1=list(thistuple)
list1.remove("apple")
thistuple=tuple(list1)
print(thistuple)

# we can remove the tuple value using list covertion 
thistuple=("apple",20,'kalai',40.6,True)
list1=list(thistuple)
list1.remove(list1[1])
thistuple=tuple(list1)
print(thistuple)

#   output
#   ('apple', 20, 'kalai', 40.6, True)
#   ('apple', 20, 'kalai', 40.6, True, 'ball', 'stump')
#   (20, 'kalai', 40.6, True)
#   ('apple', 'kalai', 40.6, True)