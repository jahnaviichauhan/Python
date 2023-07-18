import random
code = str(random.randint(1000, 9999))
max_tries = 10
for _ in range(max_tries):
    # Input the guessed code from the user
    guess = input("Enter your four-digit guess: ")
    result = ""
    for i in range(4):
        if guess[i] == code[i]:
            result += "R"
        elif guess[i] in code:
            result += "Y"
        else:
            result += "B"
    print("Output:", result)
    if guess == code:
        print("Congratulations! You guessed the code correctly!")
        break
else:
    print("Game Over! You ran out of tries. The correct code was:", code)
