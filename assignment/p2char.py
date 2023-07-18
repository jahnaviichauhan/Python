string = input("Enter a string: ")
words = string.split()
for word in words:
    if len(word) >= 2:
        print(word[:2])
    else:
        print(word)
