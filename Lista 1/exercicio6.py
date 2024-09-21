#Escreva um programa que pede ao usuário um número e verifica se ele é primo.

numero = int(input("Digite um número: "))

if numero <= 1:
    print(f"O número {numero} não é primo.")
elif all(numero % i != 0 for i in range(2, int(numero ** 0.5) + 1)):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")