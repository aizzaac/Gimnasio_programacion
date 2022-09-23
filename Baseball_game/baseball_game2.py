'''
JUEGO DE BEISBOL
Estás llevando la cuenta para un juego de béisbol con reglas extrañas. El juego consta de varias rondas, en donde los puntajes de las rondas
pasadas pueden afectar los puntajes de las rondas futuras. 
Al comienzo del juego, comienzas con un registro vacío. Se te asigna una lista de cadenas (strings) ops, donde ops[i] es la operación 
que debes aplicar al registro y es una de las siguientes:
1. Un entero (int): x. Registrar un nuevo puntaje x.
2. "+". Registrar un nuevo puntaje que es la suma de los 2 últimos puntajes. Está garantizado que siempore habrán 2 puntajes previos.
3. "D". Registrar un nuevo puntaje que es el doble del último puntaje. Está garantizado que siempre habrá un puntaje previo.
4. "C". Anular el último puntaje, eliminándolo del registro. Está garantizado que siempre habrá un puntaje previo.
Retornar la suma de todos los puntajes en el registro.
Ejemplo 1:
- Entrada: ops = ["5", "2", "C", "D", "+"]
- Salida: 30
- Explicación:
"5" : Agregar 5 al registro. El registro ahora es [5].
"2" : Agregar 2 al registro. El registro ahora es [5, 2].
"C" : Invalidar y eliminar el puntaje anterior. El registro ahora es [5].
"D" : Agregar 2 * 5 = 10 al registro. El registro ahora es [5, 10].
"+" : Agregar 5 + 10 = 15 al registro. El registro ahora es [5, 10, 15].
La suma total es 5 + 10 + 15 = 30.
Ejemplo 2:
- Entrada: ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
- Salida: 27
- Explicación:
"5" : Agregar 5 al registro. El registro ahora es [5].
"-2" : Agregar -2 al registro. El registro ahora es [5, -2].
"4" : Agregar 4 al registro. El registro ahora es [5, -2, 4].
"C" : Invalidar y eliminar el puntaje anterior. El registro ahora es [5, -2].
"D" : Agregar 2 * -2 = -4 al registro. El registro ahora es [5, -2, -4].
"9" : Agregar 9 al registro. El registro ahora es [5, -2, -4, 9].
"+" : Agregar -4 + 9 = 5 al registro. El registro ahora es [5, -2, -4, 9, 5].
"+" : Agregar 9 + 5 = 14 al registro. El registro ahora es [5, -2, -4, 9, 5, 14].
La suma total es 5 + -2 + -4 + 9 + 5 + 14 = 27.
Ejemplo 3:
- Entrada: ops = ["1"]
- Salida: 1
Restricciones:
- 1 <= ops.length <= 1000
- ops[i] es "C", "D", "+", o una cadena que representa un entero en el rango [-3 * 104, 3 * 104].
- Para la operación "+", siempre habrá por lo menos dos puntajes previos en el registro.
- Para las operaciones "C", "D", siempre habrá por lo menos un puntaje previo en el registro.
'''

import pytest


def baseball_game (ops):
  record = []
  for i in range (len(ops)):
    if ops[i] == 'C':
      record.pop()
    elif ops[i] == 'D':
      record.append(record[-1] * 2)
    elif ops[i] == '+':
      record.append(record[-1] + record[-2])
    else:
      record.append(int(ops[i]))
  return sum(record)


class TestClass:
  test_cases = (
    (["5", "2", "C", "D", "+"], 30), 
    (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
    (["1"], 1),
  )
  
  testable_functions = [
    baseball_game,
  ]
  
  def test_baseball_game(self):
    for baseball_game in self.testable_functions:
      for arr, expected in self.test_cases:
        assert baseball_game(arr) == expected
  
if __name__ == "__main__":
    pytest.main()
