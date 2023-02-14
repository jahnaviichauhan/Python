#To print number pattern as
# 1
# 2 2
# 3 3 3
# 4 4 4 4

#Takes input of number of rows the user wants
rows=int(input("Number of rows:"))

#outer loop to handle number of rows
for num in range(rows):
  
    #inner loop to handle number of times num is printed
    for i in range(num):
        #Printing the number num
        print(num, end=" ") 
     
    #Changing to the next line
    print(" ")
