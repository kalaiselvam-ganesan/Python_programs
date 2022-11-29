# Set

# union() method used to join the two set into a single set
set1={"ball","bat","stump","keeper"}
set2={"volleyball","tabletennis","kabbadi","kho-kho"}
set3=set1.union(set2)
print(set3)

# update() mwthod used to join the two set into a single set
# union() and update() both are same
set1={"ball","bat","stump","keeper"}
set2={"volleyball","tabletennis","kabbadi","kho-kho"}
set1.update(set2)
print(set1)

# intersection_update() method used to keep the common element in the both set
# so output will be stump
# and it will not return new set
set1={"ball","bat","stump","keeper"}
set2={"volleyball","tabletennis","kabbadi","kho-kho","stump"}
set1.intersection_update(set2)
print(set1)

# intersection_update() method used to keep the common element in the both set
# so output will be stump
# and it will return new set
set1={"ball","bat","stump","keeper"}
set2={"volleyball","tabletennis","kabbadi","kho-kho","stump"}
set3=set1.intersection(set2)
print(set3)


#   output

#   {'kho-kho', 'tabletennis', 'bat', 'volleyball', 'keeper', 'stump', 'kabbadi', 'ball'}
#   {'kho-kho', 'tabletennis', 'bat', 'volleyball', 'keeper', 'stump', 'kabbadi', 'ball'}
#   {'stump'}
#   {'stump'}
