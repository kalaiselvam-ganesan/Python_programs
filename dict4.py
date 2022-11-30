# Dictionaries

# values() method is used to return all values present in the dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
x=thisdict.values()
print(x)

# values() method is used to return all values present in the dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
x=thisdict.values()
print(x)
thisdict["colour"]="black"
print(x)

# items() method is used to return all items in the dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
x=thisdict.items()
print(x)

# items() method is used to return all items in the dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
x=thisdict.items()
print(x)
thisdict["colour"]="black"
print(x)


#   output

#   dict_values(['kalai', 22, 'july 8th'])

#   dict_values(['kalai', 22, 'july 8th'])
#   dict_values(['kalai', 22, 'july 8th', 'black'])

#   dict_items([('name', 'kalai'), ('age', 22), ('DOB', 'july 8th')])

#   dict_items([('name', 'kalai'), ('age', 22), ('DOB', 'july 8th')])
#   dict_items([('name', 'kalai'), ('age', 22), ('DOB', 'july 8th'), ('colour', 'black')])
