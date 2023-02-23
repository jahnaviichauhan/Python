# Write a program to accept percentage and display the category 

#Taking input
per=float(input("Enter percentage: "))

#Displaying category according to percentage
if per<40:
    print("Failed")
elif per>=40 and per<55:
    print("Fair")
elif per>=55 and per<65:
    print("Good")
else:
    print("Excellent")