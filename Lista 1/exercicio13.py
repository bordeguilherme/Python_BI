#Crie um programa que imprime a tabuada de um número fornecido pelo usuário.

numero = int(input("Digite um número para ver a sua tabuada: "))

print(f"Tabuada de {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")