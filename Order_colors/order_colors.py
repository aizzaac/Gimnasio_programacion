'''
ORDERNAR COLORES
Un string str contiene una lista de nombres de colores separados por un sólo espacio.
Los colores en str están mexclados, pero cada color tiene su posición original al final de su nombre. 
Por ejemplo, 
- El string "black1 gold2 white3" puede reorganizarse a "gold2 black1 white3" o "gold2 white3 black1".
- str contiene solamente hasta 9 colores.

Dado un str con colores reorganizados, ordenar los colores a su estado original y retornar el str.

Ejemplo 1:
- Entrada: str = "red2 blue5 black4 green1 gold3"
- Salida: "green red gold blakc blue"

Ejemplo 2:
- Entrada: str = "gold2 black1 white3"
- Salida: "black gold white"

Restricciones:
- 2 <= str.length <= 200
- str consiste de múltiples nombres de colores, espacios, y dígitos del 1 al 9.
- str contiene hasta 9 nombres de colores.
- str contiene por lo menos un nombre de color.
- Los nombres de colores en str están separados por un sólo espacio.
- str no contiene espacios iniciales ni finales.
'''


import pytest

def order_colors(str):




class TestClass:
  def test_one(self):
    assert order_colors("red2 blue5 black4 green1 gold3") == "green red glod black blue", "La respuesta debe ser: green red glod black blue"
  def test_two(self):
    assert order_colors("gold2 black1 white3") == "black gold white", "La respuesta debe ser: black gold white"

unit_test = TestClass()

if __name__ == "__main__":
    pytest.main()
