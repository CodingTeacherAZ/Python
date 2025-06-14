'''

1. Variables and Data Types:
	•	Using variables like text, shift, and custom_key to store strings and integers.
	•	Understanding string manipulation by operating on message and key.

2. Functions:
	•	Defining functions with def, such as caesar(), vigenere(), encrypt(), and decrypt().
	•	Function parameters and return values, as in passing message, offset, and key to functions, and returning results from vigenere().

3. String Methods:
	•	Using .lower() to convert text to lowercase.
	•	Using .find() to locate the index of characters in a string (e.g., finding the position of a letter in the alphabet).
	•	Using .isalpha() to check if a character is a letter.

4. Control Flow:
	•	For loops: Iterating through each character in the text with for char in message.
	•	Conditional statements: Using if and else to handle different cases (e.g., spaces vs. letters in the message).

5. Indexing and Slicing:
	•	Accessing specific characters in strings using indices, such as key[key_index % len(key)].

6. Modular Arithmetic:
	•	Using the modulus operator % to wrap around the alphabet when the shift goes past ‘z’ (e.g., (index + offset) % len(alphabet)).

7. Working with Strings and Characters:
	•	Concatenating characters to form new strings, as in encrypted_text += alphabet[new_index] and final_message += alphabet[new_index].

8. Looping Through Multiple Sequences:
	•	Managing two sequences (the message and key) at the same time in the Vigenère cipher, using key_index to track the position in the key while iterating through the message.

9. Positional Arithmetic:
	•	Adding and subtracting offsets (shifts) from character positions to perform encryption and decryption, and calculating new positions with index + offset*direction.

'''


# Caesar: every single letter is always
# encrypted with the same letter, depending on
# the specified offset.
text = 'Hello Zaira'
shift = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar(text, shift)
caesar(text, 13)

# Vigenere: the offset is different for each letter
# and is determined by another text, called the key.
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
