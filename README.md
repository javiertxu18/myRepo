# Repositorio: myRepo
Este repositorio contiene la práctica 3 del máster en big data. 
Y la teoría que yo vea conveniente tener.

Versiones de pip3 y Python3:

```bash
    python3 --version
    Python 3.8.10

    pip3 --version
    pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```

### Autor: *Javier Herrero*

## Enunciado de la práctica 3
Práctica 3. Entornos de desarrollo. 

Migrar el código de adivina frase de la práctica 1 en la máquina virtual Ubuntu.

*Nota: He vuelto a hacer el código de la práctica 1 de cero con lo aprendido hasta ahora*

Pytest. Realizar al menos 10 test unitarios.

Coverage. Garantizar un 40% de coverage del test.

Flake8. Tener cualquier tipo de “advertencia de calidad” por debajo de 5 repeticiones.

Sin contar las advertencias de tipo complejidad ciclomática.
Ejemplo:

```bash
flake8 --statistics src/main/
    2 E302 expected 2 blank lines, found 1
    1 E501 line too long (98 > 79 characters)
    1 F841 local variable 'res' is assigned to but never used
    2 W292 no newline at end of file
```

Establecer un umbral máximo de complejidad ciclomatica 8 y tener como máximo 5
advertencias.

Ejemplo para complecjidad ciclomática 2:


```bash
flake8 --max-complexity 2 --statistics src/main/
    3 C901 'Persona.dividir' is too complex (4)
```

### Enunciado práctica 1
Adivina frase.

Admin introduce una frase a adivinar y un número máximo de intentos para adivinarlo.

Pide al usuario adivinar el número de palabras (ej1) en la frase. Si el usuario se equivoca, se le indica si el numero es mayor o menor y el número de intentos restantes.

Pide al usuario si desea adivinar letras o palabras:

Letras: Se pide la letra. Muestra al usuario las letras que se van adivinando en la frase. Si se equivoca se resta 1 intento.

Palabras:Se pide la palabra. Muestra al usuario las palabras que se van adivinando en la frase. Si se equivoca se resta 1 intento.

Adivinar frase: Si se equivoca se resta 1 intento.

El programa termina cuando el usuario ha adivinado la frase o si se supera el máximo número de intentos. Al final independientemente de haber adivinado o no, muestra los intentos insertados por tipo letra o palabra.

## Virtual enviroment
El virtual enviroment no lo he subido a github. He subido en fichero
de "requirements.txt", en este fichero encontramos todas las librerías
utilizadas en el proyecto con sus respectivas versiones.

## Test unitario
Para ejecutar tests unitarios:

```bash
    python3 -m pytest -s
    python3 -m pytest -v
```

##Coverage
Instrucciones para hacer un coverage:
```bash
    python3 -m coverage run fileName  # Suele ser el main 
    python3 -m coverage report --omit="/usr/*"  # Mostrar el report en consola
    python3 -m coverage html --omit="/usr/*"  # Mostrar el report en web
```

Para aumentar el porcentaje de coverage, hacer más testeos de código.

## Flake8
He creado el fichero /.flake8 con el siguiente contenido
```bash
    [flake8]
        ignore = E722           # Para que no me moleste el bare except
        max-line-length = 120   # Para cambiar el largo máximo a 120
        exclude = src/test/*    # Para omitir los ficheros de tests
        max-complexity = 8      # Para definir una complejidad ciclomática
```

## Librerías a destacar

*configParser*: Para leer y escribir en el fichero '/config.ini'

*logger*: Para mostrar por pantalla errores y mensajes y guardar un log en '/.log'

*pandas*: Para gestionar la lectura/escritura de ficheros y el análisis de los datos.

*multipledispatch*: Para poder usar la sobrecarga de operadores en python3.

## Cómo hacer un switch en python sin aumentar la complejidad ciclomática

Código extraído de *src/main/scripts/objetos/Game.py* línea 52

```python
52    # Alternativa a Switch
53    avOpt = {1: self.playGame, 2: self.showRankings, 0: self.exitMenu}
54    result = avOpt.get(userOption, 'Default controlado por excepciones')
55    result()
```

avOpt: Es un diccionario. Este diccionario en específico contiene 3 elementos, cada 
uno de ellos separado en 2 partes separadas por dos puntos " : ". La parte de la izquierda sería el *case* de un switch,
y la derecha lo que iría dentro del case. En este caso, hemos metido los *instancemethods* (referencias) de las
funciones que queremos que se ejecuten en cada caso.

*result = avOpt.get(userOption, 'Default controlado por excepciones')*: Hacemos un
*.get(x,y)* del diccionario y lo guardamos en una variable. *x* sería el valor del
parámetro de un switch, y lo que tendría que coincidir con la parte de la izqueirda de los elementos
del diccionario. *y* es el default, en caso de no cumplirse ningún case, devuelve lo que
hayamos introducido por parámetros.

*result()*: Llamamos al método referenciado.

## Github
Para ver las branches (ramas)
```bash
    git branch
```
Para crear una branch nueva
```bash
    git branch branchName
```
Para ver ficheros añadidos al commit
```bash
    git status
```
Para añadir ficheros al commit
```bash
    git add filePath
```
Para quitar todos los ficheros del commit
```bash
    git reset
```
Para quitar 1 fichero del commit
```bash
    git reset fileName
```
Para hacer un commit
```bash
    git commit -m "mensaje"
```
Para hacer un push y que se suba a github (*Pide usuario y token*)
```bash
    git push
```
Para hacer un push de una branch nueva
```bash
    git push -u origin branchName
```
Para hacer un merge de 2 branches
```bash
    git checkout a  #  Vamos a la rama master (a)
    git merge b     # Traemos lo de la rama b a la a y lo juntamos
    git commit -a   # Guardamos los cambios
```
Si da un error de merge, podemos ir al archivo que dé el error y decidir que versión
de código se queda (si la local, o la remota) ó ejecutar el siguiente comando para
usar la mergetool.

El comando irá mostrando cambio a cambio por consola para que decidamos si nos quedamos
con el local o el remoto.
```bash
    git mergetool
```
Para borrar los commits (remotos) de una rama en específico de un hash en adelante:
```bash
    git push -f origin <last_known_good_commit>:<branch_name>
```
Para borrar los commits (locales) de una rama en específico de un hash en adelante:
```bash
    git reset --hard <last_known_good_commit>
```
En caso de que nuestro branch esté por delante del 'origin/main' por X commits,
ejecutar el siguiente comando:
```bash
    git fetch -p
```

Para ver las diferencias entre los archivos locales y el repositorio en github:
```bash
    git diff fileName
```

Para hacer un add de una parte de un fichero, no de todo. Una vez ejecutemos el comando
la consola nos irá mostrando las diferencias entre el archivo en el repositorio
y el archivo en local, mediante las claves de y (para añadir esa parte) y n (para
no añadir esa parte) decidiremos qué añadir.
```bash
    git add -p fileName
```

###¿Cómo escribir un buen mensaje de commit?

1- Título del mensaje:

- Descripción general de los cambios realizados en el commit.
- Máximo 50 carácteres

2- Cuerpo del mensaje_

- Decir los cambios que se han realizado de una forma más detallada
- El motivo de los cambios
- Remarcar las partes importantes si las hubiera

###Branching strategies

Hablar con el equipo con el que se esté trabajando para tener una estructura de 
branching en común.

Hacer unas normas en conjunto con el equipo y dejarlo por escrito (Best practices)

Una estructura de branching podría ser la siguiente:
- Pruebas
- Desarrollo
- Pre-Producción
- Producción (main)