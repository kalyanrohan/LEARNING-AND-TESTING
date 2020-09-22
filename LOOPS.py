#while loop will keep looping code as long as the conditions are met

#making a trivia game
ans= "Indonesia"
guess_count= 0
guess= ""
question= "Which country has the highest coffee bean exports?"
ask_hint= ""
hint="It is the fourth most populated country in the world"
out_of_guesses=False
print(question)
while guess != ans and not (out_of_guesses):
    if guess_count<3:
        guess=input("enter your answer: ")
        guess_count += 1
    elif guess_count==3:
        ask_hint=input("Do you want a hint?: ")
        if ask_hint=="Yes"or ask_hint=="yes"or ask_hint=="YES":
            print(hint)
            guess=input("enter your answer: ")
            guess_count += 1
        else:
            guess=input("enter your answer: ")
            guess_count += 1 
    elif guess_count<5:
        guess=input("enter your answer: ")
        guess_count += 1
    else:
        out_of_guesses=True
        
if out_of_guesses:
    print("you loose")
else:
    print("you win")
