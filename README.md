# analise-criminal-sentinel [ desenvolvendo ]

- Introdução ao projeto, objetivo da análise e breve descrição dos dados.
- Informações sobre a fonte dos dados e links para os arquivos originais.
- Descrição das ferramentas e bibliotecas usadas no projeto.
- Exemplos de visualizações e insights obtidos da análise.
- Contribuições e informações para colaboração.

# data/:
- raw/: Arquivos brutos baixados dos sites oficiais (ex: OcorrenciaMensal(Criminal)-Lins_20240518_144046.xlsx, etc).
- processed/: Arquivos processados e limpos (ex: dados_limpos.csv).
# code/:
- base_main.py É o arquivo principal que chama as funções dos outros pacotes e realiza a análise completa.
- relatorio_anual.py Contém funções para gerar o relatório anual em PDF com os resultados da análise.
- cleaning/: Scripts para a limpeza e organização dos dados (ex: limpar_dados.py).
  - limpar_dados.py: Contém funções para limpar e pré-processar os dados brutos. 
- analysis/: Scripts para análise exploratória e modelagem (ex: analise_exploratoria.py, modelo_preditivo.py).
  - analise_exploratoria.py: Contém funções para análise exploratória e visualização dos dados.
    - Função realizar_analise_exploratoria:
      Recebe o DataFrame com os dados limpos e pré-processados como argumento.

      Realiza os seguintes tipos de análise:

      - Distribuição de Ocorrências:
       - Cria gráficos de barras para visualizar o total de ocorrências por mês, trimestre e categoria de crime.

      - Tendências:
       - Cria gráficos de linhas para observar a tendência de ocorrências por mês e por trimestre.

      - Correlação:
       - Cria uma matriz de correlação e utiliza um mapa de calor para visualizar a força da correlação entre as variáveis.

      - Ocorrências por Tipo de Crime:
       - Cria um gráfico de barras para visualizar o número de ocorrências por tipo de crime.
       - Exibe os gráficos utilizando plt.show().
         
  - modelo_preditivo.py: Contém funções para criar e avaliar modelos preditivos.  
# visualization/:
- plots/: Gráficos e visualizações criadas (ex: grafico_ocorrencias.png).
# documentation/:
- reports/: Relatórios com insights e conclusões da análise (ex: relatorio_anual.pdf).
# requirements.txt: Lista das bibliotecas usadas no projeto.
Certifique-se de instalar as bibliotecas listadas no requirements.txt usando pip install -r requirements.txt.
Execute o script code/base_main.py para rodar a análise completa e gerar o relatório.
