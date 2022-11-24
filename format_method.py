# Format() method for combining the string and integer 
 
a=23
b="kalaiselvam {}"
print(b.format(a))

a=23
c=9345582479
d=80.7200
e="suji"
# using the {} curely prase for accessing the value
b="kalaiselvam {} {} {}"
print((b).format(a,c,d))

a=23
c=9345582479
d=80.7200
e="suji"
# using the index value to accessing the value
b="kalaiselvam {2} {0} {1}"
print((b).format(a,c,d))

#   output
#   kalaiselvam 23
#   kalaiselvam 23 9345582479 80.72
#   kalaiselvam 80.72 23 9345582479
 