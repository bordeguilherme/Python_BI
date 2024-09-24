# 1 - Leitura e Visualização de Dados Simples
# 1.1 - Leitura de um Arquivo CSV:
# Baixe um arquivo CSV com dados simples
# (como uma planilha de vendas, clima, ou dados financeiros). 
# Use a biblioteca pandas para ler o arquivo e exibir as primeiras linhas.

import pandas as pd

arquivo_csv = './vendas_1.csv'
df = pd.read_csv(arquivo_csv)
print(df.head())
