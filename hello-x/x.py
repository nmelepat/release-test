import datetime

def greet():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello world, I'm x")
    print(f"Current date and time: {formatted_time}")
    

if __name__ == "__main__":
    greet()