import random

game = ["rock", "paper", "scissors"]

user_choice = int(input("Welcome to the rock, paper and scissors game. Press 0 to choose rock, 1 for paper and 2 for scissors\n"))

computer_choice = random.randint(0,2)

if(user_choice>2 or user_choice<0):
    print("Invalid input. Please try again")
else:
    print(f"You chose {game[user_choice]}")
    print(f"Computer chose {game[computer_choice]}")

    if user_choice==computer_choice:
        print("Game Drawn")
    elif user_choice==0:
        if(computer_choice==1):
            print("You lost")
        else:
            print("You won")
    elif user_choice==1:
        if(computer_choice==0):
            print("You won")
        else:
            print("You lost")    
    else: 
        if(computer_choice==0):
            print("You lost")
        else:
            print("You lost")    
    
    
