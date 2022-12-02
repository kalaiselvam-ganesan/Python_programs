# Lambda() function

# creatinng a list of tuple for sorting
list1=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("original list of tuple:")
print(list1)
# sort() method is used to sort the list of tuple 
list1.sort(key=lambda x:x[1])
print("Sort the list of tuple:")
print(list1)



#   output

"""original list of tuple:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sort the list of tuple:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]"""