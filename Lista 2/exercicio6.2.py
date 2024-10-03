# 6 - Mapeamento de Dados Geográficos
# 6.2 - Mapa de Calor:
# Crie um mapa de calor para visualizar a densidade dos pontos usando a biblioteca
# folium e plotly.

import pandas as pd
import folium
from folium.plugins import HeatMap
import plotly.express as px

df = pd.read_csv('./local_6.csv')

m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=13)

heat_data = [[row['Latitude'], row['Longitude']] for index, row in df.iterrows()]

HeatMap(heat_data).add_to(m)

m.save("mapa_de_calor.html")

fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name="Nome",
                        hover_data=["Categoria"], zoom=13, height=500)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig.show()

print("O mapa de calor foi salvo como 'mapa_de_calor.html' e o gráfico interativo foi exibido.")
