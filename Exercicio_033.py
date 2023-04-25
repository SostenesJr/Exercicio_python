par = impar = soma_impar = soma_par = 0
for numero in range(3, 100):
    if numero % 2 == 0:
        par += 1
        soma_par += numero
    else:
        impar += 1
        soma_impar += numero
        print(f'{numero}')

print(f'Foram {impar} numeros impas')
print(f'A soma total dos numeros impares é :{soma_impar}')
print(f'Foram {par} numeros par')
print(f'A soma total dos numeros pares é :{soma_par}')
