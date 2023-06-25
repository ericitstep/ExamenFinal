#Ejercicio#2: Dada una lista de strings implemente una funcion que regrese una lista de tuplas de anagramas.

def encontrarAnagramas(lista):
    anagramas = {}  # Diccionario para almacenar los anagramas encontrados

    # Iterar sobre cada palabra en la lista
    for palabra in lista:
        # Crear una clave única para cada anagrama ordenando los caracteres de la palabra
        clave = ''.join(sorted(palabra))

        # Agregar la palabra a la lista de anagramas correspondiente a su clave
        if clave in anagramas:
            anagramas[clave].append(palabra)
        else:
            anagramas[clave] = [palabra]

    # Filtrar las listas de anagramas para obtener únicamente las tuplas de anagramas
    tuplasAnagramas = [tuple(anagrama) for anagrama in anagramas.values() if len(anagrama) > 1]

    return tuplasAnagramas

#Ejemplo de uso:
listaPalabras = ["apa", "oso", "paa", "soo"]
resultado = encontrarAnagramas(listaPalabras)
print(resultado)

