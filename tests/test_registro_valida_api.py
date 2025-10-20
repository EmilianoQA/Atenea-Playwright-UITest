# Archivo: tests/test_registro_validAPI.py

from playwright.sync_api import Page
import os
from dotenv import load_dotenv
import time
import json
import random
from pages.registro_page import RegistroPage
from pages.login_page import LoginPage
from utils.helpers import validar_respuesta_api_simple

# Configuración inicial
load_dotenv()
BASE_URL = os.getenv("BASE_URL")

with open("data/registro.json", "r", encoding="utf-8") as file:
    datos = json.load(file)

usuario_valido = datos["casos_exitosos"][0]


# Test de registro con validación mejorada de API
def test_registro_exitoso_valida_api(page: Page):
    """
    Test de registro que utiliza una función helper para validar la API
    y comprueba el resultado final en la UI.
    """
    registro_page = RegistroPage(page)
    login_page = LoginPage(page)

    # Email único
    timestamp = int(time.time())
    random_num = random.randint(1000, 9999)
    email_unico = f"{usuario_valido['email_base']}.test{timestamp}{random_num}@mail.com"
    password = usuario_valido["password"]

    # Registro
    registro_page.navegar(BASE_URL)
    registro_page.llenar_formulario(
        usuario_valido["nombre"],
        usuario_valido["apellido"],
        email_unico,
        password,
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
        expected_key="token",
    )

    # Verificamos los nuevos pasos de la UI post-registro
    registro_page.verificar_modal_registro_exitoso()
    registro_page.click_ir_a_login()
    login_page.login_usuario(BASE_URL, email_unico, password)
