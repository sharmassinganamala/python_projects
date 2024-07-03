import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   
print(logo)
def deal_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score , computer_score):
     if user_score > 21 and computer_score > 21:
          return "you went over , you lost?\n "
     if user_score == computer_score:
          return "The match draw\n"
     elif computer_score == 0:
          return "computer has black_Jack you lost\n"
     elif user_score == 0:
          return "You have Black_Jackt you Won!\n"
     elif user_score > 21:
          return "you went over 21 you lost\n"
     elif computer_score > 21:
          return "opponent went over you Won\n"
     elif user_score > computer_score:
          return "you Won\n"
     else:
          return "You lost\n"

def play_game():
    user_cards = []
    computers_cards = []
    is_game_over =False
    for i in range(2):
        user_cards.append(deal_cards())
        computers_cards.append(deal_cards())
    
    while not is_game_over:
         user_score = calculate_score(user_cards)
         computer_score = calculate_score(computers_cards)
         print(f"Your cards {user_cards} you current Score {user_score}")
         print(f"computer first card {computers_cards[0]}")
         if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
         else:
              user_should_deal = input("Type Y for another card or Type N for pass !\n").lower()
              if user_should_deal == "y":
                   user_cards.append(deal_cards())
              else:
                   is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
         computers_cards.append(deal_cards())
         computer_score = calculate_score(computers_cards)
    
    print(f"   Your final hand: {user_cards}, final score: {user_score}\n")
    print(f"   Computer's final hand: {computers_cards}, final score: {computer_score}\n")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()