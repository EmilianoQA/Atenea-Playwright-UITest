from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv
import pytest

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

""" Test simple de login exitoso con datos hardcodeados """


@pytest.mark.login
def test_login_exitoso(page: Page):
    """Test simple de login exitoso"""

    # Ir a la página de login
    page.goto(f"{BASE_URL}/login")

    # Validar que está en la página de login
    expect(page).to_have_url(f"{BASE_URL}/login")

    # Validar el header
    expect(page.get_by_role("heading", name="Acceso de Estudiantes")).to_be_visible()

    # Validar que los elementos del formulario están visibles
    expect(page.get_by_role("textbox", name="Correo Electrónico")).to_be_visible()
    expect(page.get_by_role("textbox", name="Contraseña")).to_be_visible()
    expect(page.get_by_role("button", name="Ingresar")).to_be_visible()

    # Llenar el formulario
    page.get_by_role("textbox", name="Correo Electrónico").fill("usuariouno@mail.com")
    page.get_by_role("textbox", name="Contraseña").fill("usuario1")
    # page.get_by_role("button", name="Ingresar").click()

    # hacer clic y capturar respuesta
    with page.expect_response(
        lambda response: "/students/login" in response.url
    ) as response_info:
        page.get_by_role("button", name="Ingresar").click()

    # Validar que la API respondió 200
    response = response_info.value
    assert response.status == 200

    # ESPERAR A QUE LLEGUE AL DASHBOARD
    expect(page).to_have_url(f"{BASE_URL}/dashboard")

    # Validar header logueado
    expect(page.get_by_role("button", name="account of current user")).to_be_visible()
    expect(page.get_by_text("Hola,")).to_be_visible()
