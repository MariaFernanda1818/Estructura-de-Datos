def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    for i in lista:
        if i not in lista_sin_duplicados:
            lista_sin_duplicados.append(i)
    return lista_sin_duplicados

lista_original = [2, 2, 5, 7, 8, 10, 10, 26, 98, 12]
resultado = eliminar_duplicados(lista_original)
print(resultado)
