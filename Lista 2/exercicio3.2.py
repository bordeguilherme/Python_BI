# 3 - Análise de Dados de Pesquisa
# 3.2 - Gráfico de Pizza:
# Crie um gráfico de pizza para mostrar a distribuição de uma variável categórica
# usando a biblioteca matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

arquivo_csv = './arquivo_3.csv'
dados = pd.read_csv(arquivo_csv)

distribuicao_marca = dados['Marca'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(distribuicao_marca, labels=distribuicao_marca.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'orange', 'pink'])

plt.title('Distribuição de Marcas de Smartphones')
plt.axis('equal') 

plt.show()
