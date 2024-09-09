#Escreva um programa que pede ao usuário um número e verifica se ele é par ou ímpar.

n1 = int(input("Digite um número: "))

if n1 % 2 == 0:
    print(f"O número {n1} é par.")
else:
    print(f"O número {n1} é ímpar.")