import os
import logging
import requests
from config import LOGGING_LEVEL, LOGGING_FORMAT, file, RAW_DIR

# Configuração do logger
logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT)

def download_file(url, destination):
    """
    Baixa o arquivo da URL fornecida para o destino especificado.
    :param url: URL do arquivo para baixar.
    :param destination: Caminho local onde o arquivo será salvo.
    """
    response = requests.get(url, stream=True)  # Use stream=True para download eficiente de arquivos grandes.
    if response.status_code == 200:
        with open(destination, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):  # Baixa o arquivo em partes.
                f.write(chunk)
        logging.info(f"[OK] Arquivo baixado para: {destination}")
    else:
        logging.error(f"[Erro] Falha ao baixar o arquivo: {url}")
        raise Exception(f"Erro {response.status_code} ao baixar o arquivo.")

def main():
    """
    Ponto de entrada principal do script de extração.
    """
    url = file['url']
    filename = os.path.basename(url)
    destination = os.path.join(RAW_DIR, filename)
    download_file(url, destination)

if __name__ == "__main__":
    main()
