# class and objects

# creating a class using class keyword with the name of person
class person:
    x=10
    y=20
    
    # method definition of sum
    def sum(self):
        # here self variable refers the object p1
        # suppose we going to declare five parameter 
        # means we have to declare six parameter because first parameter is a reference of object.
        print(self.x,self.y)
        print("Sum:",self.x+self.y)
    # method definition of new_method
    def new_method(abc,arg):
        print(arg)

# creating the object with the name of p1
p1=person()
# prining the values
print(p1.x)
print(p1.y)
# call of method using object
p1.sum()
# call of method using new_method
p1.new_method("Hello")



#   output

"""
10
20
10 20
Sum: 30
Hello
"""