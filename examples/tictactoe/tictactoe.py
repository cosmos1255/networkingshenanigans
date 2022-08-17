import text as t
import gameserver as gs 

def startGame():
    gs.initializeServer()

def entry():
    # print logo here
    # logo()

    cnt = 0

    # main game loop
    while (True):
        print(t.MAIN_MENU)
        opt = input("Select an option: ")

        if (opt == 's'):
            startGame()
            cnt = 0
        elif (opt == 'h'):
            print(t.HELP_MENU)
            cnt = 0
        elif (opt == 'q'):
            break
        else:
            if (cnt > 5):
                print("Too many incorrect options, quitting.")
                break
            print("Incorrect option, try again.")
            cnt += 1

if __name__=="__main__":
    entry()