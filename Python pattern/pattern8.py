# To print the following pattern
# 0 
# 1 2 
# 3 4 5 
# 6 7 8 9 

#To input number of rows
rows=int(input("Enter number of rows:"))
b = 0

#outer loop to handle rows
for i in range(rows):
    
    #inner loop
    for j in range(1, i + 1):
        print(b, end=" ")
        b=b+1
        
    print("\r")