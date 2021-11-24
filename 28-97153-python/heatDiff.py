import numpy as np
import matplotlib.pyplot as plt
import sys


if __name__ == "__main__":
    import sys
    temper = int  # will hold input temp from user
    row_num = int
    col_num = int
    print ("Welcome to HeatDiff.\nHigher values will take longer to compute (up to a 2 minutes or so for 120).\nEnter temperature (range: 20-120):  ")
    temper = int(input())
    if (temper > 120 or temper < 20):
        print("Number out of range (20-120).  Please try again")
        sys.exit(0)
    row_num = temper + 2 #setting value to temper plus 2 extra rows (halo cells)
    col_num = temper + 2  #setting value to temper plus 2 extra rows (halo cells)
    state1 = np.zeros((row_num,col_num))
    state1[:,0] = float(temper)
    state2 = np.zeros((row_num,col_num))
    state2 = np.copy(state1)
    stopflag = False  #will be set to True when iterations reach 3000 or no change in state (whichever first)

    counter = int (0)
    message = ""
    while not stopflag:
        for i in range(1, row_num-1):    #ignores top and bottom row
            for j in range(1,col_num-1):  #ignores left and right column
                state2[i,j] = 0.25 * (state1[i - 1,j] + state1[i + 1, j] + state1[i,j - 1] + state1[i, j +1])

        if np.array_equal(state1,state2):
            stopflag = True
            message = "Halted on previous and next state equivalence reached"
        state1 = np.copy(state2)
        counter += 1
        if counter == 4000:
            stopflag = True
            message = "Halted on 4000 iterations reached"

    tempfloat = float(temper)
    eight = tempfloat / 8.0 #used for color calibration purposes
    tempfloat = float(temper)

    plt.figure(figsize= (6, 6), dpi = 80)

    size = int
    mark = ""
    if temper > 149:
        size = 3
        mark = '.'
    elif temper > 49:
        size = 4
        mark = '.'
    elif temper > 40:
        size = 4
        mark = 'o'
    else:
        size = 6
        mark = 'o'
    for i in range(1, row_num-1):    #ignores top and bottom row
        for j in range(1,col_num-1):  #ignores left and right column
            if state2[i, j] >= (tempfloat-eight):
                plt.plot([j], [i], marker = mark, color = 'darkred', markersize = size)
            elif state2[i, j] >= (tempfloat-2*eight):
                plt.plot([j], [i], marker = mark, color = 'red', markersize = size)
            elif state2[i, j] >= (tempfloat-3*eight):
                plt.plot([j], [i], marker = mark, color = 'orange', markersize = size)
            elif state2[i, j] >= (tempfloat-4*eight):
                plt.plot([j], [i], marker = mark, color = 'yellow', markersize = size)
            elif state2[i, j] >= (tempfloat-5*eight):
                plt.plot([j], [i], marker = mark, color = 'lawngreen', markersize = size)
            elif state2[i, j] >= (tempfloat-6*eight):
                plt.plot([j], [i], marker = mark, color = 'aqua', markersize = size)
            elif state2[i, j] >= (tempfloat-7*eight):
                plt.plot([j], [i], marker = mark, color = 'blue', markersize = size)
            else:
                plt.plot([j], [i], marker = mark, color = 'darkblue', markersize = size)
    plt.xlabel(message)

    plt.show()

    sys.exit(0)

'''

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
   temperature = float(input("Enter starting temperature: "))
   previousState = np.zeros([int(temperature)+2, int(temperature)+2])
   currentState = np.zeros([int(temperature)+2, int(temperature)+2])
   
   for i in range(0,int(temperature)+2):
      currentState[i,0] = temperature

   n = 0
   while n < 3000 and not np.array_equal(previousState, currentState):
      previousState = np.copy(currentState)
      for i in range(int(temperature)):       # columns
         i += 1
         for j in range(1,int(temperature)):     # rows
            currentState[i,j] = .25 * (previousState[i-1, j] + previousState[i+1, j] + previousState[i, j-1] + previousState[i, j+1])
            j += 1
      n += 1

   section = temperature // 8
   for i in range(1,int(temperature)):        # columns
      for j in range(1,int(temperature)):     # rows
         if currentState[i,j] <= section:
            plt.scatter(j,i,c="darkblue")
         elif section < currentState[i,j] < section*2:
            plt.scatter(j,i,c="blue")
         elif section*2 < currentState[i,j] < section*3:
            plt.scatter(j,i,c="aqua")
         elif section*3 < currentState[i,j] < section*4:
            plt.scatter(j,i,c="lawngreen")
         elif section*4 < currentState[i,j] < section*5:
            plt.scatter(j,i,c="yellow")
         elif section*5 < currentState[i,j] < section*6:
            plt.scatter(j,i,c="orange")
         elif section*6 < currentState[i,j] < section*7:
            plt.scatter(j,i,c="red")
         else:
            plt.scatter(j,i,c="darkred")

   plt.title("Heat Diffusion")
   plt.show()

'''

'''
# Name: Venkata Vadrevu
# FSU id: vv18d

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
import time


def distribute_heat(old_grid):
    new_grid = np.copy(old_grid)
    for i in range(1,len(new_grid) - 1):
        for j in range(1,len(grid) - 1):
            new_grid[i, j] = 0.25*(old_grid[i - 1, j] + old_grid[i + 1, j] + old_grid[i, j - 1] + old_grid[i, j+1])
    return new_grid


def equals(old_grid, new_grid):
    for i in range(1, len(old_grid) - 1):
        for j in range(1, len(old_grid) - 1):
            if old_grid[i, j] != new_grid[i, j]:
                return False
    return True


def plot_grid(grid):
    fig, ax = plt.subplots()
    y = np.array([[_ for __ in range(len(grid))] for _ in range(len(grid))])
    x = np.array([[__ for __ in range(len(grid))] for _ in range(len(grid))])
    C = grid
    cmap = col.ListedColormap(['darkblue', 'blue', 'aqua', 'lawngreen', 'yellow', 'orange', 'red', 'darkred'])
    ax.scatter(x, y, c=C, cmap = cmap)
    plt.show()


if __name__ == "__main__":
    # start time
    start = time.time()

    # get the temperature from the user
    temp = int(input("Enter the temperature: "))

    # laminar metal
    # created halo cells
    grid = np.array([[temp * 1.00 if i == 0 else 0.00 for i in range(temp + 2)] for j in range(temp + 2)])

    num_iter = 0
    MAX_ITER = 3000
    while num_iter < MAX_ITER:
        old_grid = np.copy(grid)
        grid = distribute_heat(old_grid)
        if equals(old_grid, grid):
            break
        num_iter += 1

    show_grid = np.array([[grid[i][j] for j in range(1, len(grid) - 1)] for i in range(1, len(grid) - 1)])


    #end time
    end = time.time()

    time_taken = end - start
    print("Time taken ", time_taken, "seconds")

    plot_grid(show_grid)
'''