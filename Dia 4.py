rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_image = [rock, paper,scissors ]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choice >=3 or choice <0:
  print("You lost, this number is invalid")
else:
  print(game_image[choice])

choice_computer = random.randint(0,2)
print(f"O computador escolheu {choice_computer}")
print(game_image[choice_computer])

if choice == 0 and choice_computer ==1:
  print("Paper win")
elif choice == 0 and choice_computer ==2:
  print("Rock Win")
elif choice == 0 and choice_computer == 0:
  print("Empate")
elif choice == 1 and choice_computer ==1:
  print("Empate")
elif choice == 1 and choice_computer ==2:
  print("scissors Win")
elif choice == 1 and choice_computer == 0:
  print("Paper Wins")
elif choice == 2 and choice_computer ==1:
  print("scissors win")
elif choice == 2 and choice_computer ==2:
  print("Empate")
elif choice == 2 and choice_computer == 0:
  print("Empate")
elif choice >=3 or choice <0:
  print("You lost, this number is invalid")