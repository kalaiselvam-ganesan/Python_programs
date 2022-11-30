# Dictionaries

# Accessing the dictionaries using key 
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
print(thisdict["age"])

# get() method also used to access the dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
x=thisdict.get("name")
print(x)

# keys() method used to return all the keys present in the dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
x=thisdict.keys()
print(x)

# keys() method used to return all the keys present in the dictionarie
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
x=thisdict.keys()
print(x)
thisdict["colour"]="black"
print(x)


#   output

#   22

#   kalai

#   dict_keys(['name', 'age', 'DOB'])

#   dict_keys(['name', 'age', 'DOB'])
#   dict_keys(['name', 'age', 'DOB', 'colour'])
