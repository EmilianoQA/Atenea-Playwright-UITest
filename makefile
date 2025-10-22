# ==============================================================================
# Makefile con Doble Sistema de Reportes (Allure y Playwright Trace)
# ==============================================================================

# Directorios de resultados
ALLURE_DIR = allure-results
PLAYWRIGHT_DIR = test-results

# --- INSTALACIÓN ---
install:
	pip install -r requirements.txt
	playwright install

# --- EJECUCIÓN DE TESTS ---
# Todos los tests ahora generan resultados para AMBOS sistemas de reporte.
# '--output' es para Playwright, '--alluredir' es para Allure.

test:
	pytest --output=$(PLAYWRIGHT_DIR) --alluredir=$(ALLURE_DIR) --clean-alluredir

test-headed:
	pytest --headed --output=$(PLAYWRIGHT_DIR) --alluredir=$(ALLURE_DIR) --clean-alluredir

smoke:
	pytest -m smoke --output=$(PLAYWRIGHT_DIR) --alluredir=$(ALLURE_DIR) --clean-alluredir

# --- VISUALIZACIÓN DE REPORTES ---
# Comandos separados para ver cada tipo de reporte.

# Comando: make report-allure
# Lee los resultados de 'allure-results' y abre el reporte de Allure.
report-allure:
	allure serve $(ALLURE_DIR)

# Comando: make report-trace
# Lee los resultados de 'test-results' y abre el último Trace de Playwright.
report-trace:
	ls -t $(PLAYWRIGHT_DIR)/*/trace.zip | head -n 1 | xargs playwright show-trace

# ... (El resto de tus comandos: format, lint, help, etc.)
