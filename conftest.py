import os
import shutil
import allure
import pytest

# Archivo para las configuraciones y fixtures globales de pytest

""" limpieza de screenshots antes de la sesión de tests"""


@pytest.fixture(scope="session", autouse=True)
def limpiar_screenshots():
    folder = "screenshots"
    if os.path.exists(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)


""" limpieza de resultados de Allure antes de la sesión de tests"""


@pytest.fixture(scope="session", autouse=True)
def limpiar_allure_results():
    folder = "allure-results"
    if os.path.exists(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)


""" captura de screenshots al fallar un test y adjuntar al reporte de Allure"""


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            # Guarda la captura en la carpeta screenshots con el nombre del test
            page.screenshot(path=f"screenshots/{item.name}_fallo.png")
            screenshot_path = f"screenshots/{item.name}_fallo.png"
            page.screenshot(path=screenshot_path)
            # Adjuntar la imagen al reporte de Allure
            if os.path.exists(screenshot_path):
                with open(screenshot_path, "rb") as image:
                    allure.attach(
                        image.read(),
                        name="screenshot",
                        attachment_type=allure.attachment_type.PNG,
                    )
