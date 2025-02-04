# 5. Transformações e engenharia de dados

import pandas as pd
import os

xls = pd.ExcelFile('VendasDiarias.xlsx')
dfs_modificados = {sheet: pd.read_excel(xls, sheet_name=sheet, header=0) for sheet in xls.sheet_names}

os.makedirs("Transformacoes", exist_ok=True)

# Exercício 13: Crie uma nova coluna que seja uma transformação de 
# outras colunas (por exemplo, calcule a relação entre duas colunas numéricas).
for sheet_name, df in dfs_modificados.items():
    print(f"Criando nova coluna transformada para a aba: {sheet_name}")

    if 'Vendas' in df.columns and 'Clientes Abordados' in df.columns:
        df['Vendas por Cliente'] = df['Vendas'] / df['Clientes Abordados'].replace(0, float('nan'))
        print(f"Nova coluna 'Vendas por Cliente' criada com sucesso na aba: {sheet_name}\n")

        df.to_csv(f"Transformacoes/{sheet_name}_transformado.csv", index=False)
    else:
        print("Colunas 'Vendas' e/ou 'Clientes Abordados' não encontradas nesta aba.\n")

# Exercício 14: Aplique uma função personalizada em 
# uma coluna (vendas como "Altas", "Médias" ou "Baixas").
for sheet_name, df in dfs_modificados.items():
    print(f"Aplicando categorização na aba: {sheet_name}")

    if 'Vendas' in df.columns:
        def categorizar_vendas(venda, limites=(500, 1000)):
            if venda > limites[1]:
                return 'Alta'
            elif venda > limites[0]:
                return 'Média'
            else:
                return 'Baixa'

        df['Categoria de Vendas'] = df['Vendas'].apply(categorizar_vendas)
        print(f"Nova coluna 'Categoria de Vendas' criada com sucesso na aba: {sheet_name}\n")

        df.to_csv(f"Transformacoes/{sheet_name}_categorizado.csv", index=False)
    else:
        print("Coluna 'Vendas' não encontrada nesta aba.\n")

# Exercício 15: Realize um merge entre duas Planilhas com base em uma coluna comum.
if len(dfs_modificados) >= 2:
    sheet_names = list(dfs_modificados.keys())
    df1 = dfs_modificados[sheet_names[0]]
    df2 = dfs_modificados[sheet_names[1]]
    
    print(f"Realizando merge entre as abas: {sheet_names[0]} e {sheet_names[1]}")
    
    colunas_comuns = set(df1.columns).intersection(df2.columns)
    if 'Funcionário' in colunas_comuns:
        df_merge = pd.merge(df1, df2, on='Funcionário', suffixes=('_Planilha1', '_Planilha2'))
        dfs_modificados['Merge_Resultado'] = df_merge
        print(f"Merge realizado com sucesso! Resultado adicionado ao dicionário como 'Merge_Resultado'.\n")

        df_merge.to_csv("Transformacoes/Merge_Resultado.csv", index=False)
    else:
        print("Nenhuma coluna comum encontrada para realizar o merge.\n")
else:
    print("Menos de duas planilhas disponíveis para realizar o merge.\n")
