from playwright.sync_api import Page, expect

class LoginPage:
    """Page Object para la página de login"""
    
    def __init__(self, page: Page):
        self.page = page
        
        # Selectores
        self.email = page.get_by_role("textbox", name="Correo Electrónico")
        self.password = page.get_by_role("textbox", name="Contraseña")
        self.boton_ingresar = page.get_by_role("button", name="Ingresar")
        self.icono_usuario = page.get_by_role("button", name="account of current user")
        self.saludo_usuario = page.get_by_text("Hola,")
        self.error_message_locator = page.locator(".MuiAlert-message.css-1xsto0d")  
    
    def navegar(self, base_url):
        """Navega a la página de login"""
        self.page.goto(f"{base_url}/login")

    def validar_url(self, base_url):
        """Valida que está en la página de login"""
        expect(self.page).to_have_url(f"{base_url}/login")

    def validar_header(self):   
        """Valida que el header esté visible"""
        expect(self.page.get_by_role("heading", name="Acceso de Estudiantes")).to_be_visible()

    def validar_elementos(self):
        """Valida que los elementos del formulario estén visibles"""
        expect(self.email).to_be_visible()
        expect(self.password).to_be_visible()
        expect(self.boton_ingresar).to_be_visible()
    
    def llenar_formulario(self, email, password):
        """Completa el formulario de login"""
        self.email.fill(email)
        self.password.fill(password)
    
    def capturar_respuesta_y_click(self, func):
        """Captura la respuesta de la API al hacer clic en Ingresar"""
        with self.page.expect_response(func) as response_info:
            self.boton_ingresar.click()
        return response_info.value
    
    def click_boton_ingresar(self):
        """Hace clic en el botón Ingresar"""
        self.boton_ingresar.click()

    def validar_respuesta_api(self, response, status_code):
        """Valida que la respuesta de la API tenga el código esperado"""
        assert response.status == status_code
    
    def verificar_redireccion_dashboard(self, base_url):
        """Verifica que redirigió al dashboard"""
        expect(self.page).to_have_url(f"{base_url}/dashboard")
    
    def obtener_token_localstorage(self):
        """Obtiene el token guardado en localStorage"""
        return self.page.evaluate("() => localStorage.getItem('token')")
    
    def verificar_header_logueado(self):
        """Verifica que el header muestra que el usuario está logueado"""
        expect(self.icono_usuario).to_be_visible()
        expect(self.saludo_usuario).to_be_visible()     
    def validar_mensaje_error(self, mensaje_esperado: str):
        """Verifica que el mensaje de error es visible y contiene el texto esperado.        """
        expect(self.error_message_locator).to_be_visible()
        expect(self.error_message_locator).to_have_text(mensaje_esperado)

    def login_usuario(self, base_url, email, password):
        """Flujo completo para loguear un usuario"""
        self.navegar(base_url)
        self.validar_url(base_url)
        self.validar_header()
        self.validar_elementos()
        self.llenar_formulario(email, password)
        response = self.capturar_respuesta_y_click(lambda response: "/students/login" in response.url)
        self.validar_respuesta_api(response, 200)
        self.verificar_redireccion_dashboard(base_url)
        token = self.obtener_token_localstorage()
        assert token is not None
        self.verificar_header_logueado()
    