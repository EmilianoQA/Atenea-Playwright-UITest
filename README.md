# Atenea-Playwright-UITest: Framework de Automatización Profesional

Framework de automatización de pruebas End-to-End para la aplicación "Atenea Conocimientos", construido con Python, Playwright y Pytest. Este proyecto está diseñado para servir como un portafolio profesional que demuestra la implementación de patrones de diseño y herramientas estándar en la industria del QA Automation.

---

### ✨ Arquitectura y Fortalezas Clave

Este framework está construido para ser robusto, escalable y fácil de usar, aplicando los siguientes conceptos clave:

*   **Page Object Model (POM):**
    La arquitectura del proyecto separa la lógica de los tests de la definición de la UI. Cada página tiene su propia clase, lo que resulta en un código limpio, reutilizable y fácil de mantener.

*   **Data-Driven Testing (DDT) y Parametrización:**
    Los tests son impulsados por datos externos (`JSON`). Se utiliza la **parametrización** de Pytest (`@pytest.mark.parametrize`) para ejecutar una misma función de test con múltiples conjuntos de datos (ej. login exitoso, email inválido, contraseña inválida), eliminando la duplicación de código de forma elegante.

*   **Testing Híbrido (UI + API):**
    Las pruebas E2E no se limitan a la UI. Capturan y validan respuestas clave de la API (`status code`, `método`, `payload`) en flujos críticos, asegurando la correcta comunicación con el backend para una detección de errores más profunda.

*   **Reportes Avanzados con Allure:**
    El framework está integrado con Allure para generar reportes visuales e interactivos. Estos ofrecen una visibilidad total de los resultados, con historial, métricas y adjuntos automáticos (screenshots/videos) en caso de fallo, facilitando el análisis y la depuración.

---

### 🛠️ Stack Tecnológico

| Propósito             | Tecnología          |
| :-------------------- | :------------------ |
| Lenguaje              | **Python**          |
| Automatización        | **Playwright**      |
| Testing Framework     | **Pytest**          |
| Reportes              | **Allure Framework**|
| Manejo de Datos       | **JSON**            |
| Gestión de Entorno    | **python-dotenv**   |

---

### 🚀 Guía de Inicio Rápido

#### **1. Configuración del Proyecto**

```bash
# Clona el repositorio
git clone https://github.com/EmilianoQA/Atenea-Playwright-UITest.git
cd Atenea-Playwright-UITest

# (Recomendado) Crea e inicia un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instala todas las dependencias
pip install -r requirements.txt
```

#### **2. Configuración del Entorno**

Crea un archivo llamado `.env` en la raíz del proyecto y añade la URL base:
```
BASE_URL="https://qa.ateneaconocimientos.com"
```

#### **3. Ejecución de Pruebas y Reportes**

```bash
# Instala los navegadores de Playwright
playwright install

# Ejecuta los tests y genera los resultados para Allure
pytest --alluredir=reports

# Genera y abre el reporte de Allure en tu navegador
allure serve reports
```