# COVID-19 Data Processing Pipeline

Este projeto consiste em um pipeline de processamento de dados para baixar, transformar e carregar dados da COVID-19 obtidos de um repositório público. O objetivo é facilitar a análise desses dados em plataformas como o Databricks.

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
bash
git clone https://github.com/tthaischagas/covid-data-processing.git
```

Instale as dependências necessárias: 
```
bash
pip install -r requirements.txt
```

##Uso
Para executar o pipeline completo, use os seguintes comandos: 
```
bash
python cli.py extrai
python cli.py transforma aggregated.csv
python cli.py carrega transformed_aggregated.parquet

```
Você pode também executar cada script individualmente conforme descrito na seção de estrutura do projeto.

##Contribuição
Contribuições são sempre bem-vindas! Por favor, leia o arquivo CONTRIBUTING.md para mais detalhes sobre como enviar pull requests.




