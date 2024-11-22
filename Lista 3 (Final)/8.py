# 8. Análise estatística

import pandas as pd
from scipy import stats
import numpy as np

xls = pd.ExcelFile('VendasDiarias.xlsx')
dfs_modificados = {}

for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name, header=0)
    dfs_modificados[sheet_name] = df

# Exercício 24: Utilize a biblioteca scipy.stats para realizar 
# um teste de hipóteses simples (por exemplo, teste t ou teste de proporções).
for sheet_name, df in dfs_modificados.items():
    print(f"Teste de hipóteses para a aba: {sheet_name}\n")

    if 'Vendas' in df.columns:
        vendas = df['Vendas'].dropna().values 
        media_hipotese = 500
        t_stat, p_value = stats.ttest_1samp(vendas, media_hipotese)
        
        print(f"Teste t de uma amostra:")
        print(f"Estatística t: {t_stat:.2f}")
        print(f"Valor p: {p_value:.4f}")
        if p_value < 0.05:
            print("Rejeitamos a hipótese nula (a média é significativamente diferente de 500).\n")
        else:
            print("Não rejeitamos a hipótese nula (não há evidências suficientes para concluir que a média é diferente de 500).\n")
    else:
        print("Coluna 'Vendas' não encontrada nesta aba.\n")

# Exercício 25: Crie um intervalo de confiança para a média de uma amostra
for sheet_name, df in dfs_modificados.items():
    print(f"Intervalo de confiança para a aba: {sheet_name}\n")

    if 'Vendas' in df.columns:
        vendas = df['Vendas'].dropna().values 
        media = np.mean(vendas)
        desvio_padrao = np.std(vendas, ddof=1)
        n = len(vendas)
        confianca = 0.95
        z = stats.norm.ppf(1 - (1 - confianca) / 2)
        margem_erro = z * (desvio_padrao / np.sqrt(n))
        intervalo = (media - margem_erro, media + margem_erro)
        
        print(f"Média: {media:.2f}")
        print(f"Intervalo de confiança (95%): ({intervalo[0]:.2f}, {intervalo[1]:.2f})\n")
    else:
        print("Coluna 'Vendas' não encontrada nesta aba.\n")
