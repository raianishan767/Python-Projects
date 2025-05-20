""""
Workflow of project:
There are 3 options=Rock,paper,Scissor
User chooses one
Computer chooses one(Randomly instead of conditionally)

Case A: Rock
Rock-Rock = Match tie
Rock-Paper = Paper Wins
Rock-Scissor = Rock wins

Case B: Paper
Paper-Paper = Match tie 
Paper-Rock = Paper Wins
Paper-Scissor = Scissor wins
 
Case C: Scissor 
Scissor-Scissor = Match tie
Scissor-Rock = Rock wins
Scissor-Paper = Scissor wins

"""
import random
item_list=["rock","paper","scissor"]
user_choice=input("Choose one : Rock,Paper,Scissor ")
computer_choice=random.choice(item_list)

print(f"User choice : {user_choice},Computer choice : {computer_choice}")

if user_choice==computer_choice:
    print("Both chooses same = Match Tie")
elif user_choice=="rock":
    if computer_choice=="paper":
        print("Paper covers Rock = Computer wins")
    else:
        print("Rock smashes Scissor = You win")
elif user_choice=="paper":
    if computer_choice=="rock":
        print("Paper covers Rock = You win")
    else:
        print("Scissor cuts Paper = Computer wins")
elif user_choice=="scissor":
    if computer_choice=="paper":
        print("Scissor cuts Paper = You win")
    else:
        print("Rock smashes Scissor = Computer wins")