import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"   
choice = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!")
print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
user_choice = int(input())
user_selection = choice[user_choice]
computer_choice = choice[random.randint(0, 2)]    

if user_selection == computer_choice:
    print(f"You chose {user_selection}, computer chose {computer_choice}. It's a draw!")
else:
    if user_selection == rock and computer_choice == scissors:
        print(f"You chose {user_selection}, computer chose {computer_choice}. You win!")
    elif user_selection == paper and computer_choice == rock:
        print(f"You chose {user_selection}, computer chose {computer_choice}. You win!")
    elif user_selection == scissors and computer_choice == paper:
        print(f"You chose {user_selection}, computer chose {computer_choice}. You win!")
    else:
        print(f"You chose {user_selection}, computer chose {computer_choice}. You lose!")       