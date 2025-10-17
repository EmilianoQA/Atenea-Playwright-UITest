import pytest
from playwright.sync_api import Page
import os
from dotenv import load_dotenv
import time
from pages.registro_page import RegistroPage
import json

"""
Test que registra un usuario llamando al método principal de la Page Object
y usando datos del JSON.
"""
load_dotenv()
BASE_URL = os.getenv('BASE_URL')

with open('data/usuarios.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)
usuario_valido = datos['usuarios_validos'][0]
email_unico = f"{usuario_valido['email_base']}.test{int(time.time())}@mail.com"

def test_registro_simple(page: Page):
   
    registro_page = RegistroPage(page)
    registro_page.registrar_nuevo_usuario(
        base_url=BASE_URL,
        nombre=usuario_valido['nombre'],
        apellido=usuario_valido['apellido'],
        email=email_unico,
        password=usuario_valido['password']
    )

    token = registro_page.obtener_token_localstorage()
    assert token is not None
    registro_page.verificar_header_logueado()