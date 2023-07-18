import re
string = input("Enter a string: ")
words = re.findall(r'\b\w+\b', string)
print("Extracted words:", words)
