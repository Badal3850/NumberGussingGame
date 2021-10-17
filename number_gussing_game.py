import random
print("HEY! Let's play a game.\n Try to guess the Number.\n It can be anything between 1 to 100")
print("Menu:\n's' to start the game \n'q' to quit the game")
sstart=input()
if(sstart=='s'):
    n=random.randint(0, 100)
    while(True):
        try:
            a= input("Enter a number: ")
            if(a=='q'):
                break
            a=int(a)
            if(a>n):
                print("Try Entering a small number")
            elif(a<n):
                print("Try Entering a greater number")
            else:
                print("wahoooo! You did it @DUDE@")
        except Exception as e:
            print(e)
else:
    print("Invalid Choice")
    exit()
print("Thanks for playing")