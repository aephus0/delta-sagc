import keyboard
import os
import pickle
import ctypes
from gamedata import charvals
from gamedata import worldvals


ctypes.windll.kernel32.SetConsoleTitleW("Delta Sagc")

# Boolean for running condition.
srunning = False
freshinstall = None

# Defaults the worldstate to standard values 
wrld = worldvals(1, 1, 1)


#Checks for the gamestate file to verify the state of the installation.
def gamestate():
    global freshinstall
    if os.path.isfile('gamestate'):
        freshinstall = False
    if not os.path.isfile('gamestate'):
        freshinstall = True
        with open('gamestate', 'w') as f:
            pass

# Checks to see if savedata is present and if not it creates it accordingly.
def startingchecks():
    gamestate()
    if os.path.isfile('savedata') and freshinstall == False:
        global mc, srunning, wrld
        try:
            with open('savedata', 'rb') as loadedata:
                mc = pickle.load(loadedata)
                wrld = pickle.load(loadedata)
        except FileNotFoundError:
            print("The file cannot be loaded and could be corrupted.")
            
    if os.path.isfile('savedata') and freshinstall == True:
        print("This appears to be a fresh install of the game, however previous savedata has been found. Do you wish to try and load the previous data?")
        while True:
            try:
                if keyboard.is_pressed('y'):
                    keyboard.send('backspace')
                    try:
                        with open('savedata', 'rb') as loadedata:
                            mc = pickle.load(loadedata)
                            wrld = pickle.load(loadedata)
                            break
                    except FileNotFoundError:
                        print("The file cannot be loaded and could be corrupted.")
                        break
                if keyboard.is_pressed('n'):
                    keyboard.send('backspace')
                    break
            except KeyboardInterrupt:
                break
    if not os.path.isfile('savedata') and freshinstall == True:
        print("Save Data not found. Do you wish to create new Save Data?")
        while True:
            try:
                if keyboard.is_pressed('y'):
                    keyboard.send('backspace')
                    
                    mc = charvals("None", None, None, None, None)
                    dumpsavedata()
                    break
                if keyboard.is_pressed('n'):
                    keyboard.send('backspace')
                    print("Game cannot be loaded without Save Data. Exiting the game...")
                    srunning = False
                    break
            except KeyboardInterrupt:
                break

# Initializes the character with the parameters specified.
def charactercreation():
    
    return charvals(input("Character name: "), health=100, level=1, dex=1,str=1)

# Dumps the character data to the savefile
def dumpsavedata():
    try:
        with open('savedata', 'wb') as loadedata:
            pickle.dump(mc,loadedata)
            pickle.dump(wrld, loadedata)
    except FileNotFoundError:
        print("An error occurred during the process...")

# Sets srunning to true and allows the game loop to begin.
def setgameconditionrun():
    global srunning
    if srunning == False:
       srunning = True
    else:
        pass

def clear():
    os.system('cls')
# Prints the main menu and allows for either starting or exiting or loading the game.
def mainMenu():
    clear()
    print("*MAIN MENU*\n")


    print("F1 - Start Game")
    print("F2 - Exit Game")
    print("F3 - Load Game")
    
    while True:
        try:
            global srunning, mc
            if keyboard.is_pressed('F1'):
                clear()
                print("Starting a new game...")
                setgameconditionrun()
                mc = charactercreation()
                break
            if keyboard.is_pressed('F2'):
                clear()
                print("Closing the game...")
                
                srunning = False
                break
            if keyboard.is_pressed('F3'):
                break

        except KeyboardInterrupt:
            srunning = False
            break


startingchecks()
mainMenu()
print(mc.name)
print(wrld.room)

# Main Game loop.
while srunning:
    dumpsavedata()
    
    break
