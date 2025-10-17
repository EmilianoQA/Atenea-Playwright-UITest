import pytest
from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv
import time
import json
from pages.registro_page import RegistroPage

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

'''
Test parametrizado de registro usando page object model y datos desde JSON
   - casos de registro exitoso
   - casos de registro fallido (email inválido, password inválida, email duplicado
'''

with open('data/usuarios.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)

casos = [
    {
        "nombre": "Ana",
        "apellido": "Pérez",
        "email_base": "ana.perez",
        "password": "Atenea123",
        "debe_pasar": True,
        "desc": "Registro exitoso"
    },
    {
        "nombre": "Test",
        "apellido": "Invalid",
        "email_base": "test.password",
        "password": "123",
        "debe_pasar": False,
        "desc": "Password inválida"
    },
    {
        "nombre": "Test",
        "apellido": "Invalid",
        "email_base": "email@invalido",
        "password": "Test123456",
        "debe_pasar": False,
        "desc": "Email inválido"
    },
    {
        "nombre": "Dup",
        "apellido": "Email",
        "email_base": "ana.perez",
        "password": "Test123456",
        "debe_pasar": False,
        "desc": "Email duplicado"
    }
]


@pytest.mark.parametrize("caso", casos, ids=[c["desc"] for c in casos])
def test_registro(page: Page, caso):
    """Test parametrizado: valida si el registro pasa o falla según los datos"""
    
    # Email único para casos válidos
    if caso['desc'] == "Email duplicado":
        email = "ana.perez.test1234567890@mail.com"
    else:
        email = f"{caso['email_base']}.test{int(time.time())}@mail.com"
    
    # Configuración del test
    registro_page = RegistroPage(page)
    registro_page.navegar(BASE_URL)
    registro_page.llenar_formulario(caso['nombre'], caso['apellido'], email, caso['password'])
    registro_page.aceptar_terminos()
    
    # Accines y validaciones
    if caso['debe_pasar']:
        with page.expect_response(lambda r: "/students/register" in r.url):
            registro_page.hacer_click_crear_cuenta()
        registro_page.verificar_redireccion_dashboard(BASE_URL)
    else:
        registro_page.hacer_click_crear_cuenta()
        error = registro_page.obtener_mensaje_error()
        assert error, f"Se esperaba error pero no hay mensaje"
    
    print(f"✅ {caso['desc']}")