# 5 - Histograma de Dados
# 5.1 - Leitura e Limpeza de Dados:
# Encontre um arquivo CSV com dados numéricos (como notas de estudantes, por exemplo).
# Leia os dados utilizando pandas.

import pandas as pd

csv_file_path = './escola_5.csv'

df = pd.read_csv(csv_file_path)

print(df.head())
