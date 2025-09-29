import random

def non_adjacent_permutation(n):
    numbers = list(range(1, n+1))
    sequence = []

    while numbers:
        valid_choices = [num for num in numbers if not sequence or abs(num - sequence[-1]) > 1]
        if not valid_choices:
            break
        choice = random.choice(valid_choices)
        sequence.append(choice)
        numbers.remove(choice)
    
    # If the sequence is incomplete, try again until success
    if len(sequence) < n:
        return non_adjacent_permutation(n)
    return sequence

sequence_1_to_32 = non_adjacent_permutation(32)
print(sequence_1_to_32)

def generate_non_adjacent_sequence(n):
    while True:
        numbers = list(range(1, n+1))
        random.shuffle(numbers)
        # check adjacency
        if all(abs(numbers[i] - numbers[i-1]) > 1 for i in range(1, len(numbers))):
            return numbers
how_long = int(input("What is the upper value? "))
sequence_1_to_how_long = non_adjacent_permutation(how_long)
print(sequence_1_to_how_long)

sequence_1_to_how_long = generate_non_adjacent_sequence(how_long)
print(sequence_1_to_how_long)
