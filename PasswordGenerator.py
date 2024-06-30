#IMPORTING RANDOM MODULE
import random

#CREATING LIST
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Special_characters = ['!','@','#','$','%','&']
numbers = ['1','2','3','4','5','6','7','8','9','0']

#TAKING INPUT FROM USER
n_numbers = int(input("Enter how many number do you want :\n"))
n_letters = int(input("Enter how many letters do you want :\n"))
n_Special_characters = int(input("How many special character you need :\n"))

#CREATING AN EMPTY LIST 
password_list = []

#CHOOSING RANDOM LETTERS 
for char in range(1,n_letters+1):
    password_list += random.choice(letters)

#CHOOSING RANDOM NUMBERS
for num in range(1,n_numbers+1):
    password_list += random.choice(numbers)

#CHOOSING  RANDOM SPECIAL CHARACTERS
for symbol in range(1,n_Special_characters+1):
    password_list += random.choice(Special_characters)

#WE ARE SHUFFLEING ALL CHOOSEN ITEM 
random.shuffle(password_list)

print(password_list) #THE SHUFFLED ITEMS IN LIST FORMATE 

#CONVERTING THE LIST FORMATE INTO STRING
password = ""
for char in password_list:
    password = password + char
print(password)