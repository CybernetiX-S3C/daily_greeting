import time
import random

def get_greeting():
    current_hour = time.localtime().tm_hour
    if 5 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

def morning_greeting():
    name = input("What's your name? ")
    greeting = f"""{get_greeting()} {name}!\n"""
    print(greeting)

    # Ask for the greeting style
    print("Choose a greeting style:")
    print("1. Friendly")
    print("2. Formal")
    print("3. Playful")
    choice = int(input("Enter the number of your choice: "))

    # Additional greeting styles
    if choice == 2:
        print(f"Good day, {name}. How may I assist you?")
    elif choice == 3:
        print(f"Hey there, {name}! Ready to conquer the day?")
    else:
        print(f"Hey, {name}! What's up?")

    # Pause duration
    duration = int(input("How many seconds do you want to pause for? "))
    time.sleep(duration)

    # Random fact after greeting
    facts = [
        "Did you know that honey never spoils?",
        "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
        "A group of flamingos is called a 'flamboyance'.",
        "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
        "Octopuses have three hearts: two pump blood through the gills, and one pumps blood through the rest of the body."
    ]
    print("Choose a topic for an interesting fact:")
    print("1. Science")
    print("2. History")
    print("3. Animals")
    topic_choice = int(input("Enter the number of your choice: "))

    if topic_choice == 1:
        print(random.choice(facts[0:2]))  # Select from science facts
    elif topic_choice == 2:
        print(random.choice(facts[2]))  # Select from history facts
    elif topic_choice == 3:
        print(random.choice(facts[3:]))  # Select from animal facts

    # Riddle section
    print("Here's a riddle for you:")
    print("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
    answer = "an echo"
    user_answer = input("Your answer: ")

    if user_answer.lower() == answer:
        print("Correct! You're sharp!")
    else:
        print(f"Oops, that's not the right answer. The correct answer is: {answer}")

if __name__ == "__main__":
    morning_greeting()
