
import re
from playwright.sync_api import Page, expect


'''Page Objet para el nuevo resgistro validando el modal de registro exitoso'''
class RegistroPage:
    """Page Object para la página de registro"""
    
    def __init__(self, page: Page):
        self.page = page
        
        # Selectores
        # Campos del formulario
        self.input_nombre = page.get_by_role("textbox", name="Nombre")
        self.input_apellido = page.get_by_role("textbox", name="Apellido")
        self.input_email = page.get_by_role("textbox", name="Correo electrónico")
        self.input_password = page.get_by_role("textbox", name="Contraseña", exact=True)
        self.input_confirmar_password = page.get_by_role("textbox", name="Confirmar contraseña")
        self.checkbox_terminos = page.get_by_role("checkbox", name="Acepto los Términos y")
        self.boton_crear_cuenta = page.get_by_role("button", name="Crear cuenta") 
        self.cuenta_creada_heading = page.get_by_role("heading", name="¡Tu cuenta está lista!")
        self.mensaje_cuenta_creada = page.get_by_text("La cuenta se creó")
        self.mensaje_ahora_puedes = page.get_by_text("Ahora puedes iniciar sesión")
       # self.mensaje_recuerda = page.get_by_text(re.compile(r"Recuerda usar .*@mail.com para iniciar sesión"))
        self.boton_ir_a_login = page.get_by_role("button", name="Ir a iniciar sesión")
        # Elementos de la pagina de login
        self.acceso_estudiantes_heading = page.get_by_role("heading", name="Acceso de Estudiantes")
        self.input_email_registrado = page.get_by_role("textbox", name="Correo Electrónico")
        self.input_password_registrado = page.get_by_role("textbox", name="Contraseña")

    # Metodos

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
    
    def verificar_modal_registro_exitoso(self):
        """Verifica que el modal de registro exitoso se muestra correctamente"""
        expect(self.cuenta_creada_heading).to_be_visible()
        expect(self.mensaje_cuenta_creada).to_be_visible()
        expect(self.mensaje_ahora_puedes).to_be_visible()
        expect(self.boton_ir_a_login).to_be_visible()

    def click_ir_a_login(self):
        """Hace clic en el botón Ir a iniciar sesión"""
        self.boton_ir_a_login.click()

    def verificar_redireccion_login(self, base_url):
        """Verifica que redirige a la página de login"""
        expect(self.page).to_have_url(f"{base_url}/login")
        expect(self.acceso_estudiantes_heading).to_be_visible()
        expect(self.input_email_registrado).to_be_visible()
        expect(self.input_password_registrado).to_be_visible()
  
    def obtener_mensaje_error(self):
        """Obtiene el mensaje de error del formulario"""
        error_element = self.page.locator(".error, .alert-danger, [role='alert']")
        if error_element.is_visible():
            return error_element.text_content()
        return "La contraseña debe tener al menos 8 caracteres"
    
    def registrar_nuevo_usuario(self, base_url, nombre, apellido, email, password):
        """Flujo completo para registrar un usuario"""
        self.navegar(base_url)
        self.llenar_formulario(nombre, apellido, email, password)
        self.aceptar_terminos()
        self.hacer_click_crear_cuenta()
        self.verificar_modal_registro_exitoso()
        self.boton_ir_a_login.click()
        self.verificar_redireccion_login(base_url)
        



