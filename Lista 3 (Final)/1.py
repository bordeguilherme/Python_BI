# 1. Importação e limpeza de dados

import pandas as pd

xls = pd.ExcelFile('VendasDiarias.xlsx')
dfs_modificados = {}
colunas_renomeadas = {
    'Data_Unnamed: 0_level_1': 'Data',
    'Planejamento Futuro_Unnamed: 9_level_1': 'Planejamento Futuro',
    'Tendência_Unnamed: 10_level_1': 'Tendência',
    'Clientes Abordados_Unnamed: 12_level_1': 'Clientes Abordados',
    'Vendas Fechadas_Unnamed: 13_level_1': 'Vendas Fechadas',
    'Taxa de Conversão_Unnamed: 14_level_1': 'Taxa de Conversão'
}

for sheet_name in xls.sheet_names:
    
    # Exercício 1: Importe um conjunto de dados XLSX 
    # (VendasDiarias.xlsx disponibilizado) usando pandas. Exiba as primeiras 5 linhas de cada planilha.
    df = pd.read_excel(xls, sheet_name=sheet_name, header=[4, 5])

    print(f"Aba: {sheet_name}")
    print("Primeiras linhas do dataframe:")
    print(df.head(), "\n")

    colunas_faltantes = set(colunas_renomeadas.keys()) - set(df.columns)
    if colunas_faltantes:
        print(f"Colunas faltantes na aba {sheet_name}: {colunas_faltantes}\n")
    
    # Exercício 2: Verifique se há valores ausentes nos dados e substitua-os ou remova-os.
    missing_values = df.isnull().sum()
    if missing_values.any():
        print(f"Aba: {sheet_name} - Valores ausentes detectados:")
        print(missing_values[missing_values > 0], "\n")

    df.fillna(0, inplace=True)
    
    # Exercício 3: Renomeie colunas de um dataframe para nomes 
    # mais significativos e remova colunas irrelevantes.
    df.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in df.columns]
    df.rename(columns={col: new_col for col, new_col in colunas_renomeadas.items() if col in df.columns}, inplace=True)
    
    # Exercício 4: Converta a coluna de datas em um formato 
    # adequado e crie novas colunas para o dia, mês e ano.
    for col in df.columns:
        if 'Data' in col:
            print(f"Coluna de Data encontrada: {col}")
            df[col] = pd.to_datetime(df[col], errors='coerce')

            if df[col].isnull().any():
                print(f"Existem valores inválidos na coluna 'Data' na aba {sheet_name}\n")
                df.dropna(subset=[col], inplace=True)  

            df['Dia'] = df[col].dt.day
            df['Mês'] = df[col].dt.month
            df['Ano'] = df[col].dt.year
            break

    df = df.loc[:, (df != '').any(axis=0)]

    print(f"Resumo estatístico da aba {sheet_name}:")
    print(df.describe(), "\n")
    
    dfs_modificados[sheet_name] = df

output_file = 'VendasDiarias_Modificadas.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for sheet_name, df in dfs_modificados.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Arquivo '{output_file}' criado com sucesso!")
