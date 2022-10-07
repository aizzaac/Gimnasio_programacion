'''
CARTA GANADORA
En un juego de cartas, cada jugador recibe aleatoriamente una mano de cartas. Cuando los jugadores lancen sobre la mesa su única carta ganadora, 
ganará el que posea la carta más alta. 
Una carta ganadora es aquella que sólo existe una vez en la mano de cartas, y además es la más alta. 

Dada una matriz de conjuntos de enteros de cartas, devuelva la carta del jugador ganador. Si tal carta no existe retornar -1.

Ejemplo 1:
- Entrada: cards = [[5,7,3,9,4,9,8,3,1], [1,2,2,4,4,1], [1,2,3]]
- Salida: 8

Ejemplo 2:
- Entrada: cards = [[5, 5], [2, 2]]
- Salida: -1

Restricciones:
- 1 <= cards.length <= 2000
- 0 <= cards[i] <= 1000
'''


import pytest

def winning_card(list_list):
  empty_list = []
  for sublist in list_list:
    for element in sublist:
      if element not in empty_list:
        empty_list.append(element)
      else:
        empty_list.remove(element)
  return -1 if not empty_list else max(empty_list)


class TestClass:
  def test_one(self):
    assert winning_card([[5,7,3,9,4,9,8,3,1], [1,2,2,4,4,1], [1,2,3]]) == 8, "La carta ganadora debe ser 8"
  def test_two(self):
    assert winning_card([[5, 5], [2, 2]]) == -1, "No hay carta ganadora, entonces -1"
unit_test = TestClass()

if __name__ == "__main__":
    pytest.main()
