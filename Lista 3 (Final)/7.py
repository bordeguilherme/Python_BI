# 7. Análise avançada com Numpy

import pandas as pd
import numpy as np

xls = pd.ExcelFile('VendasDiarias.xlsx')
dfs_modificados = {}

for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name, header=0)
    dfs_modificados[sheet_name] = df

# Exercício 18: Utilize o NumPy para calcular a média, 
# variância e desvio padrão de um array numérico.
for sheet_name, df in dfs_modificados.items():
    print(f"Estatísticas NumPy para a aba: {sheet_name}")
    
    colunas_numericas = df.select_dtypes(include=['number'])
    
    for coluna in colunas_numericas.columns:
        valores = colunas_numericas[coluna].dropna().values  
        print(f"Coluna: {coluna}")
        print(f"Média: {np.mean(valores):.2f}")
        print(f"Variância: {np.var(valores):.2f}")
        print(f"Desvio Padrão: {np.std(valores):.2f}")
        print("-" * 30)
    print("\n" + "=" * 50 + "\n")

# Exercício 19: Crie arrays de números aleatórios e
# aplique operações matemáticas (adição, subtração, multiplicação e divisão).
print("Operações matemáticas com arrays NumPy\n")

array1 = np.random.randint(1, 100, 10)
array2 = np.random.randint(1, 100, 10)

print(f"Array 1: {array1}")
print(f"Array 2: {array2}")

print(f"Soma: {array1 + array2}")
print(f"Subtração: {array1 - array2}")
print(f"Multiplicação: {array1 * array2}")
print(f"Divisão: {np.divide(array1, array2).round(2)}") 

print("\n" + "=" * 50 + "\n")

# Exercício 23: Encontre os valores únicos de um array e 
# conte a frequência de cada valor.
for sheet_name, df in dfs_modificados.items():
    print(f"Análise de valores únicos para a aba: {sheet_name}\n")
    
    for coluna in df.columns:
        valores_unicos, frequencias = np.unique(df[coluna], return_counts=True)
        print(f"Coluna: {coluna}")
        print("Valores únicos e suas frequências:")
        for valor, freq in zip(valores_unicos, frequencias):
            print(f"{valor}: {freq}")
        print("-" * 30)
    print("\n" + "=" * 50 + "\n")
