# Archivo: tests/test_registro_validAPI.py

import pytest
from playwright.sync_api import Page
import os
from dotenv import load_dotenv
import time
import json
import random # <--- Importante
from pages.registro_page import RegistroPage
from utils.helpers import validar_respuesta_api_simple 

# Configuración inicial
load_dotenv()
BASE_URL = os.getenv('BASE_URL')

with open('data/usuarios.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)

usuario_valido = datos['usuarios_validos'][0]

# Test de registro con validación mejorada de API
def test_registro_exitoso(page: Page):
    """
    Test de registro que utiliza una función helper para validar la API
    y comprueba el resultado final en la UI.
    """
    
    # Email único
    timestamp = int(time.time())
    random_num = random.randint(1000, 9999)
    email_unico = f"{usuario_valido['email_base']}.test{timestamp}{random_num}@mail.com"
    registro_page = RegistroPage(page)
    registro_page.navegar(BASE_URL)
    registro_page.llenar_formulario(
        usuario_valido['nombre'],
        usuario_valido['apellido'],
        email_unico,
        usuario_valido['password']
    )
    registro_page.aceptar_terminos()
    # Acción y captura de respuesta
    with page.expect_response("**/students/register") as response_info:
        registro_page.hacer_click_crear_cuenta()
    # Validación de la respuesta API usando helper
    validar_respuesta_api_simple(
        response=response_info.value,
        expected_method="POST",
        expected_status=201,
        expected_key="token"
    )
    # Validaciones en la UI
    registro_page.verificar_redireccion_dashboard(BASE_URL)
    token_en_navegador = registro_page.obtener_token_localstorage()
    assert token_en_navegador is not None, "No se encontró ningún token en el Local Storage"
    registro_page.verificar_header_logueado()