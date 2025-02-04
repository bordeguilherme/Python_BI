# 3. Manipulação de dados com Pandas

import pandas as pd
import os

xls = pd.ExcelFile('VendasDiarias.xlsx')
dfs_modificados = {}

for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name, header=0)
    dfs_modificados[sheet_name] = df

# Diretório para salvar resultados
os.makedirs("Resultados_Manipulacao", exist_ok=True)

# Exercício 7: Ordene os dados com base em uma ou mais colunas e exiba o top 10 de maiores valores.
for sheet_name, df in dfs_modificados.items():
    print(f"Ordenando os dados na aba: {sheet_name}")
    
    colunas_numericas = df.select_dtypes(include=['number'])
    if colunas_numericas.empty:
        print("Nenhuma coluna numérica encontrada para ordenação.\n")
        continue

    for coluna_para_ordenar in colunas_numericas.columns:
        print(f"Coluna selecionada para ordenação: {coluna_para_ordenar}")
        
        df_ordenado = df.sort_values(by=coluna_para_ordenar, ascending=False)
        print(f"Top 10 maiores valores da coluna '{coluna_para_ordenar}':\n")
        print(df_ordenado.head(10))

        df_ordenado.head(10).to_csv(f"Resultados_Manipulacao/Top10_{sheet_name}_{coluna_para_ordenar}.csv", index=False)

    print("\n" + "=" * 50 + "\n")

# Exercício 8: Filtre as linhas de um dataframe onde os valores 
# de uma coluna estejam acima ou abaixo de um determinado limite.
limite_superior = 1000  
for sheet_name, df in dfs_modificados.items():
    print(f"Filtrando dados na aba: {sheet_name}")

    colunas_numericas = df.select_dtypes(include=['number'])
    if colunas_numericas.empty:
        print("Nenhuma coluna numérica encontrada para aplicar o filtro.\n")
        continue

    for coluna_para_filtrar in colunas_numericas.columns:
        print(f"Coluna selecionada para o filtro: {coluna_para_filtrar}")
        
        df_filtrado = df[df[coluna_para_filtrar] > limite_superior]
        print(f"Linhas com valores acima de {limite_superior} na coluna '{coluna_para_filtrar}':\n")
        print(df_filtrado)

        df_filtrado.to_csv(f"Resultados_Manipulacao/Filtrados_{sheet_name}_{coluna_para_filtrar}.csv", index=False)

    print("\n" + "=" * 50 + "\n")
