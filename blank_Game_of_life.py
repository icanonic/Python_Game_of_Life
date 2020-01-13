from microbit import *

##Game of Life modes: “CONFIG” and “RUN” 
#CONFIG MODE (start configuration): 
	#Tilt: move the cursor 
	#Button A: enable or disable the cell under the cursor 
	#BUtton B: switch to RUN mode 
#RUN (universe evolve): 
	#Button B: switch to CONFIG mode

##”Draw” functions: set up the how bring the LED is 
#Empty cell: 0 
#Populated cell: 9 
#Empty cell with cursor on it: 4 
#Populated cell with cursor on it: 6 

##Important variables 
#mode tells us if we are in the Configuration Mode or the Run mode of the Game 
#x contains the x coordinate position of the cell 
#y contains the y coordinate position of the cell 
#cell_neighbours is equal to the number of neighbours a cell has 

##Important functions 
#evolve(universe) returns the evolved universe
#count_neighbours(universe, x, y) returns the number of neighbours of a cell 
#cell_state(universe, x, y) returns the current state of a cell 

def draw_cursor(universe, mode, x, y):
    #### 1. FIX! Check if mode is equal to “CONFIG”. 
    #Replace this 
        if cell_state(universe, x, y) == 0:
            display.set_pixel(x, y, 4)
        else:
            display.set_pixel(x, y, 6)
        
def draw_universe( universe ):
	####FIX! 2. Modify the range of y to have a minimum of 0 and a maximum of 5.
    for y in range(#Replace this):
	####FIX! 3. Modify the range of x to have a minimum of 0 and a maximum of 5.
        for x in range(#Replace this):
            display.set_pixel(x, y, universe[x + y * 5])
            
def evolve( universe ):
    next_universe = []
    for y in range(0, 5):
        for x in range(0, 5):
            ####FIX! 4. Call the function count_neighbours(universe, x, y) and assign the return value to the variable cell_neighbours 
            #Replace this
            cell_is_alive = cell_state(universe, x, y) == 1
            ####FIX! 5. Complete the if statement for underpopulation  
            if #Replace this:
                next_universe.append(0)
            ####FIX! 6. Complete the if statement for a healthy population  
            elif #Replace this:
                next_universe.append(9)
            ####FIX! 7. Complete the if statement for overpopulation
            elif #Replace this:
                next_universe.append(0)
            ####FIX! 8. Complete the if statement for reproduction
            elif #Replace this:
                next_universe.append(9)
            else:
                next_universe.append(0)
    return next_universe

    
def cell_state(universe, x, y):
    state = 1
    if universe[x + 5 * y] == 0:
        state = 0
    return state
    
def count_neighbours(universe, x, y):
    neighbours = -cell_state(universe, x, y)
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            neighbours += cell_state(universe, (x + dx) % 5, (y + dy) % 5)
    return neighbours

####FIX! 9. Initialize all 25 LEDS to have an LED brightness of 0. 
####Change the coordinates (3,2), (3,3), (3, 4) to have an LED brightness of 9.
current_universe = [#Replace this]

cursor_x = 2
cursor_y = 2
              
mode = "CONFIG"
display.scroll(mode)

while True:
    
####FIX! 10. What do we want to do with the mode is == “RUN”? 
####Reassign current_universe variable with the by passing in the current_universe into the evolve() function 
    if #Replace this:
        if button_b.is_pressed():
            mode = "CONFIG"
            display.scroll(mode)
            
            
    if mode == "CONFIG":
        
        accelerometer_xyz = accelerometer.get_values()
        if accelerometer_xyz[0] < -200:
            cursor_x = (cursor_x - 1) % 5
        if accelerometer_xyz[0] > 200:
            cursor_x = (cursor_x + 1) % 5
        if accelerometer_xyz[1] < -200:
            cursor_y = (cursor_y - 1) % 5
        if accelerometer_xyz[1] > 200:
            cursor_y = (cursor_y + 1) % 5
        
        if button_a.is_pressed():
            if cell_state(current_universe, cursor_x, cursor_y) == 0:
                current_universe[cursor_x + 5 * cursor_y] = 9
            else:  
                current_universe[cursor_x + 5 * cursor_y] = 0
                
        if button_b.is_pressed():
            mode = "RUN"
            display.scroll(mode)
           
           
    draw_universe( current_universe )
    draw_cursor(current_universe, mode, cursor_x, cursor_y) 
    sleep(1000)
