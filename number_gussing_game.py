import random
print("HEY! Let's play a game.\n Try to guess the Number.\n It can be anything between 1 to 100")
print("Menu:\n's' to start the game \n'q' to quit the game")
nummber=random.randint(0, 100)
total_no_of_guess=5
gussed_number=0
while(gussed_number!=nummber):
    total_no_of_guess -=1
    gussed_number=int(input("Enter a number: "))
    if(total_no_of_guess==0):
        print("YOU LOST")
        exit()
    else:
        if(gussed_number>nummber):
            print("Try entering a smaller Number")
        elif(gussed_number<nummber):
            print("Try entering larger number")
        else:
            print("Congratulation !! YOU WON")
    print(f"Number of guess left{total_no_of_guess}: ")
