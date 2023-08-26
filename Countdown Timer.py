import time
import os
from plyer import notification

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Countdown Timer")
    print("Select an option")
    print("1. Set a timer")
    print("2. Exit")

    option = input("Option: ")
    if option == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Set a timer")
        seconds = int(input("Enter the number of seconds: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        start_time = time.time()
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            elapsed_time = int(time.time() - start_time)
            if elapsed_time >= seconds:
                print("Time's up!")
                notification.notify(
                title = "Time's up!",
                message="The time set on the countdown timer is up!" ,
                )
                time.sleep(5)
                break
            print(f"Time remaining: {seconds - elapsed_time} seconds")
            time.sleep(1)

    if option == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Exiting...")
        time.sleep(1)
        break
