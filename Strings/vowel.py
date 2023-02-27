# Python program to check if string starts with vowel

# take inputs
string = input('Enter the String: ')

# vowel alphabet
vowel = 'aeiou'

# check string starts with vowel or consonant
if string[0].lower() in vowel:
   print(string,'starts with vowel',string[0])
else:
   print(string,'starts with consonant',string[0])