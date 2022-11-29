# Set

# add two set using update() method
thisset={"kalai","selvam",23.0,45}
thisset1={"muilty","starbucks","chormo","cinepolis"}
thisset.update(thisset1)
print(thisset)

# set can used to add with list,tuple,dict...etc
thisset={"kalai","selvam",23.0,45}
thislist=["kalai","bat","ball","stump"]
thisset.update(thislist)
print(thisset)

# Remove() method is used to remove item in set
# suppose the given item not in set means it will raise a error
thisset={"kalai","selvam",23.0,45}
thisset.remove("selvam")
print(thisset)

# discard() method is used to remove item in set
# suppose the given item not in the set means it will not raise error
thisset={"kalai","selvam",23.0,45}
thisset.discard("23")
print(thisset)


#   output

#   {'selvam', 'starbucks', 'kalai', 'cinepolis', 45, 'muilty', 23.0, 'chormo'}
#   {'selvam', 'stump', 'kalai', 45, 'bat', 23.0, 'ball'}
#   {'kalai', 45, 23.0}
#   {'selvam', 'kalai', 45, 23.0}
