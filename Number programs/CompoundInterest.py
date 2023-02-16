def compoundinterest(principal, rate, time):
 
    # Calculates compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)
 
 
print("Enter principal")
p=int(input())
print("Enter rate")
r=float(input())
print("Enter time")
t=int(input())
#Calling of function to calculate compound interest
compoundinterest(p, r, t)