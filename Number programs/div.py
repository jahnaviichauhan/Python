#Division of two numbers

#input of first and second number and type casting them
print("Enter first number")
n1=int(input())
print("Enter second number")
n2=int(input())

#calculating answer      
if(n1>n2):
    ans=float(n1/n2)
else:
    ans=float(n2/n1)

#Printing of value 
print("Division:", ans)
