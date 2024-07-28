import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from config import LOGGING_LEVEL, LOGGING_FORMAT, SERVER_HOSTNAME, HTTP_PATH, ACCESS_TOKEN, TABLE_NAME, SCHEMA, PARQUET_DIR
import logging
import os
import sys

# Configuração do logger
logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT)

def get_engine():
    """
    Cria uma engine de conexão usando SQLAlchemy para conectar ao Databricks.
    """
    connection_string = f"mssql+pyodbc://token:{ACCESS_TOKEN}@{SERVER_HOSTNAME}/{HTTP_PATH}?driver=ODBC+Driver+for+Databricks"
    return create_engine(connection_string)

def load_to_db(df, table_name, schema):
    """
    Carrega dados no Databricks de forma incremental.
    Assume que a chave primária é 'id' e que o schema e table_name são fornecidos.
    """
    engine = get_engine()
    with engine.connect() as conn:
        existing_data = pd.read_sql_table(table_name, conn, schema=schema)
        new_data = df[~df['id'].isin(existing_data['id'])]  # Correção no uso do operador de negação
        if not new_data.empty:
            new_data.to_sql(table_name, conn, schema=schema, if_exists='append', index=False)
            logging.info(f"Dados carregados na tabela {table_name}.")
        else:
            logging.info("Nenhum novo dado para carregar.")

def load_file(file_path: str):
    """
    Carrega um arquivo parquet do caminho especificado para o Databricks.
    """
    logging.info(f"Iniciando o carregamento do arquivo {file_path}")

    try:
        df = pd.read_parquet(file_path)
        load_to_db(df, TABLE_NAME, SCHEMA)
        logging.info(f"Arquivo {file_path} carregado com sucesso.")
    except Exception as e:
        logging.error(f"Erro durante o carregamento do arquivo {file_path}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != 'carrega':
        print(f"Uso: python load.py carrega {sys.argv[2]}")
        sys.exit(1)

    file_path = os.path.join(PARQUET_DIR, sys.argv[2])
    load_file(file_path)
