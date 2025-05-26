import random
from datetime import datetime

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
    
    # Build funky greeting
    random_color = random.choice(colors)
    random_emoji = random.choice(emojis)
    
    funky_greeting = f"{random_color}Hello world, I'm y {random_emoji} - Funky time: {current_time}{reset}"
    print(funky_greeting)

if __name__ == "__main__":
    greet()