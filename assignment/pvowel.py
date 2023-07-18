string = input("Enter a string: ")
words = string.split()
for word in words:
    if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        print(word)
