# 6. Análise de séries temporais

import pandas as pd
import matplotlib.pyplot as plt
import os

xls = pd.ExcelFile('VendasDiarias.xlsx')
dfs_modificados = {sheet: pd.read_excel(xls, sheet_name=sheet, header=0) for sheet in xls.sheet_names}

os.makedirs("Series_Temporais", exist_ok=True)

def salvar_grafico(fig, nome):
    caminho = os.path.join("Series_Temporais", nome)
    fig.savefig(caminho)
    plt.close(fig)

def garantir_coluna_data(df, coluna_data):
    if coluna_data in df.columns:
        df[coluna_data] = pd.to_datetime(df[coluna_data], errors='coerce')
        df.dropna(subset=[coluna_data], inplace=True)
        return True
    return False

# Exercício 16: Plote um gráfico de linha mostrando a 
# evolução das vendas ao longo do tempo.
for sheet_name, df in dfs_modificados.items():
    print(f"Gráfico de linha para a evolução das vendas na aba: {sheet_name}")

    if garantir_coluna_data(df, 'Data') and 'Vendas' in df.columns:
        df.sort_values(by='Data', inplace=True)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df['Data'], df['Vendas'], marker='o', linestyle='-', color='blue', label='Vendas')
        ax.set_title(f"Evolução das Vendas ao Longo do Tempo - {sheet_name}")
        ax.set_xlabel("Data")
        ax.set_ylabel("Vendas")
        ax.legend()
        ax.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        salvar_grafico(fig, f"linha_vendas_{sheet_name}.png")
    else:
        print("Colunas 'Data' e/ou 'Vendas' não encontradas ou inválidas nesta aba.\n")

# Exercício 17: Calcule a média móvel de uma coluna de 
# séries temporais e plote-a junto com os dados originais.
for sheet_name, df in dfs_modificados.items():
    print(f"Gráfico de média móvel para a aba: {sheet_name}")

    if garantir_coluna_data(df, 'Data') and 'Vendas' in df.columns:
        df.sort_values(by='Data', inplace=True)

        janela = 7  
        df['Média Móvel'] = df['Vendas'].rolling(window=janela, min_periods=1).mean()

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df['Data'], df['Vendas'], marker='o', linestyle='-', color='blue', label='Vendas')
        ax.plot(df['Data'], df['Média Móvel'], linestyle='--', color='red', label=f'Média Móvel ({janela} dias)')
        ax.set_title(f"Evolução das Vendas com Média Móvel - {sheet_name}")
        ax.set_xlabel("Data")
        ax.set_ylabel("Vendas")
        ax.legend()
        ax.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        salvar_grafico(fig, f"media_movel_{sheet_name}.png")
    else:
        print("Colunas 'Data' e/ou 'Vendas' não encontradas ou inválidas nesta aba.\n")
