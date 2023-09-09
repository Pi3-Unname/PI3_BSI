# Heal Analytics

<h4 align="center">
	🚧   Concluído 🚀 🚧
</h4>

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre o projeto](#-sobre-o-projeto)
   * [Funcionalidades](#-funcionalidades)
   * [Layout](#-layout)
   * [Como executar o projeto](#-como-executar-o-projeto)
     * [Pré-requisitos](#pré-requisitos)
     * [Rodando a aplicação web (Streamlit)](#user-content--rodando-a-aplicação-web-frontend)
   * [Tecnologias](#-tecnologias)
   * [Autor(es)](#-autor(es))
   * [Licença](#user-content--licença)
<!--te-->


## 💻 Sobre o projeto

Esse projeto é voltado para área de saude e foi desenvolvido com objetivo de oferecer, por meio de análises estatísticas e uso de Marchine Learning, recursos necessários para prever os custos, tempo de estadia e procedimentos realizados pelo paciente.Estas análises serão úteis para obter insights e ajudar na tomada de decisão pelo gestor de um determinado hospital ou qualquer pessoa vinculada a saúde que lidam constantemente com essas informações.

## 🎨 Layout

## ⚙️ Funcionalidades

- [x] transformat database
- [x] Cabeçalho
- [x] Gráfico BoxPlot
- [x] Gráfico de Dispersão
- [x] Gráfico Treemap
- [x] Análise de Admissão
- [x] Análise de Diagnóstico
- [x] Análise de Estadia
- [x] Análise Financeira
- [x] Análise Exploratória
- [x] Machine Learning
- [x] Comparate Machine Learning



## 🚀 Como executar o projeto

Este projeto foi desenvolvido e executado no servidor Streamlit:  [Web App(streamlit)](https://streamlit.io)



### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Python](https://www.python.org/downloads/) e um editor de código [VSCode](https://code.visualstudio.com/).
Baixe o dataset que será usado no projeto: [DataSet The New York Hospital](https://www.kaggle.com/datasets/thedevastator/2010-new-york-state-hospital-inpatient-discharge), salve na pasta do projeto PI3_BSI/venv/project/data e renomeie o arquivo para hospital.



#### 🧭 Rodando a aplicação web (Frontend)

```bash

# Clone este repositório
$ git clone https://github.com/Pi3-Unname/PI3_BSI.git

# Acesse a pasta do projeto no seu terminal/cmd
$ cd PI3_BSI

# Recomendamos criar um abiente virtual com mesmo nome da pasta do projeto.
$ python -m venv venv

# Vá para a pasta venv
$ cd venv

# Instale as dependências
$ pip install -r requirements.txt

# Converta o dataset em .parquet
$ cd venv/project/utils/format_database.py

# Execute o transform_pkl.py
$ cd venv/transform_pkl.py

# Executa a aplicação streamlit
$ streamlit run venv/project/Home.py

# A aplicação será aberta na porta:Local URL: http://localhost:8501
  Network URL: http://192.168.0.103:8501


```
---
## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

#### **WebApp**  ([Streamlit](https://streamlit.io)  +  [Python](https://www.python.org))

-   **[Pandas](https://pandas.pydata.org)**
-   **[Numpy](https://numpy.org)**
-   **[Scikit-Learn](https://scikit-learn.org/stable/)**
-   **[MatplotLib](https://matplotlib.org)**
-   **[Plotly](https://plotly.com)**

---

### Autor(es)

* Jose Carlos
* Silas Ribeiro
* Paloma Moraes
* Michael Douglas

---

## 📝 Licença

Este projeto esta sobe a licença [MIT](./LICENSE).

Feito por  Jose Carlos | Silas Ribeiro | Paloma Moraes | Michael Douglas

---



