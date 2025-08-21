# 🧠 Pipeline de ETL com NLP para Análise de Vagas de Dados

![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![spaCy](https://img.shields.io/badge/NLP-spaCy-blueviolet)

## 🎯 Objetivo

Este projeto implementa um pipeline de dados **ETL (Extract, Transform, Load)** completo que utiliza técnicas de **Inteligência Artificial** para analisar o mercado de trabalho de Engenharia de Dados. O objetivo é converter dados textuais não estruturados, extraídos da web, em insights estruturados e acionáveis sobre as competências técnicas mais demandadas pelas empresas.

## ✨ Resultado Final

O pipeline processa milhares de palavras das descrições das vagas e, aplicando um modelo de NLP, gera uma visualização clara das tecnologias e habilidades mais requisitadas, oferecendo um panorama estratégico das tendências do setor.

![Gráfico de Top Skills](top_skills.png)

## 🏛️ Arquitetura do Pipeline

O projeto segue a clássica arquitetura ETL, onde a etapa de Transformação é enriquecida com um componente de Inteligência Artificial.

1.  **`Extração (Extract)`**

    - Um script de web scraping ético (`01_extracao.py`) navega pelo portal **Programathor** para coletar dados públicos de vagas (título, empresa, local e a descrição completa), utilizando pausas e headers para não sobrecarregar o servidor.
    - **Ferramentas:** `Requests`, `BeautifulSoup4`.

2.  **`Transformação (Transform)`**

    - Esta é a fase central do projeto. O script `02_transformacao.py` recebe os dados brutos e realiza a limpeza e padronização com Pandas.
    - Em seguida, aplicamos um modelo de **Processamento de Linguagem Natural (NLP)** com a biblioteca **`spaCy`** para realizar a **Extração de Entidades** a partir do texto não estruturado das descrições. Um `PhraseMatcher` otimizado é utilizado para identificar e extrair um dicionário customizado de _skills_, transformando texto livre em features quantificáveis para análise.
    - **Ferramentas:** `Pandas`, `spaCy` (NLP), `re` (Expressões Regulares).

3.  **`Carga (Load)`**

    - Os dados limpos e enriquecidos com as features de IA são carregados pelo script `03_carga.py` para um banco de dados relacional, garantindo o armazenamento persistente.
    - **Ferramentas:** `SQLite`.

4.  **`Análise e Visualização (Analyze & Visualize)`**
    - Um notebook (`analise.ipynb`) conecta-se ao banco de dados para realizar consultas e agregar os dados, contando a frequência de cada habilidade extraída pelo modelo de NLP.
    - O resultado da análise é exibido em um gráfico de barras, facilitando a interpretação dos insights.
    - **Ferramentas:** `Jupyter Lab`, `Matplotlib`, `Pandas`.

## 🛠️ Tecnologias e Habilidades

- **Engenharia de Dados:** Desenvolvimento de Pipelines ETL, Web Scraping, Limpeza e Estruturação de Dados.
- **Inteligência Artificial:** Processamento de Linguagem Natural (NLP) e Extração de Entidades com **`spaCy`**.
- **Linguagem:** Python.
- **Bibliotecas:** Pandas, Matplotlib, Requests, BeautifulSoup4, spaCy.
- **Banco de Dados:** SQLite.
- **Ferramentas:** Git, GitHub, Ambientes Virtuais (`venv`), Jupyter Lab.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar o pipeline em seu ambiente local.

**Pré-requisitos:**

- Python 3.9+
- Git

**Passos:**

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/joaosousa021/pipeline-analise-vagas.git](https://github.com/joaosousa021/pipeline-analise-vagas.git)
    cd pipeline-analise-vagas
    ```

2.  **Crie e ative o ambiente virtual:**

    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No Mac/Linux:
    source venv/bin/activate
    ```

3.  **Instale as dependências (incluindo o modelo spaCy):**

    ```bash
    pip install -r requirements.txt
    python -m spacy download pt_core_news_sm
    ```

4.  **Execute o pipeline ETL completo:**

    ```bash
    python 01_extracao.py
    python 02_transformacao.py
    python 03_carga.py
    ```

5.  **Visualize a análise:**
    - Inicie o Jupyter Lab:
      ```bash
      python -m jupyter lab
      ```
    - No seu navegador, abra o arquivo `analise.ipynb`.
    - Para executar cada passo da análise, selecione uma célula e pressione **`Shift + Enter`**. A última célula irá gerar o gráfico.
