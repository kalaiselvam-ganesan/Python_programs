# Set

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
set1={"ball","bat","stump","keeper"}
set2={"volleyball","tabletennis","kabbadi","kho-kho","stump"}
set1.symmetric_difference_update(set2)
print(set1)

# The symmetric_difference() method will return a new set, 
# that contains only the elements that are NOT present in both sets
set1={"ball","bat","stump","keeper"}
set2={"volleyball","tabletennis","kabbadi","kho-kho","stump"}
set3=set1.symmetric_difference(set2)
print(set3)

# difference() methode used to print a first set which is not common to both set
set1={"ball","bat","stump","keeper"}
set2={"volleyball","tabletennis","kabbadi","kho-kho","stump"}
set3=set1.difference(set2)
print(set3)

# isdisjoint() method used to check whether the two sets having same item are not.
set1={"ball","bat","stump","keeper"}
set2={"volleyball","tabletennis","kabbadi","kho-kho","stump"}
set3=set1.isdisjoint(set2)
print(set3)


#   output

#   {'tabletennis', 'keeper', 'bat', 'kabbadi', 'ball', 'volleyball', 'kho-kho'}
#   {'keeper', 'bat', 'tabletennis', 'volleyball', 'kabbadi', 'kho-kho', 'ball'}
#   {'keeper', 'bat', 'ball'}
#   False