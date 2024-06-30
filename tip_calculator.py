# welcome to calculator
print("Welcome to the tip caculator  ")
# total amount of bill
bill = float(input("Enter the total amount of Bill : "))
# total members
members = int(input("Numbers of members : "))
# how much percentage you are going to give
tip_percentage = int(input("How much percentage would you like to give 10 , 15 , 20 : "))
# tip per person
tip = float((bill/members)//tip_percentage)
print(f"The tip per person is {tip}")