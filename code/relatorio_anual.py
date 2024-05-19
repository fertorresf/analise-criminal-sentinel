import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def gerar_relatorio_anual(df, modelo):
    """
    Gera um relatório anual em PDF com os resultados da análise.

    Args:
        df (pd.DataFrame): DataFrame com os dados limpos e pré-processados.
        modelo (sklearn.linear_model.LinearRegression): Modelo de regressão linear treinado.
    """

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Relatório Anual de Ocorrências Criminais em Lins", 0, 1, "C")
    pdf.set_font("Arial", "", 12)

    # Adicionar informações gerais
    pdf.cell(0, 10, f"Ano: {df['Ano'].iloc[0]}", 0, 1)

    # Adicionar gráficos da análise exploratória
    with PdfPages("reports/relatorio_anual.pdf") as pdf_pages:
        plt.figure(figsize=(12, 6))
        sns.barplot(x=df.columns[1:13], y=df.iloc[:, 1:13].sum())
        plt.title("Total de Ocorrências por Mês")
        plt.xlabel("Mês")
        plt.ylabel("Número de Ocorrências")
        pdf_pages.savefig(bbox_inches='tight')
        plt.close()

        # ... (adicionar os outros gráficos da análise exploratória)

    # Adicionar informações sobre o modelo preditivo
    pdf.cell(0, 10, "Modelo Preditivo", 0, 1)
    pdf.cell(0, 10, f"R²: {modelo.score(df.iloc[:, 1:13], df['Total_Ocorrencias'])}", 0, 1)

    # Adicionar informações sobre a clusterização (se disponível)
    # ... 

    pdf.output("reports/relatorio_anual.pdf")
