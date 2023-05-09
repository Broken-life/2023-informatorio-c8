text = str(input("Ingrese un texto: "))
word = text.split()
text_reverse= ""

for i in range(len(word)):
    text_reverse += word[len(word)-1-i] + " "
print(text_reverse)
