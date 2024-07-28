import sys
import argparse
import logging
from config import LOGGING_LEVEL, LOGGING_FORMAT
from extractions.extrai import main as extrai_main
from extractions.transform import transform_file
from extractions.load import load_file

# Configuração básica de logger
logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT)
logger = logging.getLogger(__name__)

# Constantes para os comandos
EXTRACT_CMD = "extrai"
TRANSFORM_CMD = "transforma"
LOAD_CMD = "carrega"

def setup_arg_parser():
    """
    Configura o parser de argumentos da linha de comando.
    """
    parser = argparse.ArgumentParser(description="Script de ETL para processamento de dados.")
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponíveis')

    # Parser para comando de extração
    extract_parser = subparsers.add_parser(EXTRACT_CMD, help="Extrai dados de uma URL especifica.")
    
    # Parser para comando de transformação
    transform_parser = subparsers.add_parser(TRANSFORM_CMD, help="Transforma dados em formato Parquet.")
    transform_parser.add_argument('file', type=str, help="Nome do arquivo para transformação.")
    
     # Parser para comando de carregamento
    load_parser = subparsers.add_parser(LOAD_CMD, help="Carrega dados para o Databricks.")
    load_parser.add_argument('file', type=str, help="Nome do arquivo Parquet para carga no Databricks")

    return parser

def main():
    parser = setup_arg_parser()
    args = parser.parse_args()

    if not hasattr(args, 'command') or args.command is None:
        logger.error("Nenhum comando fornecido.")
        parser.print_help()
        sys.exit(1)

    if args.command == EXTRACT_CMD:
        logger.info("Executando extração")
        extrai_main()  # Não precisa passar nenhum argumento
    elif args.command == TRANSFORM_CMD:
        logger.info(f"Executando transformação para o arquivo: {args.file}")
        transform_file(args.file)
    elif args.command == LOAD_CMD:
        logger.info(f"Executando carregamento para o arquivo: {args.file}")
        load_file(args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

