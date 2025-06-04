import random
from datetime import datetime

def get_message_of_the_day():
    messages = [
        "Stay groovy and code on!",
        "Today is your day to shine bright!",
        "Embrace the funkiness of life!",
        "Keep those vibes positive and flowing!",
        "Be as awesome as your code!",
        "Rock this day like nobody's watching!"
        "Let your creativity run wild!",
    ]
    return random.choice(messages)

def greet():
    # Funky ANSI color codes
    colors = [
        "\033[95m", # magenta
        "\033[94m", # blue
        "\033[92m", # green
        "\033[93m", # yellow
    ]
    
    # Funky emoji collection
    emojis = ["✨", "🎵", "🔥", "🚀", "🌈", "💯", "🎸", "🤘"]
    
    # Reset color code
    reset = "\033[0m"
    
    # Current time with funky format
    current_time = datetime.now().strftime("%H:%M:%S")
    
    # Get message of the day
    motd = get_message_of_the_day()
    
    # Build funky greeting
    random_color = random.choice(colors)
    random_emoji = random.choice(emojis)
    
    funky_greeting = f"{random_color}Hello world, I'm y {random_emoji} - Funky time: {current_time}{reset}"
    print(funky_greeting)
    print(f"{random.choice(colors)}Message of the day: {motd} {random.choice(emojis)}{reset}")

if __name__ == "__main__":
    greet()
# This code is a funky greeting function that prints the current time with random colors and emojis.