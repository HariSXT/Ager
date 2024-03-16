import time
import os
import sys
ascii_art = """
                                 
     /\                          
    /  \      __ _    ___   _ __ 
   / /\ \    / _` |  / _ \ | '__|
  / ____ \  | (_| | |  __/ | |   
 /_/    \_\  \__, |  \___| |_|   
              __/ |              
             |___/               
"""

print(ascii_art)
print("      -Made by HarisXT-")
def animated_loading(stop_condition):
    while not stop_condition():  # Loop until the stop condition is True
        for i in range(4):
            sys.stdout.write('\rLoading' + '.' * i)
            sys.stdout.flush()
            time.sleep(0.5)
    print("\nLoading stopped.")

# Example stop condition
def stop_condition():
    # Add your condition here
    # For example, stop after 10 seconds
    return time.time() > start_time + 10

# Start the loading animation
start_time = time.time()
animated_loading(stop_condition)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Call the function to clear the screen
clear_screen()
ascii_art = """
                                 
     /\                          
    /  \      __ _    ___   _ __ 
   / /\ \    / _` |  / _ \ | '__|
  / ____ \  | (_| | |  __/ | |   
 /_/    \_\  \__, |  \___| |_|   
              __/ |              
             |___/               
"""

print(ascii_art)
print("      -Made by HarisXT-")
def check_age():
  age = int(input("Enter your age: "))
  if age == 1:
    print("You have 17 years till you can get a diploma")

  if age == 2:
    print("You have 16 years till you can get a diploma")

  if age == 3:
    print("You have 15 years till you can get a diploma")

  if age == 4:
    print("You have 14 years till you can get a diploma")

  if age == 5:
    print("You have 13 years till you can get a diploma")

  if age == 6:
    print("You have 12 years till you can get a diploma")

  if age == 7:
    print("You have 11 years till you can get a diploma")

  if age == 8:
    print("You have 10 years till you can get a diploma")

  if age == 9:
    print("You have 9 years till you can get a diploma")

  if age == 10:
    print("You have 8 years till you can get a diploma")

  if age == 11:
    print("You have 7 years till you can get a diploma")

  if age == 12:
    print("You have 6 years till you can get a diploma")

  if age == 13:
    print("You have 5 years till you can get a diploma")

  if age == 14:
    print("You have 4 years till you can get a diploma")

  if age == 15:
    print("You have 3 years till you can get a diploma")

  if age == 16:
    print("You have 2 years till you can get a diploma")

  if age == 17:
    print("You have 1 years till you can get a diploma")

  if age == 18:
    print("Congratulations, you can get a diploma")
  
  if age > 18:
    print("Congratulations, you can get a diploma")
  time.sleep(5)
check_age()
def animated_exiting(stop_condition):
    while not stop_condition():  # Loop until the stop condition is True
        for i in range(4):
            sys.stdout.write('\rExiting' + '.' * i)
            sys.stdout.flush()
            time.sleep(0.5)
    print("\nExiting stopped.")

# Example stop condition
def stop_condition():
    # Add your condition here
    # For example, stop after 10 seconds
    return time.time() > start_time + 5

# Start the loading animation
start_time = time.time()
animated_exiting(stop_condition)
