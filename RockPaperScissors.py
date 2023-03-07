# Rock-Paper-Scissors game with computer
import random
user = input("Enter 'r' for Rock, 'p' for Paper or 's' for Scissors: ")

computer = random.choice(['r', 'p', 's'])

# Paper is better than Rock
# Rock is better than Scissors
# Scissors is better than Paper
if user == 'r' and computer == 's':
    print("Computer selected Scissors and you won!")
elif user == 'p' and computer == 'r':
    print("Computer selected Rock and you won!")
elif user == 's' and computer == 'p':
    print("Computer selected Paper and you won!")
elif user == 'r' and computer == 'r':
    print("Computer selected Rock and its a tie!")
elif user == 'p' and computer == 'p':
    print("Computer selected Paper and its a tie!")
elif user == 's' and computer == 's':
    print("Computer selected Scissors and its a tie!")
else:
    print(f"Computer selected {computer} and you lost!")


