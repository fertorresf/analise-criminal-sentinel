import pandas as pd
from sklearn.linear_model import LinearRegression

def criar_modelo_preditivo(df):
    """
    Cria e avalia um modelo de regressão linear para prever ocorrências.

    Args:
        df (pd.DataFrame): DataFrame com os dados limpos e pré-processados.

    Returns:
        sklearn.linear_model.LinearRegression: Modelo de regressão linear treinado.
    """

    # Separar as variáveis explicativas e a variável resposta
    X = df.iloc[:, 1:13]
    y = df['Total_Ocorrencias']

    # Criar o modelo de regressão linear
    model = LinearRegression()

    # Treinar o modelo
    model.fit(X, y)

    return model
