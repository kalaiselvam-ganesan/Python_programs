# Ex_4

# Declaring previous number as 0
p_no=0
print("Previous Number:",p_no)
# Checking the for loop 
for i in range(1,11):
    sum=p_no+i
    # Printing the cuurent number & previous number & sum values
    print("Current_Number", i, "Previous Number ", p_no, " Sum: ",sum)
    # Setting the previous number as i to sum the value
    p_no=i



#   output

"""
Previous Number: 0
Current_Number 1 Previous Number  0  Sum:  1
Current_Number 2 Previous Number  1  Sum:  3
Current_Number 3 Previous Number  2  Sum:  5
Current_Number 4 Previous Number  3  Sum:  7
Current_Number 5 Previous Number  4  Sum:  9
Current_Number 6 Previous Number  5  Sum:  11
Current_Number 7 Previous Number  6  Sum:  13
Current_Number 8 Previous Number  7  Sum:  15
Current_Number 9 Previous Number  8  Sum:  17
Current_Number 10 Previous Number  9  Sum:  19
"""