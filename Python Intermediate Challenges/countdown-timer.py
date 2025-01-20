# write a function to generate a simple timer
import time

def countdown_timer(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
