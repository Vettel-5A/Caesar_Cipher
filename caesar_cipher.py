import caesar_cipher_art

#Prints logo from ceasar_cipher_art.py
print(caesar_cipher_art.logo)

#List of letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Define Caesar function, which shifts every letter of the message by the shift amount
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet: 
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

        else:
            end_text += char
    
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Sets while loop condition
restart = 'yes'
while restart == 'yes':
    #Asks user to input the desired action, the message, and the shift number
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    # Checks shift number and performs action. If shift is over 25, then it adjusts the shift number accordingly.
    if shift >= 25:
        while shift >= 25:
            shift = shift % 25
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Asks user if they want to restart program.
    restart = input('Would you like to restart the cipher program? yes or no\n') 