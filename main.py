import random

machine_score = 0
user_score = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Rock,Paper or Scissor? or q to quit ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]

    if computer_pick == user_input:
        print("We tied!")
    elif computer_pick == "rock" and user_input == "paper":
        print("Wou won!")
        user_score += 1
    elif computer_pick == "scissor" and user_input == "rock":
        print("Wou won!")
        user_score += 1
    elif computer_pick == "rock" and user_input == "paper":
        print("Wou won!")
        user_score += 1
    else:
        print("Yout lost")
        machine_score =+ 1

    
    print("Computer picked " + str(computer_pick) + ".")  

print("Computer: " + str(machine_score) + " x  You:" + str(user_score))
print("Bye")