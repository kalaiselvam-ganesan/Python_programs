# Tuple

# One item tuple can be created using comma
thistuple=("kalai",)
print(type(thistuple))

# In tuple it is a string type
thistuple=("kalai")
print(type(thistuple))


# For changing purpose
# If you wante to change the tuple values, then change the tuple into list 
#and make changes of value [or] modify the value (or) items 
#and at last convert back to tuple. 
thistuple=("apple",20,'kalai',40.6,True)
list1=list(thistuple)
list1[1]=50
thistuple=tuple(list1)
print(thistuple)


#   output
#   <class 'tuple'>
#   <class 'str'>
#   ('apple', 50, 'kalai', 40.6, True)
