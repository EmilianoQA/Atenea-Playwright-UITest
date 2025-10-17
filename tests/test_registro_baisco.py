import pytest
from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv
import time

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

'''Test basico de registro exitoso con datos hardcodeados, sin page object y con validacion de la respuesta de la API'''

def test_registro_exitoso(page: Page):
    """Test simple de registro exitoso"""
    
    # Ir a la página de registro
    page.goto(f"{BASE_URL}/signup")
    
    # Generar email único
    email_unico = f"usuario.test{int(time.time())}@mail.com"
    
    # Llenar el formulario
    page.get_by_role("textbox", name="Nombre").fill("Ana")
    page.get_by_role("textbox", name="Apellido").fill("Pérez")
    page.get_by_role("textbox", name="Correo electrónico").fill(email_unico)
    page.get_by_role("textbox", name="Contraseña", exact=True).fill("Atenea123")
    page.get_by_role("textbox", name="Confirmar contraseña").fill("Atenea123")
    
    # Aceptar términos
    page.get_by_role("checkbox", name="Acepto los Términos y").check()
    
    # Hacer clic y capturar respuesta
    with page.expect_response(lambda response: "/students/register" in response.url) as response_info:
        page.get_by_role("button", name="Crear cuenta").click()
    
    # Validar que la API respondió 201
    response = response_info.value
    assert response.status == 201

    # ESPERAR A QUE LLEGUE AL DASHBOARD
    expect(page).to_have_url(f"{BASE_URL}/dashboard")

    # Verificar que el token está en localStorage∏
    token = page.evaluate("() => localStorage.getItem('token')")
    assert token is not None
        
    # Validar redirección
    expect(page).to_have_url(f"{BASE_URL}/dashboard")
    # Validar header logueado
    expect(page.get_by_role("button", name="account of current user")).to_be_visible()
    expect(page.get_by_text("Hola,")).to_be_visible()
    
    print(f"✅ Test exitoso - Email: {email_unico}")