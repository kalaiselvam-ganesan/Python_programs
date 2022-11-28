# Tuple

# packing a tuple
thistuple=("kalai","suji",20)
print(thistuple)

# unpacking tuple
thistuple("kalai","suji",20)
(name,friend,age)=thistuple
print(name)
print(friend)

# in tuple there is a lot of values but we declared only three variables,  
# so using * asterisk it takes the remaining values in the tuple 
thistuple=("kalai","suji",20,"ball","bat")
(name,friend,*age)=thistuple
print(name)
print(friend)
print(age)

# in tuple there is a lot of values but we declared only three variables,  
# using * asterisk it takes the remaining values in the tuple 
thistuple=("kalai","suji",20,"ball","bat")
(name,*friend,age)=thistuple
print(name)
print(friend)
print(age)

#   outputs:

# 1

#('kalai', 'suji', 20)

# 2 program 

#   kalai
#   suji
#   20

# 3 program

#   kalai
#   suji
#   [20, 'ball', 'bat']

# 4 program

#   kalai
#   ['suji', 20, 'ball']
#   bat