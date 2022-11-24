# Global variables

x = "boy"
def myfunc():
  print("kalai is "+x)
myfunc()

#   output
#   kalai is boy


x = "boy"
def myfunc():
    x="good"
    print("kalai is "+x)
myfunc()
print("kalai is "+x)

#   output
#   kalai is good
#   kalai is boy


x = "boy"
def myfunc():
    global x
    x="good"
    print("kalai is "+x)
myfunc()
print("kalai is "+x)

#   output
#   kalai is good
#   kalai is good