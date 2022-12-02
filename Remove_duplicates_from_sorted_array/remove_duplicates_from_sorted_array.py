'''
ELIMINAR DUPLICADOS DE UNA MATRIZ ORDENADA
Dado una matriz de números enteros en orden ascendente, eliminar los duplicados in situ de modo que cada elemento único aparezca sólo una vez.
El orden relativo de los elementos debe mantenerse igual. Dado que es imposible cambiar la longitud de la matriz en algunos lenguajes, el 
resultado debe colocarse en la primera parte de ésta. Es decir, si hay k elementos después de eliminar los duplicados, entonces
los primeros k elementos de nums deberían contener el resultado final. No importa lo que se deje más allá de los primeros k elementos. 
Devuelve k después de colocar el resultado final en las primeras k ranuras de nums. No asigne espacio adicional para otra matriz. Para ello,
debe modificar la matriz de entrada in situ con memoria adicional O(1).

Ejemplo 1:
- Entrada: nums = [1,1,2]
- Salida: 2, nums = [1,2,_]
- Explicación: 
La función debe regresar k = 2, con los dos primeros elementos de nums siendo 1 y 2 respectivamente.
No importa lo que se deje más allá de la k devuelta (de ahí que se vean guiones bajos).

Ejemplo 2:
- Entrada: nums = [0,0,1,1,1,2,2,3,3,4]
- Salida: 5, nums = [0,1,2,3,4,_,_,_,_,_]
- Explicación: 
La función debe devolver k = 5, siendo los primeros cinco elementos de nums 0, 1, 2, 3 y 4 respectivamente. 
No importa lo que se deje más allá de la k devuelta (de ahí que hayan guiones bajos).

Restricciones:
- 1 <= nums.length <= 3 * 104
- -100 <= nums[i] <= 100
- nums está ordenado ascendentemente.
'''

