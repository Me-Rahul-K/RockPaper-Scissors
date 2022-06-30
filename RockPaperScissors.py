import random

exit = False
your_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock,paper, scissors or exit: ")
    comp_input = random.choice(options)

    if user_input == "exit":
        print("Game ended")
        print("Your total score is",str(your_points))
        print("Computer's total score is",str(computer_points))
        exit = True

    if user_input == "rock":

        if comp_input == "rock":
            print("You chose rock")
            print("Computer chose rock")
            print("It is a tie!")
        elif comp_input == "paper":
            print("You chose rock")
            print("Computer chose paper")
            print("Computer Won")
            computer_points += 1
        elif comp_input == "scissors":
            print("You chose rock")
            print("Computer chose scissors")
            print("You Won")
            your_points += 1

    elif user_input == "paper":

        if comp_input == "rock":
            print("You chose paper")
            print("Computer chose rock")
            print("You Won")
            your_points += 1
        elif comp_input == "paper":
            print("You chose paper")
            print("Computer chose paper")
            print("It is a tie!")
        elif comp_input == "scissors":
            print("You chose paper")
            print("Computer chose scissors")
            print("Computer Won")
            computer_points += 1

    elif user_input == "scissors":

        if comp_input == "rock":
            print("You chose scissors")
            print("Computer chose rock")
            print("Computer Won")
            computer_points += 1
        elif comp_input == "paper":
            print("You chose scissors")
            print("Computer chose paper")
            print("You Won")
            your_points += 1
        elif comp_input == "scissors":
            print("You chose scissors")
            print("Computer chose scissors")
            print("It's a tie!")

    elif user_input != "scissors" or user_input != "paper" or user_input != "rock" or user_input != "exit":
        print("Invalid Input")
