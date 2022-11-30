# Dictionaries

# copy() method is used to copy the one dictionaries to another dictionaries 
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
mydict=thisdict.copy()
print(mydict)

# dict() method also used to copy the one dictionaries to another dictinaries
thisdict={
    "name":"kalai",
    "age":23,
    "DOB":"july 8th"
}
mydict=dict(thisdict)
print(mydict)


#   output

#   {'name': 'kalai', 'age': 22, 'DOB': 'july 8th'}
#   {'name': 'kalai', 'age': 23, 'DOB': 'july 8th'}