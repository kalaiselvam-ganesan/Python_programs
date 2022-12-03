# class and objects

# creating a class using class keyword with the name of person
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

# creating the object with the name of p1
p1=person("kalai",23)
# prining the values
print(p1.name)
print(p1.age)


#   output

# kalai
# 23