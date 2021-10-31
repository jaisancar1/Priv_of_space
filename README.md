# Priv_of_space
Autor/a: Jaime Sanchez Carmona

Este proyecto tiene como objetivo analizar los datos sobre la privatizacion del espaci, dado el siguiente dataset con URL(https://www.kaggle.com/davidroberts13/one-small-step-for-data), inicialmente este constaba de 15 columnas, sin em vargo se le ha  reducido a 8, y se le ha añadido 1 de tipo float con los datos sobrecua ntos billones de euros se han gastado en cada mision

## Estructura de las carpetas del proyecto
El proyecta en si cuenta de 2 carpetas diferentes:

       -/src: Esta contiene los diferentes modulos que compinen el proyecto:
           -spcace.py:donde se encuentrrabn las funciones principales
           -parseo.py. Modulo donde se encuentran difrentes funciones de parseo de datos
           test.py: Modulo con funciones para comprobar si el codigo es correcto
           
       -/dataproyect: En esta se encuentra el archivo csv con los datos sobre el proyecto
       
## Estrucuta del dataset
Cada fila recoge los datos del proyecta, ademas el dataset esta compuesto de 9 columnas con 9 tipos de datos diferentes:

* **company_name**: de tipo str, incluye el nombre de la compañia.
* **location**: de tipo str, represeta la localizaciondesde donde se realizo la mision.
* **status_rocket**: de tipo boolean, representa si el cohete sigue en activo o no
* **rocket**: de tipo int, representa el tipo de cohete
* **status mission**: de tipo boolean, nos dice si la mision fue un fracaso o un exito
* **country_of_launch**: de tipo str, nos da el pais de despegue
* **date**: de tipo date, representa la fecha de lanzamiento
* **time**: de tipo time, nos da la hora de lanzamiento
* **billions_spended**: de tipo float, nos dice la cantidad de billones de euros gastados en las misiones


## Tipos implementados
Para trabajar con los datros del dataset se ha implementado la siguiente tupla:
   
       Info = namedtuple('info','company_name, location, status_rocket, rocket, status_mission,\
                   country_of_launch, date, time, billions_spended')
     
ademas, los tipos de cada dato son los siguientes:
        
        [ Info(str, str, boolean, int, boolean, str, date, time, float,)]
        
## Funciones implementadas
En este proyecto se han implemenytado las siguientes funciones, las cuales estan ordenadas segun su modulo:

### Modulo space.py

  * **lee_fichero(fichero)**: lee los datos del fichero csv y devuelve una lista de tuplas de tipo Info con los datos del fichero. Para implementar esta función se han definido las siguientes funciones auxiliares en el [módulo "Parseo"]:
    * **parseo_status_mission(cadena)**: Función para convertir de cadena a booleano, co valores de true o false al estatus de la mision
    * **parseo_status_rocket(cadena)**: Función para convertir de cadena con valores de true o false al estado del cohete.

### Module Parseo.py

* **parsea_status_mission(cadena)**: Dada una cadena, devuelve 'Success'  si la cadena contiene el literal 'verdadero' (independientemente de si está escrtio en mayúsculas o minúsculas);  devuelve 'Failure' si la cadena contiente el literal 'falso'; y en cualquier otra caso, devuelve None.
* * **parsea_status_rocket(cadena)**: Dada una cadena, devuelve 'Status Active'  si la cadena contiene el literal 'verdadero' (independientemente de si está escrtio en mayúsculas o minúsculas);  devuelve 'Status Retired' si la cadena contiente el literal 'falso'; y en cualquier otra caso, devuelve None.

### Modulo test.py

    
        

