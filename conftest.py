import pytest


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            # Guarda la captura en la carpeta screenshots con el nombre del test
            page.screenshot(path=f"screenshots/{item.name}_fallo.png")
