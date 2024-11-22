# 8. Análise estatística

import pandas as pd
from scipy import stats
import numpy as np
import os

xls = pd.ExcelFile('VendasDiarias.xlsx')
dfs_modificados = {sheet: pd.read_excel(xls, sheet_name=sheet, header=0) for sheet in xls.sheet_names}

os.makedirs("Analise_Estatistica", exist_ok=True)

def teste_t_uma_amostra(vendas, media_hipotese):
    t_stat, p_value = stats.ttest_1samp(vendas, media_hipotese)
    return t_stat, p_value

def calcular_intervalo_confianca(vendas, confianca=0.95):
    media = np.mean(vendas)
    desvio_padrao = np.std(vendas, ddof=1)
    n = len(vendas)
    z = stats.norm.ppf(1 - (1 - confianca) / 2)
    margem_erro = z * (desvio_padrao / np.sqrt(n))
    intervalo = (media - margem_erro, media + margem_erro)
    return media, intervalo

# Exercício 24: Utilize a biblioteca scipy.stats para realizar um 
# teste de hipóteses simples (por exemplo, teste t ou teste de proporções).
for sheet_name, df in dfs_modificados.items():
    print(f"Teste de hipóteses para a aba: {sheet_name}\n")

    if 'Vendas' in df.columns:
        vendas = df['Vendas'].dropna().values
        if len(vendas) > 1:
            media_hipotese = 500
            t_stat, p_value = teste_t_uma_amostra(vendas, media_hipotese)
            
            print(f"Teste t de uma amostra:")
            print(f"Estatística t: {t_stat:.2f}")
            print(f"Valor p: {p_value:.4f}")
            interpretacao = (
                "Rejeitamos a hipótese nula (a média é significativamente diferente de 500)."
                if p_value < 0.05 else
                "Não rejeitamos a hipótese nula (não há evidências suficientes para concluir que a média é diferente de 500)."
            )
            print(interpretacao, "\n")

            pd.DataFrame([{"Estatística t": t_stat, "Valor p": p_value, "Interpretação": interpretacao}]).to_csv(
                f"Analise_Estatistica/Teste_t_{sheet_name}.csv", index=False
            )
        else:
            print("Dados insuficientes para realizar o teste t.\n")
    else:
        print("Coluna 'Vendas' não encontrada nesta aba.\n")

# Exercício 25: Crie um intervalo de confiança para a média de uma amostra
for sheet_name, df in dfs_modificados.items():
    print(f"Intervalo de confiança para a aba: {sheet_name}\n")

    if 'Vendas' in df.columns:
        vendas = df['Vendas'].dropna().values
        if len(vendas) > 1:
            media, intervalo = calcular_intervalo_confianca(vendas)
            
            print(f"Média: {media:.2f}")
            print(f"Intervalo de confiança (95%): ({intervalo[0]:.2f}, {intervalo[1]:.2f})\n")

            pd.DataFrame([{"Média": media, "Intervalo Inferior": intervalo[0], "Intervalo Superior": intervalo[1]}]).to_csv(
                f"Analise_Estatistica/Intervalo_Confianca_{sheet_name}.csv", index=False
            )
        else:
            print("Dados insuficientes para calcular o intervalo de confiança.\n")
    else:
        print("Coluna 'Vendas' não encontrada nesta aba.\n")
