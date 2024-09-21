#Crie um programa que verifica se uma string fornecida pelo usuário é um palíndromo.

frase = input("Digite uma frase para verificar se é um palíndromo: ").replace(" ", "").lower()
if frase == frase[::-1]:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")