# tuple

# tuple can be created using square brackets
thistuple=("apple",20,'kalai',40.6)
print(thistuple)

# allow dupllicate values in tuple
thistuple=("apple",20,'kalai',40.6,"kalai")
print(thistuple)

#length of the tuple using len() function
thistuple=("apple",20,'kalai',40.6)
print(len(thistuple))

# containing all datatypes like integer,string,boolean,float
thistuple=("apple",20,'kalai',40.6,True)
print(thistuple)

# checking the class type using type() function 
thislist=("apple",20,'kalai',40.6,True)
print(type(thislist))


#   output
#   ('apple', 20, 'kalai', 40.6)
#   ('apple', 20, 'kalai', 40.6, 'kalai')
#   4
#   ('apple', 20, 'kalai', 40.6, True)
#   <class 'tuple'>