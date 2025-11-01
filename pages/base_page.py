from playwright.sync_api import Page, expect
import time


class BasePage:
    """
    La clase 'padre' que contiene funciones comunes y reutilizables.
    """

    def __init__(self, page: Page):
        """El constructor que recibe el objeto 'page' de Playwright."""
        self.page = page

    # Funciones

    def validar_url(self, url_esperada: str):
        """Valida que la URL actual de la página coincide con la esperada."""
        expect(self.page).to_have_url(url_esperada)

    def obtener_token_localstorage(self) -> str:
        """Obtiene el token de autenticación guardado en el Local Storage del navegador."""
        return self.page.evaluate("() => localStorage.getItem('token')")

    def tomar_captura_pantalla(self, nombre_archivo: str):
        """
        Toma una captura de pantalla de la página actual.
        El nombre del archivo incluirá un timestamp para hacerlo único.
        """
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        self.page.screenshot(path=f"screenshots/{nombre_archivo}_{timestamp}.png")
