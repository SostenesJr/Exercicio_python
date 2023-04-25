numero_incial = input('Digite um valor inicial: ')
numero_final = input('Digite um valor final: ')
numero_passo = input('Digite um valor para pulos: ')

numero_inicial_int = int(numero_incial)
numero_final_int = int(numero_final)
numero_passo_int = int(numero_passo)

for indice in range(numero_inicial_int, numero_final_int + 1, -numero_passo_int):
    print(indice)
