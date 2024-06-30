# love_score_calculator
print("Enter first name  : " )
name1 = input()
print("Enter second name : " )
name2 = input()
combined_score = name1 + name2
t = combined_score.count("t")
r = combined_score.count("r")
u = combined_score.count("u")
e = combined_score.count("e")
first_digit = t + r + u + e #adding all the letter given in input one
l = combined_score.count("l")
o = combined_score.count("o")
v = combined_score.count("v")
e = combined_score.count("e")
second_digit = l + o + v + e # adding all the letters given in the input second
love_score1 = str(first_digit) + str(second_digit)#the o/p in string
love_score = int(love_score1) # converting the string into integer
print(f"The love score is {love_score}")
if love_score < 10:
    print("The love score is less between this two name")
elif love_score >=10 and love_score < 45:
    print("The love score between this two name is moderate")
elif love_score > 45 and love_score < 100:
    print("The love score is good ! ")
else:
    print("The love score is very high between two names ")
print("Thanks for using love score calculator!!!!!!")



