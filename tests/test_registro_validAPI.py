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

# --- CONFIGURACIÓN Y DATOS ---
load_dotenv()
BASE_URL = os.getenv('BASE_URL')

with open('data/usuarios.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)

usuario_valido = datos['usuarios_validos'][0]

# --- EL ÚNICO TEST QUE NECESITAS ---
def test_registro_exitoso(page: Page):
    """
    Test de registro que utiliza una función helper para validar la API
    y comprueba el resultado final en la UI.
    """
    
    # --- LA CLAVE DE LA SOLUCIÓN ---
    # El email único se crea DENTRO del test. Cada ejecución tendrá uno nuevo.
    timestamp = int(time.time())
    random_num = random.randint(1000, 9999)
    email_unico = f"{usuario_valido['email_base']}.test{timestamp}{random_num}@mail.com"
    
    registro_page = RegistroPage(page)

    # PASO 1: ACCIONES EN LA UI
    registro_page.navegar(BASE_URL)
    registro_page.llenar_formulario(
        usuario_valido['nombre'],
        usuario_valido['apellido'],
        email_unico,
        usuario_valido['password']
    )
    registro_page.aceptar_terminos()

    # PASO 2: CAPTURAR LA RESPUESTA DE LA API
    with page.expect_response("**/students/register") as response_info:
        registro_page.hacer_click_crear_cuenta()
    
    # PASO 3: VALIDAR LA API CON LA FUNCIÓN HELPER
    validar_respuesta_api_simple(
        response=response_info.value,
        expected_method="POST",
        expected_status=201,
        expected_key="token"
    )

    # PASO 4: VALIDAR LA UI FINAL
    registro_page.verificar_redireccion_dashboard(BASE_URL)
    
    token_en_navegador = registro_page.obtener_token_localstorage()
    assert token_en_navegador is not None, "No se encontró ningún token en el Local Storage"
    
    registro_page.verificar_header_logueado()