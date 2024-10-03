# 6 - Mapeamento de Dados Geográficos
# 6.1 - Leitura de Dados Geoespaciais:
# Encontre um arquivo CSV com dados geoespaciais (como localização de pontos de interesse).
# Leia os dados com pandas.

import pandas as pd

df = pd.read_csv('./local_6.csv')

print(df.head())
