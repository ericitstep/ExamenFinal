#Ejemplo#2: Dada una lista de enteros y un entero X, generar una funcion que regrese los indices de los 
#elementos de la lista cuya suma sea igual a X.

#Encuentra los índices de los dos elementos en la lista cuya suma sea igual a x.
#Argumentos:
#        lista: Lista de enteros.
#        x (int): Entero objetivo para la suma de los 2 numeros enteros.
#Retorna: Lista de tuplas, donde cada tupla contiene los índices de los elementos que suman x.
def encontrarPares(lista, x):
   
    pares = []
    n = len(lista)

    # Iterar sobre todos los elementos de la lista
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] + lista[j] == x:
                pares.append((i, j))

    return pares

#Ejemplo de uso
lista = [8,1,7]
x = 9

resultado = encontrarPares(lista, x)
print(resultado)

