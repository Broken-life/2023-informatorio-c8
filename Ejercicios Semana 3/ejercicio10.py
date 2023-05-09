text = str(input("Ingrese un texto: ").lower())

for i in range(len(text)):
    if text[i] == "a" or text[i] == "e" or text[i] == "i" or text[i] == "o" or text[i] == "u":
        text = text.replace(text[i], text[i].upper())
print(text)