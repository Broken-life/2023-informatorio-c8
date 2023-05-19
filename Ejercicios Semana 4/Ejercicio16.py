user_input = input("Ingrese una lista de palabras separadas por espacios o comas: ")
user_list = user_input.split()

def eliminar_duplicados(lst):
    list2 = set()
    result = []
    for item in lst:
        if item not in list2:
            list2.add(item)
            result.append(item)
    return result

lista_sin_duplicados = eliminar_duplicados(user_list)
print(lista_sin_duplicados)