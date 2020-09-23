from random import*

random=(randint(0,50))
guess=int()
guess_count= 0
out_of_guesses= False
hint_count= 0
ask_hint=""
hint_1="it is an even number"
hint_2= "it is an odd number"
hint_3= "the number is between 0 to 25 exclusive"
hint_4= "the number is between 25 inclusive to 50"

print(random)
print("guess a number between 1 to 50: ")
while guess != random and not (out_of_guesses):
    if guess_count <3:
        guess= int(input("enter a number: "))
        guess_count += 1
    elif guess_count == 3:
        ask_hint= input("Do you want a hint?: ")
        if ask_hint.lower()== "yes":
            if random%2 == 0:
                print(hint_1)
                guess= int(input("enter a number: "))
                guess_count += 1
                hint_count += 1
            else:
                print(hint_2)
                guess= int(input("enter a number: "))
                guess_count += 1
                hint_count+= 1
        else:
            print("Input lagi goblok!")
            guess= int(input("enter a number: "))
            guess_count += 1
    elif guess_count == 5:
        if hint_count == 1:
            ask_hint=input("Do you want your last hint?: ")
            if ask_hint.lower()=="yes":
                if random >= 0 and random<25:
                    print(hint_3)
                    guess= int(input("enter a number: "))
                    guess_count += 1
                    hint_count += 1
                else:
                    print(hint_4)
                    guess= int(input("enter a number: "))
                    guess_count += 1
                    hint_count += 1
            else:
                print("Input lagi goblok!")
                guess= int(input("enter a number: "))
                guess_count += 1
        else:
            ask_hint= input("Do you want a hint?: ")
            if ask_hint.lower()=="yes":
                if random%2 == 0:
                    print(hint_1)
                    guess= int(input("enter a number: "))
                    guess_count += 1
                    hint_count += 1
                else:
                    print(hint_2)
                    guess= int(input("enter a number: "))
                    guess_count += 1
                    hint_count+= 1
    elif guess_count == 7:
        if hint_count == 0:
            ask_hint= input("Do you want a hint?: ")
            if ask_hint.lower()=="yes":
                if random%2 == 0:
                    print(hint_1)
                    guess= int(input("enter a number: "))
                    guess_count += 1
                    hint_count += 1
                else:
                    print(hint_2)
                    guess= int(input("enter a number: "))
                    guess_count += 1
                    hint_count+= 1
        elif hint_count == 1:
            ask_hint= input("Do you want another hint?: ")
            if ask_hint.lower()== "yes":
                if random >= 0 and random<25:
                    print(hint_3)
                    guess= int(input("enter a number: "))
                    guess_count += 1
                    hint_count += 1
                else:
                    print(hint_4)
                    guess= int(input("enter a number: "))
                    guess_count += 1
                    hint_count += 1
        else:
            ask_hint= input("Do you want another hint?: ")
            print("gaada clue lagi anjg")
            guess= int(input("enter a number: "))
            guess_count += 1
    elif guess_count < 10:
        guess= int(input("enter a number: "))
        guess_count += 1
    else:
        out_of_guesses= True
if out_of_guesses:
    print ("kalah tot")
else:
    print ("menang asu")



    
        