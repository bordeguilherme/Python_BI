# 1 - Leitura e Visualização de Dados Simples
# 1.2 - Gráfico de Linha:
# Crie um gráfico de linha mostrando a evolução de uma variável ao longo do tempo
# usando a biblioteca matplotlib. Adicione rótulos aos eixos e um título ao gráfico.

import pandas as pd
import matplotlib.pyplot as plt

arquivo_csv = './vendas_1.csv'

df = pd.read_csv(arquivo_csv)

plt.plot(df['Data'], df['Vendas'], marker='o')

plt.xlabel('Data')
plt.ylabel('Vendas')
plt.title('Evolução das Vendas ao Longo do Tempo')

plt.xticks(rotation=45)

plt.tight_layout() 
plt.show()
