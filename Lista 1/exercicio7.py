#Crie um programa que imprime os primeiros n números da sequência de Fibonacci, onde n é fornecido pelo usuário.

def sequencia_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

n = int(input("Digite o número de termos que você deseja ver da sequência de Fibonacci: "))

if n <= 0:
    print("Insira um número positivo.")
else:
    sequencia = sequencia_fibonacci(n)
    print(f"Os primeiros {n} números da sequência de Fibonacci são:")
    print(sequencia)