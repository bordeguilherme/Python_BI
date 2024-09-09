# Crie um programa que pede ao usuário dois números e imprime a soma, subtração, multiplicação e divisão dos dois números.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")

if n2 != 0:
    divisao = n1 / n2
    print(f"Divisão: {divisao}")
else:
    print("Divisão: O segundo número informado foi zero e divisão por zero não é permitida")