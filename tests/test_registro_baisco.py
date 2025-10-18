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

def test_registro_exitoso_simple(page: Page):
    """Test simple de registro exitoso
    - Navega a la página de registro
    - Completa el formulario de registro
    - Acepta los términos y condiciones
    - Hace clic en Crear cuenta
    - Verifica que el modal de registro exitoso se muestra correctamente
    - Hace clic en Ir a iniciar sesión
    - Verifica que redirige a la página de login"""

    registro_page = RegistroPage(page)
    registro_page.navegar(BASE_URL)
    
    # Generar email único
    email_unico = f"usuario.test{int(time.time())}@mail.com"
    
    # Llenar el formulario
    registro_page.llenar_formulario("Ana", "Pérez", email_unico, "Atenea123")
    
    # Aceptar términos
    registro_page.aceptar_terminos()
    
    # Hacer clic en Crear cuenta
    registro_page.hacer_click_crear_cuenta()
    
    # Verificar modal de registro exitoso
    registro_page.verificar_modal_registro_exitoso()
    
    # Hacer clic en Ir a iniciar sesión
    registro_page.boton_ir_a_login.click()
    
    # Verificar redirección a login
    login_page = LoginPage(page)
    login_page.navegar(BASE_URL)
    login_page.validar_elementos()
    expect(page).to_have_url(f"{BASE_URL}/login")
    
    print(f"✅ Test exitoso - Email: {email_unico}")