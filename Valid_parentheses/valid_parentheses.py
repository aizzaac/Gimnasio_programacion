'''
PARENTESIS VALIDO
Dado un string s que contiene los caracteres '(', ')', '{', '}', '[' y ']', determinar si el string es válido. 
Un string es válido si:
- Los caracteres abiertos deben estar cerrados por el mismo tipo de caracter.
- Los caracteres abiertos debe cerrarse en el orden correcto.

Restricciones:
- 1 <= s.length <= 104
- s consiste únicamente de '()[]{}'

Ejemplo 1:
- Entrada: s = "()"
- Salida: válido

Ejemplo 2:
- Entrada: s = "()[]{}"
- Salida: válido

Ejemplo 3:
- Entrada: s = "(]"
- Salida: inválido

Ejemplo 4:
- Entrada: s = "([)]"
- Salida: inválido

Ejemplo 5:
- Entrada: s = "{[]}"
- Salida: válido
'''


import pytest


def valid_parentheses(s):
  
class TestClass:
  def test_one(self):
    assert valid_parentheses("()") == valid, "La respuesta debe ser: válido"
  def test_two(self):
    assert valid_parentheses("()[]{}") == valid, "La respuesta debe ser: válido"
  def test_three(self):
    assert valid_parentheses("(]") == invalid, "La respuesta debe ser: inválido"
  def test_four(self):
    assert valid_parentheses("(])]") == invalid, "La respuesta debe ser: inválido"
  def test_five(self):
    assert valid_parentheses("{[]}") == valid, "La respuesta debe ser: válido"

unit_test = TestClass()

if __name__ == "__main__":
    pytest.main()

