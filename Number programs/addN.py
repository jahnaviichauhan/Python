#Addition of n numbers

print("Enter the number of numbers you want to add")
n=int(input())

sum=0

#loop for number of elements
for i in range(0,n):
    #To prevent input of alphabetic values
    try:
        a=input('enter value')
        a=int(a)
        sum=sum+a
    except:
        print("Invalid Input")
        
print("SUM:", sum)
