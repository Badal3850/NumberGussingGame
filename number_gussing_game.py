import random
print("HEY! Let's play a game.\n Try to guess the Number.\n It can be anything between 1 to 100")
print("Menu:\n's' to start the game \n'q' to quit the game")
menu_input=input("")
if menu_input == 's':
    nummber=random.randint(0, 100)
    totalNoOfGuess=5
    gussed_number=0
    while(gussed_number!=nummber):
        totalNoOfGuess -=1
        gussed_number=int(input("Enter a number: "))
        if(totalNoOfGuess==0):
            print("YOU LOST")
            exit()
        else:
            if(gussed_number>nummber):
                print("Try entering a smaller Number")
            elif(gussed_number<nummber):
                print("Try entering larger number")
            else:
                print("Congratulation !! YOU WON")
        print(f"Number of guess left{totalNoOfGuess}: ")
elif menu_input == 'q':
    print("Have a good day ! See you Soon")
