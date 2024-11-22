# 6. Análise de séries temporais

import pandas as pd
import matplotlib.pyplot as plt

xls = pd.ExcelFile('VendasDiarias.xlsx')
dfs_modificados = {}

for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name, header=0)
    dfs_modificados[sheet_name] = df

# Exercício 16: Plote um gráfico de linha mostrando a evolução das vendas ao longo do tempo.
for sheet_name, df in dfs_modificados.items():
    print(f"Gráfico de linha para a evolução das vendas na aba: {sheet_name}")

    if 'Data' in df.columns and 'Vendas' in df.columns:
        df.sort_values(by='Data', inplace=True)
        
        plt.figure(figsize=(10, 6))
        plt.plot(df['Data'], df['Vendas'], marker='o', linestyle='-', color='blue', label='Vendas')
        plt.title(f"Evolução das Vendas ao Longo do Tempo - {sheet_name}")
        plt.xlabel("Data")
        plt.ylabel("Vendas")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("Colunas 'Data' e/ou 'Vendas' não encontradas nesta aba.\n")

# Exercício 17: Calcule a média móvel de uma coluna de séries 
# temporais e plote-a junto com os dados originais.
for sheet_name, df in dfs_modificados.items():
    print(f"Gráfico de média móvel para a aba: {sheet_name}")

    if 'Data' in df.columns and 'Vendas' in df.columns:
        df.sort_values(by='Data', inplace=True)

        df['Média Móvel'] = df['Vendas'].rolling(window=7, min_periods=1).mean()
        
        plt.figure(figsize=(10, 6))
        plt.plot(df['Data'], df['Vendas'], marker='o', linestyle='-', color='blue', label='Vendas')
        plt.plot(df['Data'], df['Média Móvel'], linestyle='--', color='red', label='Média Móvel (7 dias)')
        plt.title(f"Evolução das Vendas com Média Móvel - {sheet_name}")
        plt.xlabel("Data")
        plt.ylabel("Vendas")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("Colunas 'Data' e/ou 'Vendas' não encontradas nesta aba.\n")

    