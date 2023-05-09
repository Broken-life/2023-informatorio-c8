word = str(input("Ingrese una palabra: "))
indice = -1

for i in word:
    print(word[indice], end="")
    indice -= 1
