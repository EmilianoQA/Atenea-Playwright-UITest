from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv
import time
import pytest
from pages.registro_page_new import RegistroPage
from pages.login_page import LoginPage
import json

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

with open('data/registro.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)
    datos_validos = datos['casos_exitosos']['datos_validos'][0]
    
def test_registro_exitoso(page: Page):
    """
    Test del flujo completo:
    1. Se registra un nuevo usuario.
    2. Se inicia sesión con las credenciales de ese nuevo usuario.
    3. Se valida la respuesta de la API
    """
    # Datos de prueba
    nombre = datos_validos['nombre']
    apellido = datos_validos['apellido']
    email_unico = datos_validos['email_base'] + f".test{int(time.time())}@mail.com"
    password = datos_validos['password']

    registro_page = RegistroPage(page)
    login_page = LoginPage(page)

    # Registro del nuevo usuario
    registro_page.registrar_nuevo_usuario(BASE_URL, nombre, apellido, email_unico, password)
    expect(page).to_have_url(f"{BASE_URL}/login")
    login_page.validar_elementos()

    # Inicio de sesión con las credenciales del nuevo usuario
    login_page.login_usuario(BASE_URL, email_unico, password)