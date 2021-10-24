from backend.funcs import process_input

if __name__ == '__main__':

    while 1:
        grid_str = input("Enter the upper right corner coordinates of the grid: ")
        if len(grid_str) == 3 and grid_str[1] == ' ':  # Simple misinput check, could be much more sophisticated
            break
        print(
            "The inputted format was wrong. Please follow the format \"x-position y-position\"")

    init_strs = []
    command_strs = []
    i = 1

    while 1:
        while 1:
            init_str = input("Enter the initial coordinates and orientation of rover number " + str(i) + ": ")
            if len(init_str) == 5 and init_str[1] == init_str[
                3] == ' ':  # Simple misinput check, could be much more sophisticated
                break
            print(
                "The inputted format was wrong. Please follow the format \"x-position y-position orientation\"")

        init_strs.append(init_str)
        command_strs.append(input("Enter the movement commands for rover number " + str(i) + ": "))
        if input("Add another rover? Type \"yes\" or \"no\": ") != "yes":
            break
        i += 1



    print("\nOutputs:")
    process_input(grid_str, init_strs, command_strs)
