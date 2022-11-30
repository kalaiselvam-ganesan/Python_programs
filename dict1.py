# Dictionaries

# createing dictionaries and pinting the values
thisdict={
    "name":"kalai",
    "age":"22",
    "DOB":"july 8th"
}
print(thisdict)

# we can represent the key by accessing the values.
thisdict={
    "name":"kalai",
    "age":"22",
    "DOB":"july 8th"
}
print(thisdict["DOB"])

# dictionaries does not allow duplicate values, 
# suppose it having duplicate values in key means it will be over written the
# existing value.
thisdict={
    "name":"kalai",
    "age":"22",
    "DOB":"july 8th",
    "age":"23"
}
print(thisdict)


#   output

#   {'name': 'kalai', 'age': '22', 'DOB': 'july 8th'}
#   july 8th
#   {'name': 'kalai', 'age': '23', 'DOB': 'july 8th'}
