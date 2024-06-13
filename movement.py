import keyboard #library used to check that a key was pressed
go_up = False
go_down = False
go_right = False
go_left = False
#boolean variables used to check for the movement
print("Use WASD to move")
while True: #used an infinite loop that cannot be broken
    if keyboard.is_pressed ('w'): #statement used to change the boolean value of go_up and therefore move something up
        go_up = True
        print ('up') #not mandatory
        go_up = False
    elif keyboard.is_pressed ('s'): #statement used to change the boolean value of go_down and therefore move something down
        go_down = True
        print ('down') #not mandatory
        go_down = False
    elif keyboard.is_pressed ('a'): #statement used to change the boolean value of go_left and therefore move something left
        go_left = True
        print ('left') #not mandatory
        go_left = False
    elif keyboard.is_pressed ('d'): #statement used to change the boolean value of go_right and therefore move something right
        go_right = True
        print ('right') #not mandatory
        go_right = False
#you can also add a delay, if you want