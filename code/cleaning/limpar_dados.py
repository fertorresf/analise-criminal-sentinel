import pandas as pd

def limpar_dados(path):
    """
    Carrega, limpa e pré-processa os dados brutos.

    Args:
        path (str): Caminho para a pasta com os arquivos brutos.

    Returns:
        pd.DataFrame: DataFrame com os dados limpos e pré-processados.
    """

    files = [
        "OcorrenciaMensal(Criminal)-Lins_20240518_144046.xlsx",
        "OcorrenciaMensal(Criminal)-Lins_20240518_144147.xlsx",
        "OcorrenciaMensal(Criminal)-Lins_20240518_144203.xlsx",
        "OcorrenciaMensal(Criminal)-Lins_20240518_144207.xlsx",
        "OcorrenciaMensal(Criminal)-Lins_20240518_144212.xlsx",
    ]

    dfs = []
    for file in files:
        df = pd.read_excel(path + file)
        dfs.append(df)

    df_total = pd.concat(dfs, ignore_index=True)

    # Limpeza e pré-processamento
    df_total = df_total.drop(columns=["Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO", "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO", "Nº DE VÍTIMAS EM LATROCÍNIO"])
    df_total = df_total.rename(columns={"TOTAL DE ESTUPRO (4)": "TOTAL_ESTUPRO", "TOTAL DE ROUBO - OUTROS (1)": "TOTAL_ROUBO_OUTROS", "HOMICÍDIO DOLOSO (2)": "HOMICIDIO_DOLOSO"})
    df_total = df_total.replace(",", ".", regex=True)
    df_total = df_total.apply(pd.to_numeric, errors='coerce')
    df_total = df_total.fillna(0)
    df_total["Ano"] = 2024 

    return df_total
