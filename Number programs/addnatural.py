#Addition of n natural numbers

print("Enter the number of numbers you want to add")
try:
    n=int(input())
except:
    print("Invalid Input")

sum=0

#loop for n number of elements
for i in range(0,n+1):
    sum=sum+i
        
print("SUM:", sum)