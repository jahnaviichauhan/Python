# To print the following pattern
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

#To input number of rows
rows=int(input("Enter number of rows:"))

#outer loop to handle rows
for i in range(rows, 0, -1):
    
    #inner loop to print numbers 
    for j in range(1, i + 1):
        print(j, end=" ")

    print("\r")