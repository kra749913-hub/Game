import random

item_list = ["Rock", "Paper", "Scissor"]
user_score=0
comp_score=0

for i in range(1, 6):
    print(f"\nRound {i}")

    user_input= int(input('''
1.Rock
2.Scissor
3.paper
    '''))
    
    if user_input == 1:
        user_choice = "Rock"
    elif user_input == 2:
        user_choice = "Scissor"
    elif user_input == 3:
        user_choice = "Paper"
    else:
        print("Invalid input")
        continue
    
    comp_choice = random.choice(item_list)
    print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

    if user_choice == comp_choice:
        print("Match Tie")

    elif user_choice == "Rock":
        if comp_choice == "Paper":
            print("Paper cover Rock = Computer win")
            comp_score+=1
        elif comp_choice == "Scissor":
            print("Rock smashes Scissor = You win")
            user_score+=1
    elif user_choice == "Paper":
        if comp_choice == "Scissor":
            print("Scissor cuts Paper = Computer win")
            comp_score+=1
        elif comp_choice == "Rock":
            print("Paper cover rock = You win")
            user_score+=1

    elif user_choice == "Scissor":
        if comp_choice == "Rock":
            print("Rock samshes scissor= computer win")
            comp_score+=1
        elif comp_choice == "Paper":
            print("Scissor cut Paper = You win")
            user_score+=1
    
print("\nFinal Score📜:")
print("User:", user_score)
print("Computer:", comp_score)

if user_score > comp_score:
    print("🏆 You are the winner")
elif comp_score > user_score:
    print("🏆 Computer is the winner")
else:
    print("🤝 Overall match draw")
