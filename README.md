# ApplusProject
Project for Applus+ IDIADA. Capable of simulating multiple robotic rover's movements in an established grid from a series of initial conditions and movement commands.

## Overview
The assignment read as follows:
> A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth. A rover’s position and location is represented by a combination of x and y co- ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North. In order to control a rover, NASA sends a simple string of letters. The possible letters are ‘L’, ‘R’ and ‘M’. ‘L’ and ‘R’ makes the rover spin 90 degrees left or right respectively, without moving from its current spot. ‘M’ means move forward one grid point, and maintain the same heading. Assume that the square directly North from (x, y) is (x, y+1).


 
## Preliminary processes

Since the program does not use any library, there is no need to install any packages prior to running the code (the *requirements.txt* file has been added just as a formality, but it is empty). The process starts by running the *main.py* file present in the *ApplusProject* directory.


## Funcionamiento



### Inputs

The assignment established that the input should be given as 

### Outputs
**URL**: .../post-data/

**Método**: DELETE

**Datos a incluir**: Ninguno

**Descripción**: Se elimina toda la información de la base de datos

**Output (en caso de éxito)**: *"Todos los datos han sido eliminados"*

### Consultar piloto
**URL**: .../get-pilot/?name=*piloto a consultar*

**Método**: GET

**Datos a incluir**: Nombre del piloto a consultar, como parte de la URL (p.ej. http://127.0.0.1:8000/get-pilot/?name=Cooke Rivers) o en los *query parameters* de la *request* (KEY=name, VALUE=Cooke Rivers) (ambos métodos son equivalentes)

**Descripción**: Devuelve, en formato JSON, la información requerida al respecto de todas las carreras del piloto seleccionado (añadiendo además su posición en cada una de ellas). A su vez, la API informa adecuadamente en caso de que el piloto no figure en la base de datos, así como del caso en que la base de datos esté completamente vacía.

**Output (en caso de éxito)**:
```
{
    "Nombre": "Cooke Rivers",
    "ID": "5fd7dbd8ce3a40582fb9ee6b",
    "Edad": 23,
    "Equipo": "PROTODYNE",
    "Foto": "http://placehold.it/64x64",
    "Carreras": {
        "Race 0": {
            "Posición": 13,
            "Puntos": 0,
            "Tiempo Total": "1:50:41.257000",
            "Mejor Vuelta": "0:08:04.951000"
        },
        "Race 1": {
            "Posición": 12,
            "Puntos": 0,
            "Tiempo Total": "1:50:08.934000",
            "Mejor Vuelta": "0:08:12.974000"
        },
        ...
 }
```

### Consultar carrera
**URL**: .../get-race/?name=*carrera a consultar*

**Método**: GET

**Datos a incluir**: Nombre de la carrera a consultar, como parte de la URL (p.ej. http://127.0.0.1:8000/get-race/?name=Race 1) o en los *query parameters* de la *request* (KEY=name, VALUE=Race 1) (ambos métodos son equivalentes)

**Descripción**: Devuelve, en formato JSON, la información requerida al respecto de la actuación en la carrera seleccionada de todos los pilotos presentes en la base de datos (ordenados por su posición en la misma). A su vez, la API informa adecuadamente en caso de que la carrera no figure en la base de datos, así como del caso en que la base de datos esté completamente vacía.

**Output (en caso de éxito)**:
```
[
    {
        "Nombre": "Kitty Farmer",
        "Datos de su carera": {
            "Posición": 1,
            "Puntos": 25,
            "Tiempo Total": "1:41:10.653000",
            "Mejor Vuelta": "0:08:01.389000"
        }
    },
    {
        "Nombre": "Merle Rhodes",
        "Datos de su carera": {
            "Posición": 2,
            "Puntos": 18,
            "Tiempo Total": "1:41:59.213000",
            "Mejor Vuelta": "0:08:10.802000"
        }
    },
    ...
]
```

### Consultar clasificación general
**URL**: .../get-list-all/

**Método**: GET

**Datos a incluir**: Ninguno

**Descripción**: Devuelve la clasificación de todos los pilotos tras el cómputo de los puntos obtenidos en cada una de sus carreras, así como la información adicional requerida para cada uno de ellos.

**Output (en caso de éxito)**:
```
[
    {
        "name": "White Elliott",
        "total_time": "17:51:21.571000",
        "total_pts": 90
    },
    {
        "name": "Kitty Farmer",
        "total_time": "17:54:10.571000",
        "total_pts": 81
    },
    {
        "name": "Cotton Sosa",
        "total_time": "18:10:56.603000",
        "total_pts": 77
    },
    ...
]
```

