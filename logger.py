import logging
import os

LOG_FILE = "portfolio.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s — %(message)s",
    encoding="utf-8"
)

def log(message: str):
    """Записывает действие в лог-файл."""
    logging.info(message)
