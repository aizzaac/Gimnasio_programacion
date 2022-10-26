'''
DISCREPANCIA EN UN CONJUNTO DE DATOS
Asumir que se te entrega un conjunto que inicialmente contiene números del 1 a n. Desafortunadamente, debido a un error de datos, 
uno de los números en el conjunto se duplicó a otro número dentro del conjunto, lo que resulta en la repetición de un número y la pérdida
de otro número.
Dada una matriz "nums" que representa el estado de los datos en el conjunto después del error, encuentre y retorne el número que se repite y el número faltante.

Ejemplo 1:
- Entrada: nums = [1, 2, 3, 4, 3]
- Salida: [3, 5]
- Explicación:
3 se repite y 5 está faltando.

Ejemplo 2:
- Entrada: nums = [1, 2, 2]
- Salida: [2, 3]
- Explicación:
2 se repite y 3 está faltando.
'''

import pytest


def set_mismatch(nums):
    lista=[]
    for val in range (len(nums)):
        if val+1 != nums[val]:
            lista.extend([nums[val], val+1])
    return(lista)


class TestClass:
  def test_one(self):
    assert set_mismatch([1, 2, 3, 4, 3]) == [3, 5], "El resultado debe ser [3, 5]"
  def test_two(self):
    assert set_mismatch([1, 2, 2, 4]) == [2, 3], "El resultado debe ser [2, 3]"

if __name__ == "__main__":
    pytest.main()
