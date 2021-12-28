# myRepo
Este repositorio contiene la práctica 3 del máster en big data.

## Enunciado de la práctica 3
Práctica 3. Entornos de desarrollo.
 Migrar el código de adivina frase de la práctica 1 en la máquina virtual Ubuntu.
 Pytest. Realizar al menos 10 test unitarios.
 Coverage. Garantizar un 40% de coverage del test.
 Flake8. Tener cualquier tipo de “advertencia de calidad” por debajo de 5 repeticiones.
Sin contar las advertencias de tipo complejidad ciclomática.
Ejemplo:
flake8 --statistics src/main/
2 E302 expected 2 blank lines, found 1
1 E501 line too long (98 > 79 characters)
1 F841 local variable 'res' is assigned to but never used
2 W292 no newline at end of file
 Establecer un umbral máximo de complejidad ciclomatica 8 y tener como máximo 5
advertencias.
Ejemplo para complecjidad ciclomática 2:
flake8 --max-complexity 2 --statistics src/main/
3 C901 'Persona.dividir' is too complex (4)
