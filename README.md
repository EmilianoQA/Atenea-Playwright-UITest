# Atenea-Playwright-UITest: Framework de Automatización Profesional

Framework de automatización de pruebas End-to-End para la aplicación web "Atenea Conocimientos", construido con Python, Playwright y Pytest. Este proyecto está diseñado para servir como un portafolio profesional, demostrando la implementación de patrones de diseño, herramientas y buenas prácticas estándar en la industria del QA Automation.

---

### ✨ Arquitectura y Fortalezas Clave

*   **Page Object Model (POM):**
    Arquitectura de prueba robusta que separa la lógica de los tests de la definición de la UI para un código limpio y escalable.

*   **Data-Driven & Parametrizado:**
    Los tests son impulsados por datos externos (`JSON`) y utilizan la **parametrización** de Pytest para ejecutar múltiples escenarios con código mínimo.

*   **Testing Híbrido (UI + API):**
    Las pruebas E2E capturan y validan respuestas clave de la API (`status code`, `método`, `payload`) para una detección de errores más profunda.

*   **Reportes Avanzados con Allure:**
    Generación de reportes visuales e interactivos que ofrecen una visibilidad total de los resultados, con historial, métricas y adjuntos automáticos en caso de fallo (screenshots/videos).

*   **Calidad de Código Automatizada:**
    Integración de **`Black`**, **`Ruff`** y **`pre-commit` hooks** para garantizar un código limpio, consistente y libre de errores básicos en cada commit.

---

### 🛠️ Stack Tecnológico

| Propósito | Tecnología |
| :--- | :--- |
| Lenguaje | **Python** |
| Automatización | **Playwright** |
| Testing Framework | **Pytest** |
| **Reportes** | **Allure Framework** |
| Manejo de Datos | **JSON** |
| Calidad de Código | **Black, Ruff, pre-commit** |

---

### 🚀 Guía de Inicio Rápido

1.  **Clonar y configurar el entorno:**
    ```bash
    git clone https://github.com/EmilianoQA/Atenea-Playwright-UITest.git
    cd Atenea-Playwright-UITest
    make install
    ```

2.  **Crear el archivo de entorno:**
    *   Crea un archivo llamado `.env` en la raíz del proyecto.
    *   Añade la URL base: `BASE_URL="https://qa.ateneaconocimientos.com"`

3.  **Ejecutar Pruebas y Ver Reporte:**
    ```bash
    # Ejecuta todos los tests y genera los datos para el reporte
    make test

    # Levanta el servidor de Allure y abre el reporte en el navegador
    make report
    ```
