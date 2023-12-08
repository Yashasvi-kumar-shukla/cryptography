import os
from logo import logo
def encrypt(x,y):
    cipher=""
    for letter in x:
        if letter not in alphabet:
            cipher+=letter
        else:
            position=alphabet.index(letter)
            n_position=position+y
            if n_position>=25:
                n_position=n_position-25
            cipher+=alphabet[n_position]
    return cipher

def decrypt(x,y):
    decypher=""
    for letter in x:
        if letter not in alphabet:
            decypher+=letter
        else:
            position=alphabet.index(letter)
            n_position=position-y
            if n_position<0:
                n_position=n_position+25
            decypher+=alphabet[n_position]
    return decypher

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']
print(logo)
while(True):
    direction = input("type 'encode' to encrypt, type 'decode' to decrypt, type 'exit' to exit:")
    clear_screen()
    print(logo)
    if direction=="encode":
        text=input("enter your text here:\n").lower()
        shift=int (input("type the shift number:"))
        text=encrypt(text,shift)
        print("encrypted text:\n"+text)
        
    elif direction=="decode":
        text=input("enter your text here:\n").lower()
        shift=int (input("type the shift number:"))
        text=decrypt(text,shift)
        print("Decrypted text:\n"+text)
    elif direction=="exit":
        print("Thank you")
        exit()



