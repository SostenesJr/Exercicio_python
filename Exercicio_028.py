first_number = input('Digite um numero: ')
first_number_int = int(first_number)

for indice in range(0, first_number_int + 1):
    if indice % 2 == 0:
        print(indice)
