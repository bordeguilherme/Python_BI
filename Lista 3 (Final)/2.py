# 2. Exploração e resumo dos dados

import pandas as pd
import os

xls = pd.ExcelFile('VendasDiarias.xlsx')
dfs_modificados = {}

for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name, header=0)
    dfs_modificados[sheet_name] = df

# Diretório para salvar resultados
os.makedirs("Resultados", exist_ok=True)

# Exercício 5: Calcule a média, mediana, moda, mínimo e máximo de colunas numéricas.
for sheet_name, df in dfs_modificados.items():
    print(f"Estatísticas para a aba: {sheet_name}\n")
    
    colunas_numericas = df.select_dtypes(include=['number'])
    
    if colunas_numericas.empty:
        print("Nenhuma coluna numérica encontrada nesta aba.\n")
        continue
    
    stats = []
    for coluna in colunas_numericas.columns:
        moda = colunas_numericas[coluna].mode()
        moda_valores = moda.tolist()
        
        stats.append({
            "Coluna": coluna,
            "Média": colunas_numericas[coluna].mean(),
            "Mediana": colunas_numericas[coluna].median(),
            "Moda": moda_valores,
            "Mínimo": colunas_numericas[coluna].min(),
            "Máximo": colunas_numericas[coluna].max(),
        })

    stats_df = pd.DataFrame(stats)
    stats_df.to_csv(f"Resultados/Estatisticas_{sheet_name}.csv", index=False)
    
    print(stats_df)
    print("\n" + "=" * 50 + "\n")

# Exercício 6: Encontre a correlação entre diferentes colunas numéricas do conjunto de dados.
for sheet_name, df in dfs_modificados.items():
    print(f"Correlação entre colunas numéricas na aba: {sheet_name}\n")
    
    colunas_numericas = df.select_dtypes(include=['number'])
    
    if colunas_numericas.empty:
        print("Nenhuma coluna numérica encontrada para calcular a correlação.\n")
        continue

    correlacao = colunas_numericas.corr().round(2)

    correlacao.to_csv(f"Resultados/Correlacao_{sheet_name}.csv")
    
    print(correlacao)
    print("\n" + "=" * 50 + "\n")
