# importing packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import time
from multiprocessing import Pool
import os



def main(temp):

    # Creating halo cells & create as grid
    state = np.array([[temp * 1.00 if i == 0 else 0.00 for i in range(temp + 2)] for j in range(temp + 2)])

    num_iteration = 0
    max_iteration_limit = 3000
    cpu_cores = os.cpu_count() # this give no of cpu in the system
    # Multiprocessing 
    pool = Pool(processes=cpu_cores)

    while num_iteration < max_iteration_limit:
        state_1 = np.copy(state)
        # calculating in async method
        result = [pool.apply_async(calculate_temp, args=(i,state_1)) for i in range(1, temp+1)]
        for j in result:
            y, arr = j.get()
            for i in range(1, temp+1):
                state[i, y] = arr[i - 1]

        if equals(state, state_1):
            break
        else:
            num_iteration += 1

    pool.close()

    return state


def calculate_temp(y, state_1):
    result = []
    for x in range(1, len(state_1) - 1):
        result.append(0.25*(state_1[x - 1, y] + state_1[x + 1, y] + state_1[x, y - 1] + state_1[x, y + 1]))
    return y,result


def equals(state_1, state):
    for i in range(len(state_1)):
        for j in range(len(state_1)):
            if state_1[i, j] != state[i, j]:
                return False
    return True



def plot_state(state):
    fig, ax = plt.subplots()
    y = np.array([[_ for __ in range(len(state))] for _ in range(len(state))]) # creating x axis
    x = np.array([[__ for __ in range(len(state))] for _ in range(len(state))]) # creating y axis
    C = state
    cmap = mcolors.ListedColormap(['darkblue', 'blue', 'aqua', 'lawngreen', 'yellow', 'orange', 'red', 'darkred'])
    ax.scatter(x, y, c=C, cmap = cmap)
    plt.show()


if __name__ == "__main__":
    # Intialize time
    start = time.time()
    # Get input temperature from user
    temp = int(input("Enter the temperature: "))
    # call Function
    state = main(temp)

    # Calculation end time
    end = time.time()

    time_taken = end - start
    print(f"Total time taken to complete {time_taken} seconds")

    # using list comprehension to create a list of all the values in the state
    show_state = np.array([[state[i][j] for j in range(1, len(state) - 1)] for i in range(1, len(state) - 1)])

    # Plotting the state
    plot_state(show_state)