#BBC Game of Life Program

# When displayed to a user, live cells will appear as 1, and dead cells are represented by a 0
# After setting initial variables for size, the user presses enter to move to the next generation
# If the generation doesn't change, or contains no live cells, the game of life is over
# When the game of life is over, enter is inputted to create a new random seed in the grid, and the game of life continues
# Messages are outputted when this happens

#Random is imported as it is needed for random seeding
import random

#Subroutine for seeding the cells initial values
#Each cell has a 50% chance of starting live or not
def seed_cells():
    for i in range(y_size):
        for j in range(x_size):
            if random.random() > 0.5:
                cells[i][j] = 1
            else: cells[i][j] = 0

#Function to calculate number of live cells
def live_cell_count():
    live_cells = 0
    for i in range(y_size):
        for j in range(x_size):
            if cells[i][j] == 1:
                live_cells += 1
    return live_cells

#Subroutine to display Cells
def display_cells():
    for i in range(y_size):
        for j in range(x_size):
            #Displays cells in format [y][x]
            print(cells[i][j], end =" ")
        print("")

#Count how many neighbour cells are live
#Initial if statements for each check are required so that locations outside the array are not checked
def count_neighbour_cells(y, x):
    neighbour_cells = 0
    if x > 0 and y > 0:
        if cells[y - 1][x - 1] == 1: neighbour_cells += 1
    if y > 0:
        if cells[y - 1][x] == 1: neighbour_cells += 1
    if x < x_size-1 and y > 0:
        if cells[y - 1][x + 1] == 1: neighbour_cells += 1
    if x > 0:
        if cells[y][x - 1] == 1: neighbour_cells += 1
    if x < x_size-1:
        if cells[y][x + 1] == 1: neighbour_cells += 1
    if x > 0 and y < y_size-1:
        if cells[y + 1][x - 1] == 1: neighbour_cells += 1
    if y < y_size-1:
        if cells[y + 1][x] == 1: neighbour_cells += 1
    if x < x_size-1 and y < y_size-1:
        if cells[y + 1][x + 1] == 1: neighbour_cells += 1
    return neighbour_cells

#Function for comparing the contents of 2 arrays, if the returned value is 0 they are the same
def compare_arrays(array1, array2):
    difference = 0
    for i in range(y_size):
        for j in range(x_size):
            if array1[i][j] != array2[i][j]: difference += 1
    return difference

#Although the grid is supposed to be infinite, only a finite sized grid can be used and displayed
#The user selects the size of this within these while loops
#A try...except loop is used so the user cannot input an invalid input
while True:
    try:
        x_size = int(input('Define size of grid (x axis):'))
        if x_size > 0:
            break
        else:
            print("Number must be greater than 0, please try again.")
    except ValueError:
        print("Invalid input, please try again.")

while True:
    try:
        y_size = int(input('Define size of grid (y axis):'))
        if y_size > 0:
            break
        else:
            print("Number must be greater than 0, please try again.")
    except ValueError:
        print("Invalid input, please try again.")

# Declares the array cells and live_neighbours, all their values are initialised at 0
cells = [[0 for i in range(x_size)] for j in range(y_size)]
live_neighbours = [[0 for i in range(x_size)] for j in range(y_size)]
old_cells = [[0 for i in range(x_size)] for j in range(y_size)]


seed_cells() # Initial seeding values
while True:

    display_cells()
    input("Press enter to go to the next generation.")
    # First loop to see the number of live neighbours, completed first so that no changes to cells occur until all numbers of cells completed
    for i in range(y_size):
        for j in range(x_size):
            # Sets each value in array live_neighbours to the number of live neighbours for each corresponding cell
            live_neighbours[i][j] = count_neighbour_cells(i, j)
            # Sets old_cells to the value of cells before cells is changed to the next generation
            old_cells[i][j] = cells[i][j]

    # Second loop to modify any cells for the next generation
    for i in range(y_size):
        for j in range(x_size):
            if live_neighbours[i][j] == 3: cells[i][j] = 1  # Scenario 4 and part of 3
            if live_neighbours[i][j] == 2: cells[i][j] = cells[i][j]  # Other part of scenario 3
            if live_neighbours[i][j] < 2: cells[i][j] = 0  # Scenario 1
            if live_neighbours[i][j] > 3: cells[i][j] = 0  # Scenario 2

    # Check for scenario 0 or 5
    if live_cell_count() == 0:
        display_cells()
        input("No more live cells. The game of life is over. Press enter to create a new seed.")
        seed_cells()

    # Check if there is no change from previous generation
    if compare_arrays(old_cells, cells) == 0:
        display_cells()
        input("No change from previous generation, the game of life will no longer change. Press enter to create a new seed.")
        seed_cells() # Seeds the cells again
