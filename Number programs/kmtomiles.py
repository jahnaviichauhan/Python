#Program to convert kilometres to miles and vice-versa

#Choice to check what conversion is to be made
print("Enter choice")
print("1.Kilometres to miles")
print("2.Miles to kilometres")
ch=int(input())

if(ch==1):
    print("Enter kilometres")
    n=float(input())
    ans= n * 0.62137119
    print("{0} kilometres is {1} miles". format(n,ans))

elif(ch==2):
    print("Enter miles")
    n=float(input())
    ans=  n/0.62137119
    print("{0} miles is {1} kilometres". format(n,ans))
    
#Printing invalid input is choice is not 1 or 2.
else:
    print("Invalid Input")