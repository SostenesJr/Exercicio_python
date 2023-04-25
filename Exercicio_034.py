numero = input('Digite um numero: ')
numero_int = int(numero)
contador = 0
for indice in range(1, numero_int + 1):
    if numero_int % indice == 0:
        contador += 1
if contador == 2:
    print('Esse numero é primo!')
    print(f'Esse numero é divisivel por 1 é {numero}')
else:
    print('Esse numero nao é primo')
    print(f'Esse numero é divisivel {contador} vez')
