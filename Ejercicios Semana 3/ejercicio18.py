number = int(input("Escribe un número: "))
counter = 1

for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(counter, end=" ")
        counter += 1
    print("")


