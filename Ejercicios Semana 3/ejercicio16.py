text = input("Ingrese un texto: ").lower()
text_reverse = ""
for i in range(len(text)):
    text_reverse += text[len(text)-1-i]
print(text_reverse)