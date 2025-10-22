# ==============================================================================
# Makefile Final para el Framework de Automatización Atenea
# ==============================================================================

# --- INSTALACIÓN ---
install:
	pip install -r requirements.txt
	playwright install

# --- EJECUCIÓN DE TESTS ---
# Gracias a 'pytest.ini', todos estos comandos generan los archivos de traza (.zip) en la carpeta 'traces/'.

test:
	pytest

test-headed:
	pytest --headed

smoke:
	pytest -m smoke

# --- VISUALIZACIÓN DE REPORTES ---
trace:
	@last_trace=$$(find test-results -name "trace.zip" | sort | tail -1); \
	if [ -n "$$last_trace" ]; then \
		echo "🔍 Abriendo trace: $$last_trace"; \
		playwright show-trace $$last_trace; \
	else \
		echo "❌ No se encontró ningún trace.zip en test-results/"; \
	fi

# --- CALIDAD DE CÓDIGO ---
format:
	black .

lint:
	ruff check . --fix

# --- AYUDA ---
help:
	@echo "--- Comandos Disponibles ---"
	@echo "make install       -> Instala dependencias y navegadores."
	@echo "make test          -> Ejecuta todos los tests (y genera trazas)."
	@echo "make test-headed   -> Ejecuta todos los tests con UI (y genera trazas)."
	@echo "make smoke         -> Ejecuta solo los smoke tests (y genera trazas)."
	@echo "make report        -> MUESTRA el último reporte de traza de Playwright."
	@echo "make format        -> Formatea el código con Black."
	@echo "make lint          -> Limpia el código con Ruff."

.PHONY: install test test-headed smoke report format lint help
