# 4 - Análise de Dados de Vendas
# 4.2 - Gráfico de Linhas Múltiplas:
# Crie um gráfico de linhas múltiplas para comparar vendas de diferentes produtos ao
# longo do tempo usando matplotlib e seaborn.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = './data_4.csv'
df = pd.read_csv(file_path)

df['Date'] = pd.to_datetime(df['Date'])

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))

sns.lineplot(data=df, x='Date', y='Units Sold', hue='Product', marker='o')

plt.title('Comparação de Vendas de Diferentes Produtos ao Longo do Tempo', fontsize=14)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Unidades Vendidas', fontsize=12)
plt.xticks(rotation=45)  

plt.tight_layout()
plt.show()
