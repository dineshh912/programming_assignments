# importing packages 
import numpy as np
import matplotlib.pyplot as plt # Visualization library
import matplotlib.colors as mcolors
import time # for timing


def main(temp):
    try:
        # Creating halo cells & create as grid
        state = np.array([[temp * 1.00 if i == 0 else 0.00 for i in range(temp + 2)] for j in range(temp + 2)])

        num_iteration = 0
        max_iteration_limit = 3000
        while num_iteration < max_iteration_limit:
            state_1 = np.copy(state)
            # calculating temp
            state = calculate_temp(state_1)
            if equals(state_1, state):
                break
            num_iteration += 1
       
        return state

    except Exception as e:
        print(e)


def calculate_temp(state_1):
    state_2 = np.copy(state_1)
    for i in range(1,len(state_2) - 1):
        for j in range(1,len(state_1) - 1):
            state_2[i, j] = 0.25*(state_1[i - 1, j] + state_1[i + 1, j] + state_1[i, j - 1] + state_1[i, j+1])
    return state_2


def equals(state_1, state):
    for i in range(1, len(state_1) - 1):
        for j in range(1, len(state_1) - 1):
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