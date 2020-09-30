import random

RAND = random.randint(1, 50)
MAX_TRIES = 10
tries = 1

hints = [
    "The number is even.",
    "The number is between 1 and 25 inclusively.",
    "SIKE ! No more hints."
]

if (RAND % 2 == 1):
    hints[0] = "The number is odd."

if (RAND > 25):
    hints[1] = "The number is between 26 and 50 inclusively."

while (tries < MAX_TRIES):

    guess = input("Enter a number: ")
    if (not guess.isnumeric()):
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if (guess != RAND):
        print("Your guess is wrong! Try again.")
        print("Try", tries, "out of", MAX_TRIES)

        # Lets say we give the user a hint every 3 attempts they fail.
        if (tries % 3 == 0):
            while (True):
                response = input("Do you want a hint? ").lower()
                if response == "yes":
                    print(hints[tries // 3 - 1])
                    break
                elif response == "no":
                    print("ok.")
                    break
                print("Enter a valid answer ! (yes/no)")
    else:
        print("Congratulations. You got it right!")
        print("The number of attempts:", tries)
        exit()

    tries+=1

print("You lost !")
print("The actual number is", RAND)