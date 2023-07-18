def get_first_word(string):
    words = string.split()
    if len(words) > 0:
        return words[0]
    else:
        return None
string = input("Enter a string: ")
first_word = get_first_word(string)
print("First word:", first_word)
