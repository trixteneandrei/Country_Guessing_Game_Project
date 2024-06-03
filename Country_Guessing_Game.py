import random  # Importing the random module to generate random numbers
import time    # Importing the time module for adding delays

# Welcome message and introduction to the game
print("Hi! Welcome to the guessing game! I am going to pick a country and you have to guess it. Oh and by the way, the first letter of your answer has to be in Caps. Here we go!")
time.sleep(4)  # Adding a delay of 4 seconds
print("Picking a country...")
time.sleep(2)  # Adding a delay of 2 seconds

# Dictionary of countries
country_dict = {
    1: "Philippines",
    2: "Thailand",
    3: "Vietnam",
    4: "Indonesia",
    5: "Malaysia",
    6: "China",
    7: "Japan",
    8: "Korea",
    9: "Singapore"
}

# Function to generate a random country
def generate_random_country():
    random_number = random.randint(1, len(country_dict))
    country_name = country_dict[random_number]
    return country_name

random_country = generate_random_country()  # Generating a random country

guess_count = 1  # Initializing guess count to 1

# Asking the user to guess the country
guess = input("What is your guess?: ")

# Checking if the guess is incorrect
if guess not in country_dict.values():
    print("Nope. I'll give you a hint, it's in Asia.")
    guess = input("What is your guess?: ")
    guess_count += 1

# Providing additional hints if the guess is still incorrect
if guess != random_country:
    print(f"Nope. I'll give you a hint. The first letter of the country is: {random_country[0]}")
    guess = input("What is your guess?: ")
    guess_count += 1

if guess != random_country:
    print(f"Nope. I'll give you a hint. The second letter of the country is: {random_country[1]}")
    guess = input("What is your guess?: ")
    guess_count += 1

if guess != random_country:
    print(f"Nope. I'll give you a hint. The third letter of the country is: {random_country[2]}")
    guess = input("What is your guess?: ")
    guess_count += 1

# Giving a final hint if the guess is still incorrect
if guess != random_country:
    print("That was your last hint! You have one last try left, if you don't get it this time you'll lose!")
    guess = input("What is your guess?: ")
    guess_count += 1

# Checking if the final guess is correct
if guess != random_country:
    print("Oh no... you lost... good try though!")

# Displaying the result if the guess is correct
if guess == random_country:
     print(f"Congrats! The right answer was {random_country}. It took you {guess_count} guesses. You DO know your countries!")