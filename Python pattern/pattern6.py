# To print the following pattern
# 0 
# 0 0 
# 0 0 0 
# 0 0 0 0 

#To input number of rows
rows=int(input("Enter number of rows:"))
b = 0

#outer loop to handle rows
for i in range(rows):
    
    #inner loop to print 0,i times
    for j in range(1, i + 1):
        print(b, end=" ")
        
    print("\r")