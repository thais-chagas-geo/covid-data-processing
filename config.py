import logging
import os

# Constantes de arquivo
file = {
    'file': 'aggregated.csv',
    'url': 'https://storage.googleapis.com/covid19-open-data/v3/latest/aggregated.csv'
}

# Diretórios locais
APP_DIR = '/home/thaischagas/ntconsult'
RAW_DIR = os.path.join(APP_DIR, 'raw')
STAGE_DIR = os.path.join(APP_DIR, 'stage')

# Configuração do destino
# Esses valores devem ser válidos e acessíveis para conectar ao Databricks se necessário.
SERVER_HOSTNAME = 'databricks-hostname'
HTTP_PATH = 'databricks-http-path'
ACCESS_TOKEN = 'databricks-access-token'

# Configuração de logging
LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# Configurações adicionais para testes locais
DB_CONNECTION_STRING = 'sqlite:///test.db'  # Exemplo usando SQLite localmente
TABLE_NAME = 'data_table'  # Nome da tabela para operações de carregamento
SCHEMA = 'public'  # Esquema de banco de dados, se necessário
PARQUET_DIR = os.path.join(APP_DIR, 'parquet')  # Diretório para arquivos Parquet


