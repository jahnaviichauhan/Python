# To print the following pattern
#    1
#   12
#  123
# 1234
#12345

#To input number of rows
row = int(input("Enter number of rows:"))

#outer loop to handle rows
for i in range(row):
    
    #inner loop 
    for j in range(1, row - i):
        print(" ", end="")
    for k in range(1, i + 2):
        print(k, end='')
    print()