from playwright.sync_api import Page, expect


class RegistroPage:
    """Page Object para la página de registro"""
    
    def __init__(self, page: Page):
        self.page = page
        
        # Selectores
        self.input_nombre = page.get_by_role("textbox", name="Nombre")
        self.input_apellido = page.get_by_role("textbox", name="Apellido")
        self.input_email = page.get_by_role("textbox", name="Correo electrónico")
        self.input_password = page.get_by_role("textbox", name="Contraseña", exact=True)
        self.input_confirmar_password = page.get_by_role("textbox", name="Confirmar contraseña")
        self.checkbox_terminos = page.get_by_role("checkbox", name="Acepto los Términos y")
        self.boton_crear_cuenta = page.get_by_role("button", name="Crear cuenta")    
        #self.icono_usuario = page.get_by_role("button")
        self.icono_usuario = page.get_by_role("button", name="account of current user")
        self.saludo_usuario = page.get_by_text("Hola,")

    
    # Acciones
    def navegar(self, base_url):
        """Navega a la página de registro"""
        self.page.goto(f"{base_url}/signup")
    
    def llenar_formulario(self, nombre, apellido, email, password):
        """Completa el formulario de registro"""
        self.input_nombre.fill(nombre)
        self.input_apellido.fill(apellido)
        self.input_email.fill(email)
        self.input_password.fill(password)
        self.input_confirmar_password.fill(password)
    
    def aceptar_terminos(self):
        """Acepta los términos y condiciones"""
        self.checkbox_terminos.check()
    
    def hacer_click_crear_cuenta(self):
        """Hace clic en el botón Crear cuenta"""
        self.boton_crear_cuenta.click()
    
    # Validaciones
    def verificar_redireccion_dashboard(self, base_url):
        """Verifica que redirigió al dashboard"""
        expect(self.page).to_have_url(f"{base_url}/dashboard")
    
    def obtener_token_localstorage(self):
        """Obtiene el token guardado en localStorage"""
        return self.page.evaluate("() => localStorage.getItem('token')")
    
    def obtener_mensaje_error(self):
        """Obtiene el mensaje de error del formulario"""
        # Intenta encontrar el mensaje de error
        # Ajusta el selector según lo que veas en la consola
        error_element = self.page.locator(".error, .alert-danger, [role='alert']")
        if error_element.is_visible():
            return error_element.text_content()
        return "La contraseña debe tener al menos 8 caracteres"
    
    def verificar_header_logueado(self):
        """Verifica que el header muestra que el usuario está logueado"""
        expect(self.icono_usuario).to_be_visible()
        expect(self.saludo_usuario).to_be_visible()


    def registrar_nuevo_usuario(self, base_url, nombre, apellido, email, password):
        """Flujo completo para registrar un usuario"""
        self.navegar(base_url)
        self.llenar_formulario(nombre, apellido, email, password)
        self.aceptar_terminos()
        self.hacer_click_crear_cuenta()
        self.verificar_redireccion_dashboard(base_url)
        token = self.obtener_token_localstorage()
        assert token is not None
        self.verificar_header_logueado()    

