import random

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

figures = [rock,paper, scissors]

computer_choice = random.randint(0,2)
computer_figure = figures[computer_choice]


human_choice = int(input('Please enter your weapon (rock-0, paper-1, scissors-2): '))
human_figure = figures[int(human_choice)]

print("\n\nHuman:\n" + human_figure)
print("Computer:\n" + computer_figure)

if human_choice == 0 and computer_choice == 2:
    print("Human wins!")
elif human_choice == 1 and computer_choice == 0:
    print("Human wins!")
elif human_choice == 2 and computer_choice == 1:
    print("Human Wins!")
elif human_choice == computer_choice:
    print("We have a tie!")
else:
    print("Comnputer wins :(")