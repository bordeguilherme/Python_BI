# 2 - Análise de Dados Financeiros
# 2.1 - Leitura de Dados Financeiros:
# Encontre ou crie um arquivo CSV com dados financeiros, como cotações diárias de ações.
# Leia os dados usando pandas e mostre um gráfico em linhas de uma ação, ouro, dólar, ...

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./dados_2.csv')

print(df.head())

df['Data'] = pd.to_datetime(df['Data'])

plt.figure(figsize=(10, 5))
plt.plot(df['Data'], df['Fechamento'], marker='o')

plt.title('Preço de Fechamento ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')

plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
