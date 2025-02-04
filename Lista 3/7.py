# 7. Análise avançada com NumPy

import pandas as pd
import numpy as np
import os

xls = pd.ExcelFile('VendasDiarias.xlsx')
dfs_modificados = {sheet: pd.read_excel(xls, sheet_name=sheet, header=0) for sheet in xls.sheet_names}

os.makedirs("Analise_NumPy", exist_ok=True)

def calcular_estatisticas(valores):
    return {
        "Média": np.mean(valores),
        "Variância": np.var(valores),
        "Desvio Padrão": np.std(valores)
    }

# Exercício 18: Utilize o NumPy para calcular a média, variância e desvio padrão de um array numérico.
for sheet_name, df in dfs_modificados.items():
    print(f"Estatísticas NumPy para a aba: {sheet_name}")
    
    colunas_numericas = df.select_dtypes(include=['number'])
    estatisticas = []

    for coluna in colunas_numericas.columns:
        valores = colunas_numericas[coluna].dropna().values
        stats = calcular_estatisticas(valores)
        estatisticas.append({"Coluna": coluna, **stats})
        print(f"Coluna: {coluna}")
        print(f"Média: {stats['Média']:.2f}, Variância: {stats['Variância']:.2f}, Desvio Padrão: {stats['Desvio Padrão']:.2f}")
        print("-" * 30)

    pd.DataFrame(estatisticas).to_csv(f"Analise_NumPy/Estatisticas_{sheet_name}.csv", index=False)
    print("\n" + "=" * 50 + "\n")

# Exercício 19: Crie arrays de números aleatórios e 
# aplique operações matemáticas (adição, subtração, multiplicação e divisão).
print("Operações matemáticas com arrays NumPy\n")

tamanho_array = 10
intervalo = (1, 100)
array1 = np.random.randint(intervalo[0], intervalo[1], tamanho_array)
array2 = np.random.randint(intervalo[0], intervalo[1], tamanho_array)

operacoes = {
    "Soma": array1 + array2,
    "Subtração": array1 - array2,
    "Multiplicação": array1 * array2,
    "Divisão": np.divide(array1, array2).round(2)
}

print(f"Array 1: {array1}")
print(f"Array 2: {array2}")
for op, resultado in operacoes.items():
    print(f"{op}: {resultado}")

np.savetxt("Analise_NumPy/Arrays.csv", np.column_stack((array1, array2)), delimiter=",", header="Array1,Array2", fmt="%d")
print("\n" + "=" * 50 + "\n")

# Exercício 23: Encontre os valores únicos de um array e conte a frequência de cada valor.
for sheet_name, df in dfs_modificados.items():
    print(f"Análise de valores únicos para a aba: {sheet_name}\n")
    
    valores_unicos_csv = []
    for coluna in df.columns:
        valores_unicos, frequencias = np.unique(df[coluna].dropna(), return_counts=True)

        if len(valores_unicos) > 10:
            print(f"Coluna: {coluna} possui mais de 10 valores únicos. Exibindo os 10 primeiros.")
            valores_unicos, frequencias = valores_unicos[:10], frequencias[:10]
        
        print(f"Coluna: {coluna}")
        print("Valores únicos e suas frequências:")
        for valor, freq in zip(valores_unicos, frequencias):
            print(f"{valor}: {freq}")
            valores_unicos_csv.append({"Coluna": coluna, "Valor": valor, "Frequência": freq})
        print("-" * 30)

    pd.DataFrame(valores_unicos_csv).to_csv(f"Analise_NumPy/Valores_Unicos_{sheet_name}.csv", index=False)
    print("\n" + "=" * 50 + "\n")
