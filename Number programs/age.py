#Checking eligibility to vote 

#Inputting age from user
a=int(input("Enter age: \n"))

#Checking if age is above 18
if a>18:
    print("Eligible to vote")
#If age is below 18
else:
    print("Not eligible to vote\n")
    c=18-a
    #Printing years left to be eligible for voting
    print("{0} years left to be eligible to vote".format(c))