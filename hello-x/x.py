import datetime

def greet():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f"Hello world, I'm x - Today is {current_date}")
     
if __name__ == "__main__":
    greet()