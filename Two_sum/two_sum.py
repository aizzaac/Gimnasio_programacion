'''
DOS SUMAN MENOS QUE K
Dada una matriz A de enteros y un entero K, retornar el valor máximo S tal que exista i < j con A[i] + A[j] = S y S < K. 
Si no existe tal i, j que satisfaga la ecuación, retornar -1.

Ejemplo 1:
- Entrada: A = [34, 23, 1, 24, 75, 33, 54, 8], K = 60
- Salida: 58
- Explicación:
Se suma 34 y 24 para obtener 58 que es menor que 60 y no hay un par que sume 59. Por lo tanto, la suma máxima es 58.

Ejemplo 2:
- Entrada: A = [10, 20, 30], K = 15
- Salida = -1
- Explicación:
En este caso no es posible obtener un par de números que sumen menos que 15.

Restricciones:
- 1 <= A.length <= 100
- 1 <= A[i] <= 1000
- 1 <= K <= 20005
'''


import pytest

def two_sum(A, K):
    ans = -1
    if len(A) == 1:
        return -1
    A.sort()
    for i in reversed(A):
        if i < K:
            for j in A:
                if j < i and i+j < K:
                    ans = max(ans, i+j)
                else:
                    break
    return ans


class TestClass:
  def test_one(self):
    assert two_sum([34, 23, 1, 24, 75, 33, 54, 8], 60) == 58, "La respuesta debe ser 58"
  def test_two(self):
    assert two_sum([10, 20, 30], 15) == -1, "La respuesta debe ser -1"
unit_test = TestClass()

if __name__ == "__main__":
    pytest.main()
