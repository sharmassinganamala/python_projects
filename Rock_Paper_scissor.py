#rock_paper_scissor
# rules
# 1 . Rock beats scissors and loses to paper. 
# 2 . Paper beats rock, but loses to scissors.
# 3 . Scissors beat paper but loses to rock.
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
game_images = [rock,paper,scissors] #nested list
user_choose = int(input("choose 0 for Rock , 1 for paper , 2 for scissors :\n")) #taking user input
print(game_images[user_choose]) #by that input adding game images to that
computer_choice = random.randint(0,2)
print(f"computer choice : {computer_choice} ") #computer chooses random number from 0 - 1 
print(game_images[computer_choice])
#conditions for rock paper scissors game
if user_choose >= 3 or user_choose < 0:
    print("Enter valid number") #if the input is 3 or above 3 and less than zero it shows error
elif computer_choice == user_choose:
    print("The match draw")
elif user_choose == 0 and computer_choice == 1:
    print("computer wins")
elif user_choose == 1 and computer_choice == 2:
    print("Computer wins")
elif user_choose == 2 and computer_choice == 0:
    print("Computer wins")
elif computer_choice == 0 and user_choose == 1:
    print("You won")
elif computer_choice == 1 and user_choose == 2:
    print("You won")
elif computer_choice == 2 and user_choose == 0:
    print("YOu won")
