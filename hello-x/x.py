from datetime import datetime

def greet():
    print("Hello world, I'm x")
    print(f"Current date: {datetime.now().date()}")

if __name__ == "__main__":
    greet()