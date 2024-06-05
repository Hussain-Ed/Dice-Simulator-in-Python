import random
import time

x = "r"
print("\n")
print(f"'Welcome to Dice Simulator'\n")
print("Instructions: The Dice simulator generates a number between 1 and 6 in a single dice.\n")
time.sleep(1)

while x == "r":
    
    x= input(f"Press 'r' to roll again and 'e' to exit: ")

    # Generates a random number
    # between 1 and 6 (including
    # both 1 and 6
    no = random.randint(1,6)

    if x == "r" or x == "R":
        print()
    elif x == "e" or x == "E":
        print("Thankyou for playing!")
        break
    else:
        print("Invalid input")
        break


    if no == 1:
        print("[--------]")
        print("[        ]")
        print("[    0   ]")
        print("[        ]")
        print("[--------]")
        print("You rolled : 1")


    if no == 2:
        print("[--------]")
        print("[  0     ]")
        print("[        ]")
        print("[     0  ]")
        print("[--------]")
        print("You rolled : 2")

    if no == 3:
        print("[--------]")
        print("[        ]")
        print("[ 0 0 0  ]")
        print("[        ]")
        print("[--------]")
        print("You rolled : 3")


    if no == 4:
        print("[--------]")
        print("[0      0]")
        print("[        ]")
        print("[0      0]")
        print("[--------]")
        print("You rolled : 4")


    if no == 5:
        print("[--------]")
        print("[0      0]")
        print("[    0   ]")
        print("[0      0]")
        print("[--------]")
        print("You rolled : 5")
        
        
       
    if no == 6:
        print("[--------]")
        print("[0  0  0 ]")
        print("[        ]")
        print("[0  0  0 ]")
        print("[--------]")
        print("You rolled : 6")
    

    print("\n")