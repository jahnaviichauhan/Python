#Checking whether last digit of a number is divisible by 3

#Inputting a number
n=int(input("Enter number"))

#Finding last digit of number
d=n%10

#Checking if last digit is divisible by 3
if d%3==0:
    print("Last digit {0} is divisible by 3".format(d))
else:
    print("Last digit {0} is not divisible by 3".format(d))