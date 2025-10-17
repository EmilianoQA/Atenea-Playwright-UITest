import pytest
from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv
import time
from pages.registro_page import RegistroPage

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

'''Test mejorado de registro exitoso usando page object model y validando la respuesta de la API'''

def test_registro_exitoso(page: Page):  
    """Test simple de registro exitoso"""
    
    # Ir a la página de registro
    registro_page = RegistroPage(page)
    registro_page.navegar(BASE_URL)
    
    # Generar email único
    email_unico = f"usuario.test{int(time.time())}@mail.com"
    
    # Llenar el formulario
    registro_page.llenar_formulario("Ana", "Pérez", email_unico, "Atenea123")
    
    # Aceptar términos
    registro_page.aceptar_terminos()
    
    # Hacer clic y capturar respuesta
    with page.expect_response(lambda response: "/students/register" in response.url) as response_info:
        registro_page.hacer_click_crear_cuenta()
        
    # Validar respuesta API
    response = response_info.value
    assert response.status == 201
    
    # Validar redirección al dashboard
    registro_page.verificar_redireccion_dashboard(BASE_URL)
    
    # Validar token (ya está en el dashboard)
    token = registro_page.obtener_token_localstorage()
    assert token is not None
    
    # Validar header logueado
    registro_page.verificar_header_logueado()
    
    print(f"✅ Test exitoso - Email: {email_unico}")