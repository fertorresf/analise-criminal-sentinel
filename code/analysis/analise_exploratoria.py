import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def realizar_analise_exploratoria(df):
    """
    Realiza a análise exploratória dos dados e gera visualizações.

    Args:
        df (pd.DataFrame): DataFrame com os dados limpos e pré-processados.
    """

    # Analisando Distribuição de Ocorrências
    # Total de Ocorrências por Mês
    plt.figure(figsize=(12, 6))
    sns.barplot(x=df.columns[1:13], y=df.iloc[:, 1:13].sum())
    plt.title("Total de Ocorrências por Mês")
    plt.xlabel("Mês")
    plt.ylabel("Número de Ocorrências")
    plt.show()

    # Total de Ocorrências por Trimestre
    plt.figure(figsize=(12, 6))
    sns.barplot(x=['1º Trimestre', '2º Trimestre', '3º Trimestre', '4º Trimestre'], 
               y=[df['Total_Primeiro_Trimestre'].sum(), df['Total_Segundo_Trimestre'].sum(), 
                  df['Total_Terceiro_Trimestre'].sum(), df['Total_Quarto_Trimestre'].sum()])
    plt.title("Total de Ocorrências por Trimestre")
    plt.xlabel("Trimestre")
    plt.ylabel("Número de Ocorrências")
    plt.show()

    # Distribuição de Ocorrências por Categoria
    plt.figure(figsize=(12, 6))
    sns.countplot(x='Categoria_Crime_Resumida', data=df)
    plt.title("Distribuição de Ocorrências por Categoria de Crime")
    plt.xlabel("Categoria de Crime")
    plt.ylabel("Número de Ocorrências")
    plt.show()

    # Analisando Tendências ao Longo do Ano
    # Tendência de Ocorrências por Mês
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=df.columns[1:13], y=df.iloc[:, 1:13].sum(), marker='o')
    plt.title("Tendência de Ocorrências por Mês")
    plt.xlabel("Mês")
    plt.ylabel("Número de Ocorrências")
    plt.show()

    # Tendência de Ocorrências por Trimestre
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=['1º Trimestre', '2º Trimestre', '3º Trimestre', '4º Trimestre'], 
               y=[df['Total_Primeiro_Trimestre'].sum(), df['Total_Segundo_Trimestre'].sum(), 
                  df['Total_Terceiro_Trimestre'].sum(), df['Total_Quarto_Trimestre'].sum()], marker='o')
    plt.title("Tendência de Ocorrências por Trimestre")
    plt.xlabel("Trimestre")
    plt.ylabel("Número de Ocorrências")
    plt.show()

    # Analisando Correlação entre Variáveis
    # Matriz de Correlação
    plt.figure(figsize=(12, 6))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Matriz de Correlação")
    plt.show()

    # Analisando Ocorrências por Tipo de Crime
    # Total de Ocorrências por Tipo de Crime
    plt.figure(figsize=(12, 6))
    sns.barplot(y=df['Natureza'].value_counts().index, x=df['Natureza'].value_counts().values)
    plt.title("Total de Ocorrências por Tipo de Crime")
    plt.xlabel("Número de Ocorrências")
    plt.ylabel("Tipo de Crime")
    plt.show()
