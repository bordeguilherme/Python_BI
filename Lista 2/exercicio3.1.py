# 3 - Análise de Dados de Pesquisa
# 3.1 - Leitura de Dados de Pesquisa:
# Encontre um conjunto de dados de uma pesquisa ou questionário em formato CSV.
# Carregue os dados com pandas e explore as colunas.

import pandas as pd

arquivo_csv = './arquivo_3.csv'

dados = pd.read_csv(arquivo_csv)

print("Primeiras linhas do dataset:")
print(dados.head())

print("\nInformações do dataset:")
print(dados.info())

print("\nResumo estatístico dos dados numéricos:")
print(dados.describe())

print("\nContagem de valores únicos em colunas categóricas:")
for coluna in dados.select_dtypes(include='object').columns:
    print(f"{coluna}:\n{dados[coluna].value_counts()}\n")
