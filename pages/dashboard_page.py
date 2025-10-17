from playwright.sync_api import Page, expect



class DashboardPage:
    '''Page object model para la página de dashboard''' 
    def __init__(self, page: Page):
        self.page = page

# Selectores
        self.saludo_usuario = page.get_by_text("Hola,")
        self.nivel_usuario   = page.get_by_text("Nivel")
        self.talleres_usuario = page.get_by_role("heading", name="Mis Talleres")
        self.icono_usuario = page.get_by_role("button", name="account of current user")
        self.link_tickets = page.get_by_role("link", name="Tickets comunidad")
        self.link_top_atenienses = page.get_by_role("link", name="Top Atenienses")
        self.link_mis_certificados = page.get_by_role("link", name="Mis Certificados")
        self.link_desafios = page.get_by_role("link", name="Desafíos")
        self.link_mis_talleres = page.get_by_role("link", name="Mis Talleres")

    def navegar(self, base_url):
        """Navega a la página de dashboard"""
        self.page.goto(f"{base_url}/dashboard") 

    def verificar_elementos_dashboard(self):
        """Verifica que los elementos del dashboard estén visibles"""
        expect(self.saludo_usuario).to_be_visible()
        expect(self.nivel_usuario).to_be_visible()
        expect(self.talleres_usuario).to_be_visible()
        expect(self.icono_usuario).to_be_visible()
        expect(self.link_tickets).to_be_visible()
        expect(self.link_top_atenienses).to_be_visible()
        expect(self.link_mis_certificados).to_be_visible()
        expect(self.link_desafios).to_be_visible()
        expect(self.link_mis_talleres).to_be_visible()



