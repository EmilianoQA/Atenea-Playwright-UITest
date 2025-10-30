# Configuración centralizada de variables de entorno
import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

"""
Ejemplo de otra variable de entorno

API_KEY = os.getenv("API_KEY")
TIMEOUT = int(os.getenv("TIMEOUT", 30))
DATA_PATH = os.getenv("DATA_PATH", "data/")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
"""
