from random import*

random= int(randint(0,50))
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
    elif guess_count ==3:
        ask_hint=input("do you want a hint?: ")
        if ask_hint== "yes" or ask_hint== "Yes" or ask_hint== "YES":
            if random %2 == 0:
                print(hint_1)
                guess= int(input("enter a number: "))
                guess_count += 1
                hint_count +=1
            else:
                print(hint_2)
                guess= int(input("enter a number: "))
                guess_count += 1
                hint_count += 1
        else:
            guess= int(input("enter a number: "))
            guess_count += 1
    elif guess_count == 5:
        ask_hint= (input("do you want a hint?: ")
        if ask_hint=="yes" or ask_hint== "Yes" or ask_hint=="YES":
           if hint_count == 1 and random >=0 and random < 25:
               print(hint_3)
               guess= int(input("enter a number: "))
               guess_count += 1
               hint_count += 1
           elif hint_count==1 and random <=50 and random >=25:            
                print(hint_4)
                guess= int(input("enter a number: "))
                guess_count += 1
                hint_count += 1
           elif hint_count == 0:
               if random %2 == 0:
                   print(hint_1)
                   guess= int(input("enter a number: "))
                   guess_count += 1
                   hint_count +=1
               else:
                   print(hint_2)
                   guess= int(input("enter a number: "))
                   guess_count += 1
                   hint_count += 1
        else:
            guess= int(input("enter a number: "))
            guess_count += 1
    elif guess_count < 10:
        guess= int(input("enter a number: "))
        guess_count += 1
    else:
        out_of_guesses= True
if out_of_guesses:
    print("you loose")
else:
    print("you win")
            






    



        

            




            


        



  



    
    
