# 5 - Histograma de Dados
# 5.2 - Histograma:
# Crie um histograma para visualizar a distribuição dos dados numéricos usando matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = './escola_5.csv'

df = pd.read_csv(csv_file_path)

plt.hist(df['Nota'], bins=5, edgecolor='black')

plt.title('Distribuição de Notas dos Estudantes')
plt.xlabel('Notas')
plt.ylabel('Frequência')

plt.show()
