import random

options = ["rock", "paper", "scissor"]
user_score = 0
computer_score = 0
tie = 0

while True:
    
    user_input = input("Type Rock/Paper/Scissors to start or q to quit: ").lower()
    
    if user_input == "q":
        break
    
    if user_input not in options:
        print("Invalid input please try again!")
        continue

    random_number = random.randint(0,2)
    
    computer_pick = options[random_number]

    if computer_pick == user_input:
        print("You Tied!")
        tie += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("User won")
        user_score += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("User won")
        user_score += 1
    elif user_input == "rock" and computer_pick == "scissor":
        print("User won")
        user_score += 1

    else:
        print("Computer won")
        computer_score += 1
        
    

print("You won", user_score, "times!")
print("Computer won", computer_score, "times!")
print("You both tied", tie , "times!")    

