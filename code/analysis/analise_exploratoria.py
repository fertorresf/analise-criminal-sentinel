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

    # ... (continuar com as outras visualizações do passo 4)
