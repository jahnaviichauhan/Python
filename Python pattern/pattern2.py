#To print the following star pattern
# *  
# * *  
# * * *  
# * * * *  

rows=int(input("Number of rows:"))

#outer loop to handle number of rows
for num in range(rows):
    
    #inner loop to tell how many times star will be printed
    for i in range(num):
        
        #printing stars
        print("*", end=" ") 
    #Changing lines
    print(" ")