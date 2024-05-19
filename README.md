# analise-criminal-sentinel [desenvolvendo]

## Introdução

Este repositório contém um projeto de análise de dados de ocorrências criminais em Lins, SP. O objetivo é analisar os dados, identificar padrões e tendências, e gerar insights para auxiliar na compreensão da criminalidade na cidade.

## Descrição dos Dados

Os dados utilizados neste projeto são dados mensais de ocorrências criminais coletados do portal da Secretaria da Segurança Pública do Estado de São Paulo ([https://www.ssp.sp.gov.br/estatistica/dados-mensais](https://www.ssp.sp.gov.br/estatistica/dados-mensais)). Os dados abrangem o período de 2024 e incluem informações sobre o tipo de crime, o mês da ocorrência e o total de ocorrências.

## Ferramentas e Bibliotecas

O projeto utiliza as seguintes bibliotecas Python:

* **pandas:** Para manipulação e análise de dados.
* **matplotlib:** Para criação de gráficos.
* **seaborn:** Para visualização de dados estatísticos.
* **scipy:** Para testes estatísticos.
* **scikit-learn:** Para criação de modelos preditivos.
* **fpdf:** Para geração de relatórios em PDF.

## Exemplos de Visualizações e Insights

* **Gráfico de barras:**  Mostrando o total de ocorrências por mês.
* **Gráfico de linhas:**  Demonstrando a tendência de ocorrências ao longo do ano.
* **Matriz de correlação:**  Analisando a relação entre diferentes tipos de crime.
* **Modelo de regressão linear:**  Prevendo o número total de ocorrências em cada mês.

## Contribuições e Colaboração

Contribuições para este projeto são bem-vindas! Se você tiver interesse em colaborar, entre em contato com o autor do projeto ou abra um issue no repositório.

## Estrutura do Repositório

analise-criminal-sentinel/ <br>
├── data/ <br>
│ ├── raw/ <br>
│ │ └── OcorrenciaMensal(Criminal)-Lins_20240518_144046.xlsx \n
│ │ ... \n
│ └── processed/ \n
│ | └── dados_limpos.csv \n
├── code/ \n
│ ├── base_main.py \n
│ ├── relatorio_anual.py \n
│ ├── cleaning/ \n
│ │ └── limpar_dados.py \n
│ ├── analysis/ \n
│ │ ├── analise_exploratoria.py \n
│ │ └── modelo_preditivo.py \n
│ └── visualization/ \n
│ └── plots/ \n
│ └── grafico_ocorrencias.png \n
└── documentation/ \n
| └── reports/ \n
| | └── relatorio_anual.pdf \n

## Descrição dos Arquivos

### `code/base_main.py`

É o arquivo principal que chama as funções dos outros pacotes e realiza a análise completa.

### `code/relatorio_anual.py`

Contém funções para gerar o relatório anual em PDF com os resultados da análise.

**Função `gerar_relatorio_anual(df, modelo)`:**

Gera um relatório anual em PDF com os resultados da análise, incluindo informações gerais, gráficos da análise exploratória, informações sobre o modelo preditivo e informações sobre a clusterização (se disponível).

**Parâmetros:**

* `df (pd.DataFrame)`: DataFrame com os dados limpos e pré-processados.
* `modelo (sklearn.linear_model.LinearRegression)`: Modelo de regressão linear treinado.

**Passos:**

1. **Criar o PDF:**
   * Cria um objeto `FPDF` para gerar o PDF.
   * Adiciona uma página e define a fonte e o título do relatório.

2. **Adicionar Informações Gerais:**
   * Adiciona informações sobre o ano dos dados.

3. **Adicionar Gráficos da Análise Exploratória:**
   * Utiliza `PdfPages` para adicionar os gráficos gerados na `realizar_analise_exploratoria` ao PDF.

4. **Adicionar Informações sobre o Modelo Preditivo:**
   * Adiciona informações sobre o R² do modelo.

5. **Adicionar Informações sobre a Clusterização:**
   * Adiciona informações sobre os clusters (se disponíveis) e suas características.

6. **Salvar o PDF:**
   * Salva o PDF com o nome "reports/relatorio_anual.pdf".

### `code/cleaning/limpar_dados.py`

Contém funções para limpar e pré-processar os dados brutos.

**Função `limpar_dados(path)`:**

Esta função é responsável por carregar, limpar e pré-processar os dados brutos.

**Parâmetros:**

* `path (str)`: Caminho para a pasta com os arquivos brutos.

**Passos:**

1. **Carregar os Dados:**
   * Lê os arquivos Excel da pasta especificada no `path`.
   * Concatena os DataFrames em um único DataFrame (`df_total`).

2. **Limpar os Dados:**
   * Remove colunas irrelevantes (como as que contam o número de vítimas).
   * Renomeia colunas para facilitar a manipulação e leitura dos dados.
   * Substitui vírgulas por pontos para que os valores numéricos sejam lidos corretamente.
   * Converte as colunas para o tipo numérico usando `pd.to_numeric`.
   * Trata valores faltantes (NaN) substituindo-os por zero.
   * Cria uma coluna "Ano" para indicar o ano das ocorrências.

3. **Retorna o DataFrame:**
   * Retorna o DataFrame com os dados limpos e pré-processados.

### `code/analysis/analise_exploratoria.py`

Contém funções para análise exploratória e visualização dos dados.

**Função `realizar_analise_exploratoria`:**

Recebe o DataFrame com os dados limpos e pré-processados como argumento.

Realiza os seguintes tipos de análise:

* **Distribuição de Ocorrências:** Cria gráficos de barras para visualizar o total de ocorrências por mês, trimestre e categoria de crime.
* **Tendências:** Cria gráficos de linhas para observar a tendência de ocorrências por mês e por trimestre.
* **Correlação:** Cria uma matriz de correlação e utiliza um mapa de calor para visualizar a força da correlação entre as variáveis.
* **Ocorrências por Tipo de Crime:** Cria um gráfico de barras para visualizar o número de ocorrências por tipo de crime.

Exibe os gráficos utilizando `plt.show()`.

### `code/analysis/modelo_preditivo.py`

Contém funções para criar e avaliar modelos preditivos.

**Função `criar_modelo_preditivo(df)`:**

Cria e avalia um modelo de regressão linear para prever o número total de ocorrências em cada mês, com base nos dados históricos.

**Parâmetros:**

* `df (pd.DataFrame)`: DataFrame com os dados limpos e pré-processados.

**Passos:**

1. **Preparar os Dados:**
   * Separa as colunas que representam os meses (Janeiro a Dezembro) como variáveis explicativas (`X`).
   * Separa a coluna "Total_Ocorrencias" como variável resposta (`y`).

2. **Criar o Modelo:**
   * Cria um modelo de regressão linear usando `LinearRegression()`.

3. **Treinar o Modelo:**
   * Treina o modelo com os dados `X` e `y` utilizando `model.fit(X, y)`.

4. **Avaliar o Modelo:**
   * Calcula o R² do modelo (coeficiente de determinação) para avaliar o quão bem o modelo se ajusta aos dados.

5. **Retorna o Modelo:**
   * Retorna o modelo de regressão linear treinado.

## Instalação e Execução

1. **Instalação das Bibliotecas:**

   ```bash
   pip install -r requirements.txt

2. Execução da Análise:

   ```bash
   python code/base_main.py
