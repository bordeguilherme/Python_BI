# 4 - Análise de Dados de Vendas
# 4.1 - Leitura de Dados de Vendas:
# Utilize um arquivo CSV com dados de vendas (como produtos vendidos, receita, etc.).
# Carregue e processe os dados usando pandas.

import pandas as pd

file_path = './data_4.csv'  
df = pd.read_csv(file_path)

print("Primeiras linhas do DataFrame:")
print(df.head())

print("\nResumo estatístico dos dados:")
print(df.describe())

print("\nValores ausentes no DataFrame:")
print(df.isnull().sum())

print("\nUnidades vendidas e receita total por produto:")
sales_summary = df.groupby('Product')[['Units Sold', 'Revenue']].sum()
print(sales_summary)
