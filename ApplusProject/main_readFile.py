from backend.funcs import process_input

if __name__ == '__main__':
    f = open('input.txt', 'r').read().splitlines()

    if len(f[0]) != 3 and f[0][1] != ' ':  # Simple misinput check, could be much more sophisticated
        print(
            "The inputted format for the grid data was wrong. Please follow the format \"x-position y-position\"")

    elif len([1 for i in f[1::2] if len(i)!=5])!=0:
        print(
            "The inputted format for the initial conditions was wrong. Please follow the format "
            "\"x-position y-position orientation\"")
    else:
        print("\nOutputs:")
        process_input(f[0], f[1::2], f[2::2])
