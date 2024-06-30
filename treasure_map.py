line1 = ["⬜","⬜","⬜"]
line2 = ["⬜","⬜","⬜"]
line3 = ["⬜","⬜","⬜"] #list
map = [line1,line2,line3] #nested list
print("hiding your treasure !, X mark is the spot")
position = input()
abc = ["a","b","c"] #list of rows
letters = position[0].lower() 
letters_index = abc.index(letters)
number_index = int(position[1]) - 1
map[number_index][letters_index] = "x"
print(f"{line1}\n{line2}\n{line3}")

#    a     b    c
#1  ⬜","⬜","⬜"
#2  ⬜","⬜","⬜"
#3  ⬜","⬜","⬜"a3
