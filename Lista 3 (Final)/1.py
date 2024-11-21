import pandas as pd

# Exercício 1: Importação de dados
# Carrega o arquivo Excel
xls = pd.ExcelFile('VendasDiarias.xlsx')

# Dicionário para armazenar DataFrames modificados
dfs_modificados = {}

# Mapeamento de renomeação de colunas
colunas_renomeadas = {
    'Data_Unnamed: 0_level_1': 'Data',
    'Planejamento Futuro_Unnamed: 9_level_1': 'Planejamento Futuro',
    'Tendência_Unnamed: 10_level_1': 'Tendência',
    'Clientes Abordados_Unnamed: 12_level_1': 'Clientes Abordados',
    'Vendas Fechadas_Unnamed: 13_level_1': 'Vendas Fechadas',
    'Taxa de Conversão_Unnamed: 14_level_1': 'Taxa de Conversão'
}

# Itera sobre as abas do Excel
for sheet_name in xls.sheet_names:
    # Exercício 1: Importação de cada aba do Excel
    df = pd.read_excel(xls, sheet_name=sheet_name, header=[4, 5])
    
    print(f"Aba: {sheet_name}")
    print("Primeiras linhas do dataframe:")
    print(df.head(), "\n")
    
    # Exercício 2: Verificação e tratamento de valores ausentes
    missing_values = df.isnull().sum()
    if missing_values.any():
        print(f"Aba: {sheet_name} - Valores ausentes detectados:")
        print(missing_values[missing_values > 0], "\n")
    
    # Preenche valores ausentes restantes com zero
    df.fillna(0, inplace=True)
    
    # Exercício 3: Renomeação de colunas
    # Junta os níveis de cabeçalho e renomeia colunas para nomes mais significativos
    df.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in df.columns]
    df.rename(columns={col: new_col for col, new_col in colunas_renomeadas.items() if col in df.columns}, inplace=True)
    
    # Exercício 4: Manipulação de colunas de data
    # Identifica e processa a coluna de datas, se existir
    for col in df.columns:
        if 'Data' in col:
            print(f"Coluna de Data encontrada: {col}")
            df[col] = pd.to_datetime(df[col], errors='coerce')
            
            if df[col].isnull().any():
                print(f"Existem valores inválidos na coluna 'Data' na aba {sheet_name}\n")
            
            # Adiciona colunas de Dia, Mês e Ano
            df['Dia'] = df[col].dt.day
            df['Mês'] = df[col].dt.month
            df['Ano'] = df[col].dt.year
            break

    # Remove colunas irrelevantes (exemplo: com todas as células vazias ou sem significado)
    df = df.loc[:, (df != '').any(axis=0)]
    
    # Armazena o DataFrame modificado
    dfs_modificados[sheet_name] = df

# Salva os DataFrames modificados em um novo arquivo Excel
output_file = 'VendasDiarias_Modificadas.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for sheet_name, df in dfs_modificados.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Arquivo '{output_file}' criado com sucesso!")
