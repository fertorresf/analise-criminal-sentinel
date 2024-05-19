import pandas as pd
from code.limpar_dados import limpar_dados
from code.analise_exploratoria import realizar_analise_exploratoria
from code.modelo_preditivo import criar_modelo_preditivo
from code.relatorio_anual import gerar_relatorio_anual

if __name__ == "__main__":
    path_dados = "data/raw/"

    # Carregando, limpando e pré-processando os dados
    df_total = limpar_dados(path_dados)
    df_total.to_csv("data/processed/dados_limpos.csv", index=False)

    # Realizando a análise exploratória
    realizar_analise_exploratoria(df_total)

    # Criando o modelo preditivo
    modelo = criar_modelo_preditivo(df_total)

    # Gerando o relatório anual
    gerar_relatorio_anual(df_total, modelo)
