import datetime
import random

def get_message_of_the_day():
    messages = [
        "Make today amazing!",
        "Every day is a new opportunity.",
        "Keep learning, keep growing.",
        "Do something today that your future self will thank you for.",
        "Small steps lead to big changes.",
        "Be the reason someone smiles today."
    ]
    return random.choice(messages)

def greet():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    motd = get_message_of_the_day()
    print(f"Hello world, I'm x - Today is {current_date}")
    print(f"Message of the day: {motd}")
     
if __name__ == "__main__":
    greet()
# This code is a simple greeting function that prints the current date.