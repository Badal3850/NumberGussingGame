import random
print("HEY! Let's play a game.\n Try to guess the Number.\n It can be anything between 1 to 100")
print("Menu:\n's' to start the game \n'q' to quit the game")
menu_input = input("")
if menu_input == 's':
    nummber = random.randint(0, 100)
    TOTAL_NUMBER_OF_GUESS = 5
    GUESSED_NUMBER = 0
    while GUESSED_NUMBER != nummber:
        TOTAL_NUMBER_OF_GUESS -= 1
        GUESSED_NUMBER = int(input("Enter a number: "))
        if TOTAL_NUMBER_OF_GUESS == 0:
            print("YOU LOST")
            exit()
        else:
            if GUESSED_NUMBER > nummber:
                print("Try entering a smaller Number")
            elif GUESSED_NUMBER < nummber:
                print("Try entering larger number")
            else:
                print("Congratulation !! YOU WON")
        print(f"Number of guess left{TOTAL_NUMBER_OF_GUESS}: ")
elif menu_input == 'q':
    print("Have a good day ! See you Soon")
