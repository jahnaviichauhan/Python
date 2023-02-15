#To print the following star pattern
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5 

#To input number of rows
rows=int(input("Enter number of rows:"))
b = 0

#outer loop to handle rows
for i in range(rows, 0, -1):
    b += 1
    #inner loop to print b, i times
    for j in range(1, i + 1):
        print(b, end=" ")

    print("\r")