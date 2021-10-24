def process_input(grid_str, init_strs, command_strs):
    """
    process_input is in charge of preprocessing the inputted string lists and recursively calling the
    rover_route function, feeding it the correct formats.

    :grid_str: string containing the grid information
    :init_strs: list of the initial parameter strings for each of the inputted rovers
    :command_strs: list of the movement commands strings for each of the inputted rovers
    :return: the output is given through the printed lines
    """

    grid = [int(grid_str[0]), int(grid_str[-1])]

    for i in range(len(init_strs)):
        print(rover_route([int(init_strs[i][0]), int(init_strs[i][2])], init_strs[i][4], command_strs[i], grid))


def rover_route(pos, car_ini, moves, grid):
    """
    rover_route is the core of the program: it simulates the movement of a rover through the grid from its starting
    position in concordance with the movement commands given. This is done in a recursive way, command by command,
    using an approach that resembles the use of vectors. Additionally, it oversees that the rover does not leave the
    grid, returning a warning if it does.

    :pos: list with two integers, the initial coordinates of the rover
    :car_ini: one character string, with the cardinal initial direction
    :moves: string containing the letters of the movement commands
    :grid: list with two integers, the coordinates of top right corner of the grid
    :return: string with the final position and cardinal orientation of the rover. In case the rover went off the grid,
    the return string is a message informing of the error with the position where the rover left the grid
    """

    # These two lists relate the cardinal letters with the numerical direction they symbolize on the grid, being in the
    # same index. This allows the use of the ".index()" function to move between the two. Moreover, they are ordered so
    # that, for a given index "i", "i+1" would mean a rotation to the right, and "i-1" would represent a rotation to the
    # left

    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    cars = ['N', 'E', 'S', 'W']


    dir_index = cars.index(car_ini)
    dir = dirs[dir_index]

    #Traverses the whole command string, updating the position (pos) or the direction (dir) at each step
    i = 0
    while i < len(moves):
        letter = moves[i]
        if letter == 'M':
            # For each of the axes, the position is checked and updated
            for j in [0, 1]:
                pos[j] += dir[j]

                # Checks to see if it went off the grid
                if pos[j] > grid[j] or pos[j] < 0:
                    return 'The rover went off the established grid at command number ' + str(
                        i + 1) + ', at position [' + str(pos[0]) + ' ' + str(pos[1]) + ']'


        elif letter == 'R':
            # Using the modulo operator allows to traverse the list indexes in a looping manner.
            dir_index = (dir_index + 1) % 4
            dir = dirs[dir_index]

        elif letter == 'L':
            dir_index = (dir_index - 1) % 4
            dir = dirs[dir_index]

        # In case there was an error in the movement string
        else:
            return 'There was an incorrect input at command number ' + str(i + 1)

        i += 1

    return str(pos[0]) + ' ' + str(pos[1]) + ' ' + str(cars[dirs.index(dir)])
