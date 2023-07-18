def count_character(string, character, start_position=0):
    count = 0
    for index in range(start_position, len(string)):
        if string[index] == character:
            count += 1
    return count
string = input("Enter a string: ")
character = input("Enter a character: ")
start_position = int(input("Enter the starting position: "))
result = count_character(string, character, start_position)
print("The count of", character, "in the string is:", result)
