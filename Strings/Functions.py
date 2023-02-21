#Performing string functions in python

str1="welcome to upes"
print(len(str1)) #Gives the length of the string 
print(str1[0:18]) #Prints the letters from 1+the first number to the second number

print(str1[0:10:2]) #Prints the string till middle value with difference of third value

print(str1[:7]) #Prints the string till 7th position starting from 1
print(str1[::]) #Prints the entire string
print(str1[::-1]) #Reverses the string
print(type(str1)) #Prints the data type 
print(str1.isalnum()) #Returns true or false if string is alphanumeric(only contains alphabets and numbers) or not
print(str1.isalpha()) #Returns true of false if string is aphabetical(only contains alphabets) or not
print(str1.endswith("es")) #Returns true of false if the string ends with particular string or not
print(str1.count("e")) #Counts number of alphabets; case sensitive
print(str1.capitalize()) #Converts first letter to upper case
print(str1.find("es")) #Gives a number earlier at which these letters are present for the first time
print(str1.lower()) #Prints entire string in lowercase
print(str1.upper()) #Prints entire string in uppercase
print(str1.replace("u", "U")) #Replaces first letter with second letter

#15
#welcome to upes
#wloet
#welcome
#welcome to upes
#sepu ot emoclew
#<class 'str'>
#False
#False
#True
#3
#Welcome to upes
#13
#welcome to upes
#WELCOME TO UPES
#welcome to Upes
