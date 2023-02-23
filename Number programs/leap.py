#Program to find if year is a leap year or not

#Input year
year=int(input("Enter year"))

#If remainder of dividing with 4 is 0 then year is leap year
if year%4==0:
    print("Year {0} is leap year".format(year))
else:
    print("Year {0} is not a leap year".format(year))