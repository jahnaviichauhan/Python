#Calculation of simple interest

#Inputting values of principal, rate and time
print("Enter principal value")
p=float(input())
print("Enter rate per annum")
r=float(input())
print("enter time in years")
t=int(input())

#Calculation
SI=(p*r*t)/100.0

print("Simple Interest:", SI)