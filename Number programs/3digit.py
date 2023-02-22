#Program to check if number entered is a three digit number

#Inputting a number
n=int(input("Enter number"))

#Checking for three digit number
if n>=100 and n<=999:
    print("Number is three digit number")
else:
    print("Number is not a three digit number")