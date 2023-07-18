import re
string = input("Enter a string: ")
characters = re.findall(".", string)
print("Extracted characters:", characters)
