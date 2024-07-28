import pandas as pd
import os
import datetime as dt
import logging
import sys
from config import LOGGING_LEVEL, LOGGING_FORMAT, STAGE_DIR  # Ajuste aqui

# Configuração do logger
logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT)

def clean_mixed_types(value):
    """
    Limpa e converte tipos de dados mistos para um formato mais consistente.
    """
    try:
        return pd.to_numeric(value, errors='coerce')
    except:
        return value

def process_data(df):
    """
    Função para processar os dados do DataFrame.
    """
    # Converter datas para tipo datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Limpar e converter colunas com tipos mistos
    mixed_type_cols = [col for col in df.columns if df[col].dtype == 'object']
    for col in mixed_type_cols:
        df[col] = df[col].apply(clean_mixed_types)

    # Preencher valores NaN
    df.fillna(method='ffill', inplace=True)

    return df

def save_to_parquet(df, out):
    """
    Função para salvar em formato parquet.
    """
    # Salva o arquivo parquet diretamente no STAGE_DIR
    df.to_parquet(os.path.join(STAGE_DIR, out + ".parquet"))

def transform_file(input_file: str):
    """
    Função para transformar arquivo CSV e salvar como Parquet.
    """
    logging.info(f"{dt.datetime.now()} TRANSFORMA: Iniciando transformação de {input_file}")

    try:
        df = pd.read_csv(input_file, low_memory=False)
        df = process_data(df)
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        save_to_parquet(df, f"transformed_{base_name}")
        logging.info(f"{dt.datetime.now()} TRANSFORMA: Transformação concluída e arquivo salvo como transformed_{base_name}.parquet")
    except Exception as e:
        logging.error(f"Erro durante a transformação do arquivo {input_file}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != 'transforma':
        print("Uso: python transform.py transforma {input_file}")
        sys.exit(1)

    input_file = os.path.join(STAGE_DIR, sys.argv[2])
    transform_file(input_file)
