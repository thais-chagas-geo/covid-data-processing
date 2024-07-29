# COVID-19 Data Processing Pipeline

Este projeto consiste em um pipeline de processamento de dados projetado para baixar, transformar e carregar dados da COVID-19 obtidos de um repositório público. O objetivo é facilitar a análise desses dados em plataformas como o Databricks.

## Estrutura do Projeto

- `extrai.py`: Script para baixar arquivos CSV diretamente de uma URL especificada.
- `transform.py`: Script para transformar dados em formato CSV para Parquet, realizando limpezas e transformações necessárias.
- `load.py`: Script para carregar dados em formato Parquet para uma tabela no Databricks usando SQLAlchemy.
- `config.py`: Configurações globais do projeto, incluindo caminhos de diretórios e credenciais de banco de dados.
- `cli.py`: Interface de linha de comando para executar as operações de extração, transformação e carga.

## Pré-requisitos

Antes de iniciar, certifique-se de que você tem Python instalado em seu sistema. Este projeto foi desenvolvido usando Python 3.8.

## Instalação

Clone o repositório para sua máquina local usando:

```
git clone https://github.com/seu-usuario/covid-data-processing.git
```
##Instale as dependências necessárias com o seguinte comando:
```
pip install -r requirements.txt
```
##Uso

Para executar o pipeline completo, utilize os seguintes comandos:
```
python cli.py extrai
python cli.py transforma aggregated.csv
python cli.py carrega transformed_aggregated.parquet
```
Você também pode executar cada script individualmente conforme descrito na seção de estrutura do projeto.

##Databricks
Para além de executar o processo ETL localmente através de uma CLI, também implementei o processo ETL diretamente no Databricks. Este está disponível neste notebook:

[ETL Notebook on Databricks](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3096057179230130/2322585530028599/2483491886094004/latest.html)

Adicionalmente, criei um outro notebook para realizar algumas análises:

[Data Analysis Notebook on Databricks](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3096057179230130/2322585530028609/2483491886094004/latest.html)

Todas as respostas aos requisitos estão no arquivo requisitos.txt deste projeto.

##Contribuição
Contribuições são sempre bem-vindas! Por favor, leia o arquivo CONTRIBUTING.md para mais detalhes sobre como enviar pull requests.
