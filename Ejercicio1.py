#Ejercicio#1: Dado un string implemente una funcion que haciendo uso de la tecnica de recursividad regrese el 
#inverso del string. 

def invertirString(string):
    # Caso base: cuando la longitud del string es 0 o 1, simplemente se devuelve el string original
    if len(string) <= 1:
        return string
    
    # Llamada recursiva: se invierte el substring que va desde el segundo carácter hasta el final
    # y se concatena con el primer carácter
    return invertirString(string[1:]) + string[0]

# Ejemplo de uso
stringOriginal = "pedro"
stringInvertido = invertirString(stringOriginal)
print(stringInvertido) 
