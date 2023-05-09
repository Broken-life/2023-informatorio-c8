x = 0
y = 1
z = 0

while True:
    n = int(input("Ingrese un numero mayor a 1: "))
    if n > 1:
        break
print("1", end=" ")

for i in range(1, n):
    z = x + y
    print(z, end=" ")
    x = y
    y = z
print("")