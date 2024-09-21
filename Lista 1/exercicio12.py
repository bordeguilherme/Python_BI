#Escreva um programa que ordena uma lista de números fornecida pelo usuário em ordem crescente e decrescente.

lista = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))

print("Ordem crescente:", sorted(lista))
print("Ordem decrescente:", sorted(lista, reverse=True))