import pytest
from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv      
import time
import json
from pages.login_page import LoginPage


load_dotenv()
BASE_URL = os.getenv('BASE_URL')

''' Test mejorado de login exitoso usando page object model y validando la respuesta de la API'''
def test_login_exitoso(page: Page):
    """Login exitoso usando page object model"""
    
    login_page = LoginPage(page)
    login_page.navegar(BASE_URL)
    login_page.validar_url(BASE_URL)
    login_page.validar_header()
    login_page.validar_elementos()
    login_page.llenar_formulario("usuariouno@mail.com", "usuario1")
    response = login_page.capturar_respuesta_y_click(lambda response: "/students/login" in response.url)
    login_page.validar_respuesta_api(response, 200)
    login_page.verificar_redireccion_dashboard(BASE_URL)
    token = login_page.obtener_token_localstorage()
    assert token is not None
    login_page.verificar_header_logueado()


