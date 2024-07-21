import random

top_of_range = input("Please type a number for computer to guess from: ")



if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number greater than 0 next time!")
        quit()

else:
    print("Please type a number greater than 0 next time!")
    quit()

computer_guess = random.randint(0, top_of_range)
guess = 0
while True:
    user_guess = input("Please make a guess: ")
    guess += 1
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number!")
        continue

    if user_guess == computer_guess:
        print("You won")
        break
    elif user_guess > computer_guess:
        print("Hint: Please guess a smaller number!")
    else:
        print("Hint: Please guess a higher number")

print("You won in", guess, "guesses!")

