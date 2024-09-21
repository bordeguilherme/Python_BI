#Crie um programa que calcula o fatorial de um número fornecido pelo usuário.

def main():
    try:
        numero = int(input("Digite um número inteiro para calcular o fatorial: "))
        
        if numero < 0:
            print("O fatorial não está definido para números negativos.")
        else:
            fatorial = 1
            for i in range(1, numero + 1):
                fatorial *= i
            print(f"O fatorial de {numero} é {fatorial}.")
    
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

main()