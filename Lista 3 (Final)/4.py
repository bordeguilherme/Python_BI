# 4. Visualização de dados

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

sns.set(style="whitegrid")
os.makedirs("Visualizacoes", exist_ok=True)

xls = pd.ExcelFile('VendasDiarias.xlsx')
dfs_modificados = {sheet: pd.read_excel(xls, sheet_name=sheet, header=0) for sheet in xls.sheet_names}

def salvar_grafico(fig, nome):
    caminho = os.path.join("Visualizacoes", nome)
    fig.savefig(caminho)
    plt.close(fig)

# Exercício 9: Crie um gráfico de barras para exibir a 
# quantidade de vendas de cada funcionário.
for sheet_name, df in dfs_modificados.items():
    print(f"Gráfico de barras para a aba: {sheet_name}")
    if 'Funcionário' in df.columns and 'Vendas' in df.columns:
        vendas_por_funcionario = df.groupby('Funcionário')['Vendas'].sum()
        
        fig, ax = plt.subplots(figsize=(10, 6))
        vendas_por_funcionario.sort_values(ascending=False).plot(kind='bar', color='skyblue', ax=ax)
        ax.set_title(f"Quantidade de Vendas por Funcionário - {sheet_name}")
        ax.set_xlabel("Funcionário")
        ax.set_ylabel("Quantidade de Vendas")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        
        salvar_grafico(fig, f"barras_{sheet_name}.png")
    else:
        print("Colunas 'Funcionário' e/ou 'Vendas' não encontradas nesta aba.\n")

# Exercício 10: Faça um histograma para mostrar a distribuição
# dos valores de uma coluna numérica.
for sheet_name, df in dfs_modificados.items():
    print(f"Histograma para a aba: {sheet_name}")
    colunas_numericas = df.select_dtypes(include=['number'])
    
    for coluna in colunas_numericas.columns:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(df[coluna], bins=20, kde=True, color='blue', ax=ax)
        ax.set_title(f"Distribuição dos valores - {coluna} ({sheet_name})")
        ax.set_xlabel(coluna)
        ax.set_ylabel("Frequência")
        
        salvar_grafico(fig, f"histograma_{sheet_name}_{coluna}.png")

# Exercício 11: Plote um gráfico de dispersão (scatter plot) 
# entre duas variáveis numéricas para investigar a relação entre elas.
for sheet_name, df in dfs_modificados.items():
    print(f"Gráfico de dispersão para a aba: {sheet_name}")
    colunas_numericas = df.select_dtypes(include=['number'])
    
    if colunas_numericas.shape[1] < 2:
        print("Menos de duas colunas numéricas disponíveis para criar um gráfico de dispersão.\n")
        continue

    x_col, y_col = colunas_numericas.columns[:2]
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x=x_col, y=y_col, color='purple', s=50, ax=ax)
    ax.set_title(f"Relação entre {x_col} e {y_col} ({sheet_name})")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    
    salvar_grafico(fig, f"dispersao_{sheet_name}.png")

# Exercício 12: Use o Seaborn para criar um heatmap de 
# correlações entre diferentes colunas numéricas.
for sheet_name, df in dfs_modificados.items():
    print(f"Heatmap de correlações para a aba: {sheet_name}")
    colunas_numericas = df.select_dtypes(include=['number'])
    
    if colunas_numericas.empty:
        print("Nenhuma coluna numérica encontrada para criar o heatmap de correlação.\n")
        continue

    correlacao = colunas_numericas.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlacao, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, square=True, ax=ax)
    ax.set_title(f"Heatmap de Correlações - {sheet_name}")
    
    salvar_grafico(fig, f"heatmap_{sheet_name}.png")
