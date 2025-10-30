from playwright.sync_api import Page, expect
import json
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import pytest
from config import BASE_URL


""" Test total de login usando page object model con metodos principales,  datos de entorno y validaciones de API
    - test login exitoso
    - test login fallido con email inválido
    - test login fallido con password inválida"""

with open("data/login.json", "r", encoding="utf-8") as file:
    datos = json.load(file)
    usuario_valido = datos["login_valido"]["datos_validos"]["email"]
    password_valido = datos["login_valido"]["datos_validos"]["contraseña"]
    datos_email_invalido = datos["login_invalidos"]["email_invalido"]
    datos_pass_invalida = datos["login_invalidos"]["contraseña_invalida"]


@pytest.mark.login
@pytest.mark.smoke
def test_login_exitoso(page: Page):
    """Test de login exitoso usando login_page y dashboard_page y datos de entorno."""
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    login_page.login_usuario(BASE_URL, usuario_valido, password_valido)
    dashboard_page.verificar_elementos_dashboard()


@pytest.mark.login
@pytest.mark.negative
@pytest.mark.smoke
def test_login_email_invalido(page: Page):
    """Test de login fallido con email inválido usando datos del JSON."""
    login_page = LoginPage(page)
    login_page.navegar(BASE_URL)
    login_page.llenar_formulario(
        datos_email_invalido["email"], datos_email_invalido["contraseña"]
    )
    login_page.click_boton_ingresar()
    login_page.validar_mensaje_error(datos_email_invalido["mensaje_esperado"])
    expect(page).to_have_url(f"{BASE_URL}/login")


@pytest.mark.login
@pytest.mark.negative
@pytest.mark.smoke
def test_login_password_invalida(page: Page):
    """Test de login fallido con contraseña inválida usando datos del JSON."""
    login_page = LoginPage(page)
    login_page.navegar(BASE_URL)
    login_page.llenar_formulario(
        datos_pass_invalida["email"], datos_pass_invalida["contraseña"]
    )
    login_page.click_boton_ingresar()
    login_page.validar_mensaje_error(datos_pass_invalida["mensaje_esperado"])
    expect(page).to_have_url(f"{BASE_URL}/login")
