import pandas as pd

# Recarregando os dados para garantir que dfs_modificados exista
xls = pd.ExcelFile('VendasDiarias.xlsx')
dfs_modificados = {}

# Exemplo de carregamento simples das abas em dfs_modificados
for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name, header=0)
    dfs_modificados[sheet_name] = df

# Exercício 7: Ordenação dos dados e exibição do Top 10
for sheet_name, df in dfs_modificados.items():
    print(f"Ordenando os dados na aba: {sheet_name}")
    
    # Verifica se há colunas numéricas para ordenar
    colunas_numericas = df.select_dtypes(include=['number'])
    if colunas_numericas.empty:
        print("Nenhuma coluna numérica encontrada para ordenação.\n")
        continue
    
    # Define uma coluna para ordenação (ajustar para a coluna desejada, por exemplo 'Vendas')
    coluna_para_ordenar = colunas_numericas.columns[0]  # Substituir pelo nome da coluna desejada, se necessário
    print(f"Coluna selecionada para ordenação: {coluna_para_ordenar}")
    
    # Ordena o DataFrame
    df_ordenado = df.sort_values(by=coluna_para_ordenar, ascending=False)
    
    # Exibe o Top 10
    print(f"Top 10 maiores valores da coluna '{coluna_para_ordenar}':\n")
    print(df_ordenado.head(10))
    print("\n" + "=" * 50 + "\n")

# Exercício 8: Filtro de linhas com base em valores de uma coluna
limite_superior = 1000  # Substituir pelo limite desejado
for sheet_name, df in dfs_modificados.items():
    print(f"Filtrando dados na aba: {sheet_name}")
    
    # Verifica se há colunas numéricas para aplicar o filtro
    colunas_numericas = df.select_dtypes(include=['number'])
    if colunas_numericas.empty:
        print("Nenhuma coluna numérica encontrada para aplicar o filtro.\n")
        continue
    
    # Define uma coluna para o filtro (ajustar para a coluna desejada, por exemplo 'Vendas')
    coluna_para_filtrar = colunas_numericas.columns[0]  # Substituir pelo nome da coluna desejada, se necessário
    print(f"Coluna selecionada para o filtro: {coluna_para_filtrar}")
    
    # Aplica o filtro (valores acima do limite superior)
    df_filtrado = df[df[coluna_para_filtrar] > limite_superior]
    
    # Exibe o resultado do filtro
    print(f"Linhas com valores acima de {limite_superior} na coluna '{coluna_para_filtrar}':\n")
    print(df_filtrado)
    print("\n" + "=" * 50 + "\n")


