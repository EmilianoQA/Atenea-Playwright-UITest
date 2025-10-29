
# Atenea-Playwright-UITest

Framework profesional de automatización End-to-End para la web "Atenea Conocimientos", desarrollado con Python, Playwright y Pytest. Ideal para mostrar buenas prácticas, patrones y herramientas modernas de QA Automation.

---

## 🚀 Fortalezas

- **Page Object Model (POM):** Código limpio y escalable, separación entre lógica de test y UI.
- **Tests Data-Driven:** Escenarios parametrizados y datos externos (JSON).
- **Validación UI + API:** Pruebas híbridas para mayor cobertura y detección de errores.
- **Reportes Allure:** Resultados visuales, históricos y adjuntos automáticos (screenshots/videos).
- **Calidad de Código:** Integración con Black, Ruff y pre-commit hooks.

---

## 🗂️ Estructura del Proyecto

```
├── assets/           # Recursos estáticos (CSS, imágenes)
├── data/             # Datos de prueba (JSON, CSV)
├── fixtures/         # Fixtures de Pytest
├── pages/            # Objetos de página (POM)
├── tests/            # Casos de prueba
├── utils/            # Utilidades y helpers
├── report.html       # Reporte generado por Allure
├── requirements.txt  # Dependencias
└── README.md         # Este archivo
```

---

## 🛠️ Stack Tecnológico

- Python
- Playwright
- Pytest
- Allure Framework
- Black, Ruff, pre-commit

---

## 🏃‍♂️ Uso Diario y Comandos Clave

1. Instala dependencias (si es necesario):
   ```bash
   make install
   ```
2. Ejecuta los tests:
   ```bash
   make test
   ```
3. Genera y abre el reporte Allure:
   ```bash
   make report
   ```
