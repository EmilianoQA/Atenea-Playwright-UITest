import pytest
from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv      
import json
from pages.login_page import LoginPage

# Carga de variables de entorno 
load_dotenv()
BASE_URL = os.getenv('BASE_URL')

'''Test optimizado para login usando page object y datos de entorno
    - test login exitoso
    - test login fallido con email inválido
    - test login fallido con password inválida'''

# Carga de datos desde el archivo JSON
with open('data/login.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)
    datos_validos = datos['login_valido']['datos_validos']
    datos_email_invalido = datos['login_invalidos']['email_invalido']
    datos_pass_invalida = datos['login_invalidos']['contraseña_invalida']
        
def test_login_exitoso(page: Page):
    """Test de login exitoso."""
    login_page = LoginPage(page)
    login_page.navegar(BASE_URL)
    login_page.validar_url(BASE_URL)
    login_page.validar_header()
    login_page.validar_elementos()
    login_page.llenar_formulario(datos_validos['email'], datos_validos['contraseña'])
    response = login_page.capturar_respuesta_y_click(lambda r: "/students/login" in r.url)
    login_page.validar_respuesta_api(response, 200)
    login_page.verificar_redireccion_dashboard(BASE_URL)
    token = login_page.obtener_token_localstorage()
    assert token is not None
    login_page.verificar_header_logueado()

def test_login_email_invalido(page: Page):
    """Test de login fallido con email inválido."""
    login_page = LoginPage(page)
    login_page.navegar(BASE_URL)
    login_page.llenar_formulario(datos_email_invalido['email'], datos_email_invalido['contraseña'])
    login_page.click_boton_ingresar()
    login_page.validar_mensaje_error(datos_email_invalido['mensaje_esperado'])
    expect(page).to_have_url(f"{BASE_URL}/login")

def test_login_password_invalida(page: Page):
    """Test de login fallido con contraseña inválida."""

    login_page = LoginPage(page)
    login_page.navegar(BASE_URL)
    login_page.validar_url(BASE_URL)
    login_page.validar_header()
    login_page.validar_elementos()
    login_page.llenar_formulario(datos_pass_invalida['email'], datos_pass_invalida['contraseña'])
    response = login_page.capturar_respuesta_y_click(lambda r: "/students/login" in r.url)
    login_page.validar_respuesta_api(response, 401)
    login_page.validar_mensaje_error(datos_pass_invalida['mensaje_esperado'])
    expect(page).to_have_url(f"{BASE_URL}/login")