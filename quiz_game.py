print("Welcom to my quiz game!")

playing = input("Type yes if you want to play: " ).lower()

if playing != "yes":
    print("See you next time!")
    quit()
else:
    print("Good Luck")

score = 0

answer1 = input("What does CPU stand for: ").lower()
if answer1 == "central processing unit":
    score1 = 1
    score += score1
    print("You are correct! You got", score1, "added to the final score!")
else:
    score -= 0.5
    print("Incorrect You got 0.5 deducted from final score")

answer2 = input("Longest building in the world: ").lower()
if answer2 == "burj khalifa":
    score2 = 1.3
    score += score2
    print("You are correct! You got", score2, "added to the final score!")
else:
    score -= 0.7
    print("Incorrect You got 0.7 deducted from final score")

answer3 = input("What's the longest river in the world: ").lower()
if answer3 == "nile":
    score3 = 1.5
    score += score3
    print("You are correct! You got", score3, "added to the final score!")
else:
    score -= 0.9
    print("Incorrect You got 0.9 deducted from final score")

print("you need atleast 1 score to win")
print("You got", score, "score")
if score >= 1:
    print("Congratulation you won!")
else:
    print("You lost")