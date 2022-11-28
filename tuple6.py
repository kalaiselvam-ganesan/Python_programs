# Tuple

# count() method is used to count a spicified value int he tuple
thistuple=("kalai",20,30,"kalai",45.0)
x=thistuple.count("kalai")
print(x)

# both are same but in this we accessing with index to count the tuple
thistuple=("kalai",20,30,"kalai",45.0)
x=thistuple.count(thistuple[0])
print(x)


# index() method is used to search the first occurance of number 
# and it will give the result the occurance of index value  in tuple
thistuple=(1,2,3,4,5,6,7,8,9)
x=thistuple.index(3)
print(x)

# Tuple

# adding the tuples each other it is called concatination
thistuple=("kalai","suji",20)
tuple1=("ball","stump",2000)
thistuple+=tuple1
print(thistuple)

# We can multiply the tuple
thistuple=("kalai","selvam","spa-crust")
x=thistuple*2
print(x)


#   output
#   2
#   2
#   2
#   ('kalai', 'suji', 20, 'ball', 'stump', 2000)
#   ('kalai', 'selvam', 'spa-crust', 'kalai', 'selvam', 'spa-crust')