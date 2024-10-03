# 2 - Análise de Dados Financeiros
# 2.2 - Gráfico de Velas (Candlestick):
# Crie um gráfico de velas para os dados financeiros utilizando a biblioteca plotly ou
# mplfinance e mostre a variação do preço das ações ao longo do tempo.

import pandas as pd
import mplfinance as mpf

df = pd.read_csv('./dados_2.csv')

df['Data'] = pd.to_datetime(df['Data'])

df.set_index('Data', inplace=True)

mpf.plot(df, type='candle', style='charles', volume=True, title='Gráfico de Velas - Preço das Ações', ylabel='Preço')

