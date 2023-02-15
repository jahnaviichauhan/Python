# To print the following pattern
# 5 5 5 5 5 
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5 

#To input number of rows
rows=int(input("Enter number of rows:"))
b = 5

#outer loop to handle rows
for i in range(rows, 0, -1):
    #inner loop to print 5 from 1 to i times
    for j in range(1, i + 1):
        print(b, end=" ")

    print("\r")
