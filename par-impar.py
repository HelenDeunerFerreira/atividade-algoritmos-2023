num = int(input("Número desejado: "))
contador = 0

for i in list(range(1, 11)):
    if(num < 1):
        continue
    else:
        if(num % i == 0):
            contador += 1
            continue

if(contador > 2):
    print(f"{num} não é um número primo")
else:
    print(f"{num} é um número primo")