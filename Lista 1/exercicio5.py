#Crie um programa que pede ao usuário uma string e imprime o número de caracteres, palavras e frases na string. 

import re

def contar_texto(texto):
    num_caracteres = len(texto)
    palavras = texto.split()
    num_palavras = len(palavras)
    
    frases = re.split(r'[.!?]+', texto)
    frases = [f.strip() for f in frases if f.strip()] 
    num_frases = len(frases)
    
    return num_caracteres, num_palavras, num_frases

def main():
    texto = input("Digite: ")
    num_caracteres, num_palavras, num_frases = contar_texto(texto)
    
    print(f"Número de caracteres: {num_caracteres}")
    print(f"Número de palavras: {num_palavras}")
    print(f"Número de frases: {num_frases}")

main()