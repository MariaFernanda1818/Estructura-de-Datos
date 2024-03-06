def listas(lista1, lista2):
    for item in lista1:
        for item2 in lista2:
            if item == item2:
                return True
    return False

lista1 = ['a', 'b', 'c', 'd', 'e']
lista2 = ['f', 'g', 'h', 'i', 'j']
print(listas(lista1, lista2))