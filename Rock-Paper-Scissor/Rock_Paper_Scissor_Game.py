import random

comp_points = 0
user_points = 0
r = 2
def play_game():
    global comp_points, user_points, r
    while r >= 0:
        r -= 1
        comp_sel = ["Rock", "Paper", "Scissor"]
        rand_int = random.randint(0, 2)
        comp_choice = comp_sel[rand_int]

        user_input = input("Enter your choice (Rock, Paper, Scissor):")

        if user_input.capitalize() == "Rock" and comp_choice == "Rock":
            print("Tie!")
        elif user_input.capitalize() == "Rock" and comp_choice == "Paper":
            print("Computer Won!")
            comp_points += 1
        elif user_input.capitalize() == "Rock" and comp_choice == "Scissor":
            print("You Won!")
            user_points += 1
        elif user_input.capitalize() == "Paper" and comp_choice == "Rock":
            print("You Won!")
            user_points += 1
        elif user_input.capitalize() == "Paper" and comp_choice == "Paper":
            print("Tie!")
        elif user_input.capitalize() == "Paper" and comp_choice == "Scissor":
            print("Computer Won!")
            comp_points += 1
        elif user_input.capitalize() == "Scissor" and comp_choice == "Rock":
            print("Computer Won!")
            comp_points += 1
        elif user_input.capitalize() == "Scissor" and comp_choice == "Paper":
            print("You Won!")
            user_points += 1
        elif user_input.capitalize() == "Scissor" and comp_choice == "Scissor":
            print("Tie!")
        else:
            print("Invalid input!!")

    play_again = input("Do you want to play another round..?:(Y/N)")
    if play_again.upper() == "Y":
        r = 2
        play_game()
    if play_again.upper() != "Y" and play_again.upper() != "N":
        print("Invalid input!!")
    elif play_again.upper() == "N":
        if user_points > comp_points:
            print(f"You won the game!!\nUser Points: {user_points}\nComputer Points: {comp_points}")
        elif user_points < comp_points:
            print(f"Computer won the game!!\nUser Points: {user_points}\nComputer Points: {comp_points}")
        elif user_points == comp_points and (user_points > 0 and comp_points > 0):
            print(f"Game Tied!!\nUser Points: {user_points}\nComputer Points: {comp_points}")
        else:
            print(f"User Points: {user_points}\nComputer Points: {comp_points}")

play_game()
