# import random module
import random

# create a list of options that has rock, paper, scissors
options = ["rock", "paper", "scissors"]

# create a score variable ans set it to 0
score = 0

# create a variable to count the number of rounds
rounds = 0

# create a loop that iterates until the user quits and the score of the user cannot decrease if user loses
while True:
    # create a variable that stores the user's choice
    user_choice = input("Enter a choice (rock, paper, scissors, quit): ")
    # validate that user's choice is rock paper or scissors or quit
    if user_choice not in options and user_choice != "quit":
        print("Invalid choice, try again.")
        continue
    # create a variable that stores the computer's choice
    computer_choice = random.choice(options)

    # create a condition that checks if the user's choice is equal to the computer's choice
    if user_choice == computer_choice:
        print("Tie!")
        print("Computer: " + computer_choice)
        print("User: " + user_choice)
        print("Score: " + str(score))
        print("Rounds: " + str(rounds))
    # create a condition that checks if the user's choice is rock and the computer's choice is scissors
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        score += 1
        rounds += 1
        print("Computer: " + computer_choice)
        print("User: " + user_choice)
        print("Score: " + str(score))
        print("Rounds: " + str(rounds))
    # create a condition that checks if the user's choice is rock and the computer's choice is paper
    elif user_choice == "rock" and computer_choice == "paper":
        print("You lose!")
        rounds += 1
        print("Computer: " + computer_choice)
        print("User: " + user_choice)
        print("Score: " + str(score))
        print("Rounds: " + str(rounds))
    # create a condition that checks if the user's choice is paper and the computer's choice is rock
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        score += 1
        rounds += 1
        print("Computer: " + computer_choice)
        print("User: " + user_choice)
        print("Score: " + str(score))
        print("Rounds: " + str(rounds))
    # create a condition that checks if the user's choice is paper and the computer's choice is scissors
    elif user_choice == "paper" and computer_choice == "scissors":
        print("You lose!")
        rounds += 1
        print("Computer: " + computer_choice)
        print("User: " + user_choice)
        print("Score: " + str(score))
        print("Rounds: " + str(rounds))
    # create a condition that checks if the user's choice is quit and if so, then quit the game
    elif user_choice == "quit":
        print("Thanks for playing!")
        break
