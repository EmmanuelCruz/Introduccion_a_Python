# Introducción a Python
## Emmanuel Cruz Hernández.

----

### Descripción
Bloques de ejercicios del curso ***Master en Python***. Bloques de ejecicios de la introducción a Python.

En esta unidad introductoria se explican y hacen ejercicios de los siguientes temas:

* Introducción general al lenguaje de programación: Python
* Variables y tipos de datos.
* Operadores.
* Entrada y salida de datos.
* Estructuras de control.
* Funciones.
* Listas.
* Diccionarios.
* Sets.

----

### Otros temas

#### Módulos
Son funcionalidades ya hechas para reutilizar en Python. Todos los módulos disponibles en Python se pueden encontrar en su [Documentación](https://docs.python.org/3/py-modindex.html).

También se pueden consultar y descargar módulos externos en internet, así como crearlos. La definición para importar un módulo

        import modulo

En caso de importar funciones específicas, se puede usar la siguiente sintaxis:

        from modulo import func1, func2, ..., funcN

Si se necesita importar cada función en un módulo sin necesidad de tener un objeto, se puede hacer con la sintaxis

        from modulo import *

Los módulos también se pueden organizar en paquetes. Estos se caracterízan por tener un directorio específico con los módulos usados en el paquete y el paquete está dado por el archivo

        __init__.py

Algunos paquetes pueden ser descargados con _pip_.

#### Ficheros en Python
Se utiliza un módulo llamado _io_, en particular para recibir un archivo de datos se utiliza la función _open_.

        archivo = open("ruta/del/archivo.extension", "a+")

Con la ruta absoluta se puede usar la función Path().absolute()

        import pathlib
        ruta = str(pathlib.Path().absolute()) + "ruta/absoluta/archivo.extension"
        archivo = open(ruta, "a+")

Para escribir un archivo, se utiliza el método _write_.

        archivo.write("Mensaje a escribir")

Para cerrar el archivo después de modificarlo, se usa el método _close_, esto **es muy importante**.

        archivo.close()

Para leer contenido, sólo se utiliza el método read().

        contenido = archivo.read()

Con el módulo _shutil_ se dan más opciones de manejo de archivos, tal como copiar, eliminar, mover.
* Copiar

        shutil.copyfile("ruta_original/nombre1", "ruta_nueva/nombre2")

* Mover o renombrar

        shutil.move("ruta_original/nombre1", "ruta_nueva/nombre2")
    
* Eliminar

        import os
        os.remove("ruta/arhivo/nombre")

* Crear un directorio

        os.mkdir("./Nombre_Directorio")

* Eliminar un directorio

        os.rmdir("./Nombre_Directorio")

* Copiar

        os.copytree("Ruta1", "Ruta2")

#### Manejo de Excepciones
El manejo de excepciones se puede tratar dentro de un bloque _try_. A diferencia de los bloques _try catch_, aquí no existe _catch_, pero su equivalente es _except_. 

        try:
            ...
        except:
            ...
        finally:
            ...

El bloque _finally_ se ejecuta en todos los casos, si ocurre o no un error. Para el manejo de excepciones múltuples se usa la siguiente sintaxis:

        try:
            ...
        except Exception1:
            ...
        except Exception2 as ex2:
            ...
        except ExceptionN:
            ...
        
Nótese que en la segunda excepción, se puede acceder a la información de la excepción como su nombre, su tipo, etc.

----

### Bloque de ejercicios 1:
* Ejercicio 1: Creación e impresión de variables
* Ejercicio 2: Mostrar los números del 1 al 120.
* Ejercicio 3: Obtener el cuadrado de los primeros 60 naturales con for y while.
* Ejercicio 4: Mostrar el resultado de las operaciones aritméticas de dos números ingresados desde consola.
* Ejercicio 5: Mostrar los números dentro de un rango específico.
* Ejercicio 6: Mostrar todas las tablas de multiplicar del 1 al 10.
* Ejercicio 7: Mostrar los números impares dentro de un rango específico ingresado desde consola.
* Ejercicio 8: Obtener el porcentaje de un número ingresado por consola.
* Ejercicio 9: Pedir números indefinidamente hasta ingresar 111.
* Ejercicio 10: Pedir la nota de ***n*** alumnos y saber cuantos aprobaron y cuantos reprobaron.

### Bloque de ejercicios 2
* Ejercicio 1: Creación de una lista, recorrerla, ordenarla, mostrarla y encontrar el indice de un elemento.
* Ejercicio 2: Añadir elementos a una lista y mostrarla.
* Ejercicio 3: Ingreso de texto a una variable vacía hasta tener contenido.
* Ejercicio 4: Dar el tipo de datos definidos en el programa.
* Ejercicio 5: Lista de diccionarios para representar una tabla.