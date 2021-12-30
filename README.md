# Repositorio: myRepo
Este repositorio contiene la práctica 3 del máster en big data.

## Enunciado de la práctica 3
Práctica 3. Entornos de desarrollo. 

Migrar el código de adivina frase de la práctica 1 en la máquina virtual Ubuntu.

*Nota: He vuelto a hacer el código de la práctica 1 de cero con lo aprendido hasta ahora*

Pytest. Realizar al menos 10 test unitarios.

Coverage. Garantizar un 40% de coverage del test.

Flake8. Tener cualquier tipo de “advertencia de calidad” por debajo de 5 repeticiones.

Sin contar las advertencias de tipo complejidad ciclomática.
Ejemplo:

```python
flake8 --statistics src/main/
    2 E302 expected 2 blank lines, found 1
    1 E501 line too long (98 > 79 characters)
    1 F841 local variable 'res' is assigned to but never used
    2 W292 no newline at end of file
```

Establecer un umbral máximo de complejidad ciclomatica 8 y tener como máximo 5
advertencias.

Ejemplo para complecjidad ciclomática 2:


```python
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
Para ejecutar un test unitario, ir al terminal y ejecutar el siguiente comando:

```bash
python3 -m pytest
```

## Librerías a destacar

*configParser*: Para leer y escribir en el fichero '/config.ini'

*logger*: Para mostrar por pantalla errores y mensajes y guardar un log en '/.log'

