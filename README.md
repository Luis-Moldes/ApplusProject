# ApplusProject
Project for Applus+ IDIADA. Capable of simulating multiple robotic rover's movements in an established grid from a series of initial conditions and movement commands.

## Overview
The assignment read as follows:
> A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth. A rover’s position and location is represented by a combination of x and y co- ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North. In order to control a rover, NASA sends a simple string of letters. The possible letters are ‘L’, ‘R’ and ‘M’. ‘L’ and ‘R’ makes the rover spin 90 degrees left or right respectively, without moving from its current spot. ‘M’ means move forward one grid point, and maintain the same heading. Assume that the square directly North from (x, y) is (x, y+1).

The program must obtain the final position of these rovers from the inputted position and movement information. This will be performed by sequentially reading the movement commands for each of the rovers, updating either the position or the orientation at each given step. 

Two different ways of inputting the initial conditions and commands have been implemented: a more direct one where an *input.txt* file is directy read, and a more UI-like one where the user inputs each lines as reponses to queries in the command prompt. The exact format of the inputs and outputs will be laid out in their corresponding sections. 


## Preliminary processes

Since the program does not use any library, there is no need to install any packages prior to running the code (the *requirements.txt* file has been added just as a formality, but it is empty). The process starts by running either the *main.py* or the *main_readFile.py* files present in the *ApplusProject* directory.


## Structure and performance

Two different "Main" scripts have been implemented, providing the aforementioned options for providing the program the necessary information: *main.py* and *main_readFile.py*. Both of them are very simple error-checking files that do not carry out any of the calculations themselves: the actual algorithms are located in the _funcs.py_ script, which is called by both "Main" scripts. This makes it so that the outputs of both input options are identical, following the assignment's requirements. The exact format of their inputs will be laid out in the next section.

The _funcs.py_ script, in turn, contains two different functions: 

* **_rover_route_** is the function that actually tracks a single rover's path, by sequentially updating its position and orientation, using an approach that resembles the use of vectors. Additionally, it oversees that the rover does not leave the established grid, returning a warning if it does.

* **_process_input_** is only in charge of feeding _rover_route_ the correct information, giving it the rovers one by one and doing some format preprocessing with what it receives from the main script.

This modular approach for the program's structure allows for more flexibility in case new implementations need to be performed.

### Inputs

As said, there are two scripts with which the program can be launched, which provide different options regarding the input method:

* **_main.py_** uses the console to communicate with the user, prompting him/her to input each of the required lines of information. After correctly inputting each rover's information, the option of either adding another rover or starting the calculations will be given to the user. This method allows for checking for input errors before the process starts, as can be seen in the example below:

```
Enter the upper right corner coordinates of the grid: 5,5
The inputted format was wrong. Please follow the format "x-position y-position"
Enter the upper right corner coordinates of the grid: 5 5
Enter the initial coordinates and orientation of rover number 1: 1 2 N
Enter the movement commands for rover number 1: LMLMMLLM
Add another rover? Type "yes" or "no": yes
Enter the initial coordinates and orientation of rover number 2: 13S
The inputted format was wrong. Please follow the format "x-position y-position orientation"
Enter the initial coordinates and orientation of rover number 2: 1 3 S
Enter the movement commands for rover number 2: LM
Add another rover? Type "yes" or "no": no

Outputs:
...
```

* **_main_readFile.py_** will simply read the _input.txt_ file located in the project directory. This allows for a more direct way of starting the process. Each line of the _input.txt_ corresponds to each of the questions prompted in the other method, following the structure established by the assignment:

```
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
5 5 S
MMRLRLLLMM
3 4 E
LRLRLRLR
```


### Outputs

The output is printed in the console, following the format established by the assignment. In case of there being no errors present, the output should be a line for each inputted rover containing its final position and orientation, for example:

```
Outputs:
1 3 N
5 1 E
5 4 N
3 4 E
```

Moreover, there is a series of error messages that can be shown in case of something going awry. If one of the rovers leaves the grid, that rover's output line will provide information regarding this issue:

```
Outputs:
1 3 N
5 1 E
The rover went off the established grid at command number 11, at position [5 6]
3 4 E
```

There are also warnings in case the input was incorrectly given, such as:
```
Outputs:
1 3 N
There was an incorrect input at command number 6
5 5 N
3 4 E
```
```
The inputted format for the initial conditions was wrong. Please follow the format "x-position y-position orientation"
```

