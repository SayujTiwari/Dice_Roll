import random

# Function to roll 2 dice
def roll2Dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(die1, die2, "(sum: " + str(die1 + die2) + ")")
    return die1 + die2

# Menu function
def menu():
    print("Dice Roll Simulator Menu")
    print("1. Roll Dice Once")
    print("2. Roll Dice 5 Times")
    print("3. Roll Dice 'n' Times")
    print("4. Roll Dice until Snake Eyes")
    print("5. Exit")

# Roll dice once function
def rollDiceOnce():
    roll2Dice()

# Roll dice 5 times function
def rollDice5Times():
    for i in range(5):
        roll2Dice()

# Roll dice n times function
def rollDiceNTimes():
    n = int(input("How many rolls would you like? "))
    for i in range(n):
        roll2Dice()

# Roll dice until snake eyes function
def rollDiceUntilSnakeEyes():
    count = 0
    while True:
        count += 1
        result = roll2Dice()
        if result == 2:
            print("SNAKE EYES! It took", count, "rolls to get snake eyes.")
            break

# Main program
while True:
    menu()
    choice = input("Select an option (1-5): ")
    if choice == '1':
        rollDiceOnce()
    elif choice == '2':
        rollDice5Times()
    elif choice == '3':
        rollDiceNTimes()
    elif choice == '4':
        rollDiceUntilSnakeEyes()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
