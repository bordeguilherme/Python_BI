#Crie um programa que pede ao usuário sua altura em metros e peso em quilogramas e calcula o Índice de Massa Corporal (IMC).

def calcular_imc():
    try:
        altura = float(input("Digite sua altura em metros (ex: 1.70): "))
        peso = float(input("Digite seu peso em quilogramas (ex: 60.5): "))

        imc = peso / (altura ** 2)
        print(f"Seu Índice de Massa Corporal (IMC) é: {imc:.2f}")

        if imc < 18.5:
            print("Você está abaixo do peso.")
        elif 18.5 <= imc < 24.9:
            print("Você está com peso normal.")
        elif 25 <= imc < 29.9:
            print("Você está com sobrepeso.")
        else:
            print("Você está com obesidade.")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos para altura e peso.")

calcular_imc()