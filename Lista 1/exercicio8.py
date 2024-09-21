#Escreva um programa que gera um número aleatório entre 1 e 100 e pede ao usuário para adivinhar o número, fornecendo dicas de "maior" ou "menor" até que o usuário acerte.

import random

numero = random.randint(1, 100)
print("Tente adivinhar o número que estou pensando entre 1 e 100.")

while True:
    palpite = int(input("Digite o número que você acha que estou pensando: "))

    if palpite < numero:
        print("O número que estou pensando é maior!")
    elif palpite > numero:
        print("O número que estou pensando é menor!")
    else:
        print(f"Parabéns! Você acertou o número {numero}.")
        break