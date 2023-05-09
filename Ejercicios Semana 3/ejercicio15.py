text = str(input("Ingrese un texto: ").lower())

#contar cuantas veces aparece cada letra

for i in range(97, 123):
    if chr(i) in text:
        text_count = text.count(chr(i))
        print(f'La letra "{chr(i).upper()}" aparece {text_count} vez/veces en el texto ingresado.')
