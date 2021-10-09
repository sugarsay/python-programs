#Creates a random number generator that allows
#the user to attempt 3 times. After each attempt
#the program must tell the user if the guess is
#too high or low.

import random
#Generate random number
number=random.randint(1,10)
#print(number) #Added for debugging to display random value
#Create counter and take user input to start program
tries=0
guess=int(input("Please enter a number(1-10):"))
#Loops for attempts
while(tries!=2 and guess!=number):
    #If statement to decide if the number guessed what high or low
    if guess>=number:
        print("Too High")
    else:
        print("Too Low")
    #Counter
    tries+=1
    #Take User input
    guess=int(input("Please enter a number:"))
#Prints if correct welcome and if incorrect max attempts reached
if (guess==number):
    print("Congrats you guessed the right number")
else:
    print("Max attempts reached")
    print("The number was ",number)
