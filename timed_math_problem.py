import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 4
MAX_OPERAND = 10
TOTAL_QUESTION = 4

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operators = random.choice(OPERATORS)

    expr = str(left) + operators + str(right)
    answer = eval(expr)
    
    return expr, answer

input("Press enter to start: ")
print("---------------------------------")
start_time = time.time()

wrong = 0

for i in range(TOTAL_QUESTION):
    expr, answer = generate_problem()
    while True:
        guess = input("Question #"+ str(i+1) + ": " + "What is " + expr + ": ")
        if guess == str(answer):
            break
        wrong += 1

print("---------------------------------")
end_time = time.time()
total_time = round(end_time - start_time, 2)
print(f"You took {total_time} seconds! and were wrong {wrong} times!")
