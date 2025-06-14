'''
1. String Slicing and Reversing:
	•	Reversing a string using slicing: card_number[::-1].
	•	Extracting odd-indexed and even-indexed characters using slicing, such as odd_digits = card_number_reversed[::2] and even_digits = card_number_reversed[1::2].

2. String Translation with str.maketrans() and translate():
	•	str.maketrans(): Creating a translation map to remove unwanted characters like hyphens or spaces
	•	translate(): Applying the translation to remove the characters from the card number.


3. Data Conversion:
	•	Converting strings to integers using int(), which is necessary to perform arithmetic on the card digits.
	•	Handling character-to-integer conversion within loops.

4. Mathematical Operations and Conditional Logic:
	•	Doubling digits (for the even-indexed digits in the Luhn Algorithm) and adjusting the result if it’s greater than or equal to 10 by summing the digits (e.g., (number // 10) + (number % 10)).
	•	Using if statements to check conditions (like checking if a doubled digit is >= 10).

5. Looping Through Sequences:
	•	For loops to iterate through odd and even digits separately.
	•	Applying logic in a loop to update sums based on conditions (e.g., adding odd and processed even digits).

6. Modular Arithmetic for Validation:
	•	Using % 10 to check if the total sum is divisible by 10, which is the key validation condition for the Luhn algorithm.

7. Modular Program Structure:
	•	Writing a main function (main()) to handle the overall flow of the program, separating out the input, processing, and output from the algorithm logic in verify_card_number().

8. Working with Input in Different Formats:
	•	Handling a formatted input (with hyphens) and cleaning it (removing non-numeric characters) before performing operations on it.

	
	
'''
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits

    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()
