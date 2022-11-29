# Set

# set is created and it is unordered
thisset={"kalai","selvam",23.0,45}
print(thisset)

# accessing the set using for loop 
thisset={"kalai","selvam","ball","bat"}
for i in thisset:
    print(i)

# accessing the set using in keyword
thisset={"kalai","selvam","ball","stump","ball"}
print("ball" in thisset)

# set is created and it is unordered
# while adding the item in set if the item is exist it will skip the duplicate items and print the output
thisset={"kalai","selvam",23.0,45}
thisset.add("kalai")
print(thisset)

# Add() method is used to add item in the set if the item is exsit it will skip and if the item doesn't exist it will added in the set 
thisset={"kalai","selvam",23.0,45}
thisset.add("bat")
print(thisset)


#   output

#   'selvam', 45, 'kalai', 23.0}

#   bat
#   ball
#   selvam
#   kalai

#   True

#   {'selvam', 45, 'kalai', 23.0}

#   {'kalai', 45, 23.0, 'bat', 'selvam'}