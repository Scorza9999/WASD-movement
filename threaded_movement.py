import threading # library used to implemet threading
import time #library used to create delays
import keyboard # library used to check that a key was pressed

go_up = go_down = go_right = go_left = hitwall = False #setting up variables to detect movement

def checkUp():
    while True: # infinite loop
        if keyboard.is_pressed('w'): # check if key w is pressed 
            global go_up # aquires global go_up variable
            go_up = True # sets the value to True
            print ('up') # not mandatory
            go_up = False # sets the value to False
            time.sleep(0.2) # Delay time to prevent spamming
        elif hitwall:
            return # preventive set up of the way to stop threads when player hits wall

def checkDown():
    while True:
        if keyboard.is_pressed('s'): # check if key s is pressed 
            global go_down # aquires global go_down variable
            go_down = True # sets the value to True
            print ('down') # not mandatory
            go_down = False # sets the value to False
            time.sleep(0.2) # Delay time to prevent spamming
        elif hitwall:
            return # preventive set up of the way to stop threads when player hits wall

def checkLeft():
    while True:
        if keyboard.is_pressed('a'): # check if key a is pressed 
            global go_left # aquires global go_left variable
            go_left = True # sets the value to True
            print ('left') # not mandatory
            go_left = False # sets the value to False
            time.sleep(0.2) # Delay time to prevent spamming
        elif hitwall:
            return # preventive set up of the way to stop threads when player hits wall

def checkRight():
    while True:
        if keyboard.is_pressed('d'): # check if key d is pressed 
            global go_right # aquires global go_right variable
            go_right = True # sets the value to True
            print ('right') # not mandatory
            go_right = False # sets the value to False
            time.sleep(0.2) # Delay time to prevent spamming
        elif hitwall:
            return # preventive set up of the way to stop threads when player hits wall

threads = [] # array to kepping track of the different threads

checkUpThread = threading.Thread(target=checkUp) # inizializing the thread passing check{direction} as a parameter
threads.append(checkUpThread) #append the thread to the array

checkDownThread = threading.Thread(target=checkDown) # inizializing the thread passing check{direction} as a parameter
threads.append(checkDownThread) #append the thread to the array

checkLeftThread = threading.Thread(target=checkLeft) # inizializing the thread passing check{direction} as a parameter
threads.append(checkLeftThread) #append the thread to the array

checkRightThread = threading.Thread(target=checkRight) # inizializing the thread passing check{direction} as a parameter
threads.append(checkRightThread) #append the thread to the array

checkUpThread.start() #starting threads' routines
checkDownThread.start()
checkLeftThread.start()
checkRightThread.start()

# whitout the hitwall the threads will never end and this part will be never executed

print(threads) # not mandatory

checkUpThread.join() # whaits for the thread to finish the process and 
threads.remove(checkUpThread) # than deletes it from the array (this is currently non possible because the while loop
checkDownThread.join() # doesn't end whitout implementig the hitwall)
checkLeftThread.join()
threads.remove(checkLeftThread)
checkRightThread.join()
threads.remove(checkRightThread)
