'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 
 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""  
     
    # loop to see the postion of the character in list(alphabets) present in the "text" input 
    # so that we can shift the postion acc to the shift number provides by the user. 
                
    for letter in plain_text:                 
       position = alphabet.index(letter)
       new_position = position + shift_amount
       new_letter = alphabet[new_position]
       cipher_text += new_letter
    print(f'The encoded text is {cipher_text}.')

def decrypt(cipher_text, shift_amount):
    caesar_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        old_position = position - shift_amount
        old_letter = alphabet[old_position]
        caesar_text += old_letter
    print(f'The decoded text is {caesar_text}')

if direction == "encode":
    encrypt(plain_text= text, shift_amount= shift)
elif direction == "decode":
    decrypt(cipher_text= text, shift_amount= shift)
'''

#optimized way of above code
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
  'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction): # optimized by creating single function
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1            #this will turn shift_amount to negative
    for char in start_text:
        if char in alphabet:            #this condition is to include " ", or asny special character or number if that is present in the input text
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
            
        

    print(f"Here's the {direction}d result: {end_text}")

    

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end == True
        print("Goodbye!")
        exit()




