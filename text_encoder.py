logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
should_end = False
while not should_end:
    alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    direction = input("Type encode for 'encrypt' or Type decode for 'decrypt' : ")
    text = input("Type your message : ").lower()
    shift = int(input("Enter shift number : "))
    shift = shift % 26
    def encrypt(plain_text,shift_amount):
        cyper_text = ""
        for letters in plain_text:
            position = alphabets.index(letters)
            new_position = position + shift_amount
            cyper_text += alphabets[new_position]
        print(f"The encrypt sentence is {cyper_text}")
    def decrypt(plain_text1,shift_amount):
        cyper_text1 = ""
        for letters in plain_text1:
            position = alphabets.index(letters)
            new_position  = position - shift_amount
            cyper_text1 += alphabets[new_position]
        print(f"The decrypt message is {cyper_text1}")
    if direction == "encode":
        encrypt(plain_text=text,shift_amount=shift)
    elif direction == "decode":
        decrypt(plain_text1=text,shift_amount=shift)
    else:
        print("Enter correct sentence in the direction")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")




