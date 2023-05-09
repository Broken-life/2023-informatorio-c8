word = str(input("Ingrese una palabra: "))
indice = -1
word_palindroma= "" 

for i in word:
    word_palindroma += word[indice]
    indice -= 1

if word_palindroma == word:
    print("La palabra ingresada es palíndroma")
else:
    print("La palabra ingresada no es palíndroma")
