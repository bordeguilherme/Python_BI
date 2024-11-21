import pandas as pd

# Recarregando os dados para garantir que dfs_modificados exista
xls = pd.ExcelFile('VendasDiarias.xlsx')
dfs_modificados = {}

# Exemplo de carregamento simples das abas em dfs_modificados
for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name, header=0)
    dfs_modificados[sheet_name] = df

# Exercício 5: Cálculo de estatísticas básicas
for sheet_name, df in dfs_modificados.items():
    print(f"Estatísticas para a aba: {sheet_name}\n")
    
    # Seleciona colunas numéricas
    colunas_numericas = df.select_dtypes(include=['number'])
    
    if colunas_numericas.empty:
        print("Nenhuma coluna numérica encontrada nesta aba.\n")
        continue
    
    # Calcula as métricas solicitadas
    for coluna in colunas_numericas.columns:
        print(f"Coluna: {coluna}")
        print(f"Média: {colunas_numericas[coluna].mean():.2f}")
        print(f"Mediana: {colunas_numericas[coluna].median():.2f}")
        # Verifica se há moda para evitar erros
        if not colunas_numericas[coluna].mode().empty:
            print(f"Moda: {colunas_numericas[coluna].mode().iloc[0]:.2f}")
        else:
            print("Moda: Não disponível (todas as observações são únicas)")
        print(f"Valor mínimo: {colunas_numericas[coluna].min():.2f}")
        print(f"Valor máximo: {colunas_numericas[coluna].max():.2f}")
        print("-" * 30)
    print("\n" + "=" * 50 + "\n")

# Exercício 6: Correlação entre colunas numéricas
for sheet_name, df in dfs_modificados.items():
    print(f"Correlação entre colunas numéricas na aba: {sheet_name}\n")
    
    # Seleciona colunas numéricas
    colunas_numericas = df.select_dtypes(include=['number'])
    
    if colunas_numericas.empty:
        print("Nenhuma coluna numérica encontrada para calcular a correlação.\n")
        continue
    
    # Calcula a matriz de correlação e formata os valores para duas casas decimais
    correlacao = colunas_numericas.corr().round(2)
    print(correlacao)
    print("\n" + "=" * 50 + "\n")
