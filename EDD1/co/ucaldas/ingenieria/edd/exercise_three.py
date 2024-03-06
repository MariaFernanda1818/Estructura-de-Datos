def suma_elementos(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

lista = [1,2,3,4,5,6,7,8,9,10]
print("La suma de los elementos de la lista es:", suma_elementos(lista))
