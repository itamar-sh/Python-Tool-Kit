import random


# Generate a random integer
random_number = random.randint(1, 100)
print("Random number:", random_number)

# Generate a random float
random_float = random.random()
print("Random float:", random_float)

# Shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list:", my_list)

# Choose a random element from a list
random_element = random.choice(my_list)
print("Random element:", random_element)

# Sample elements without replacement (can't choose twice same element)
sample = random.sample(range(1, 11), 8)
print("Sample without replacement:", sample)

# Sample elements with replacement
sample_with_replacement = [random.choice(['A', 'B', 'C']) for _ in range(5)]
print("Sample with replacement:", sample_with_replacement)
