import random

player = str(input("Ingrese su nombre: "))
print(f"Bienvenido {player} a este juego de adivinar el número secreto😎" 
      f"\nTienes 8 intentos para adivinar el número secreto, el cual está entre 1 y 100"
      f"\n¡Y que la suerte, esté siempre de tu lado!🤞")

num_secret = random.randint(1, 100)

intentos = 0

while intentos < 8:
    num = input("Ingrese un número:")
    if num.isdigit() == False:
        print("Ingrese un número válido")
        continue
    num = int(num)
    intentos += 1
    if num < num_secret:
        print(f"El número secreto es mayor que {num}, te quedan {8 - intentos} intentos")
    elif num > num_secret:
        print(f"El número secreto es menor que {num}, te quedan {8 - intentos} intentos")
    else:
        break

if num == num_secret:
    print(f"¡Felicidades {player} ganaste un caramelo!🎉" 
          f"\nHas adivinado el número secreto en {intentos} intentos")
else:
    print(f"¡Lo siento {player}, perdiste!😢 No has adivinado."
          f"\nEl número secreto era {num_secret}")
    
print("¡Gracias por jugar!👋")