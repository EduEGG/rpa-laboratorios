"""Práctica 5: mantiene dos usuarios aislados en un solo navegador."""

import os
from playwright.sync_api import sync_playwright

PORTAL = "http://127.0.0.1:8010/login.html"
HEADLESS = os.getenv("CODESPACES") == "true"


def iniciar_sesion(context, usuario, contrasena):
    """Abre una página e inicia sesión dentro del contexto recibido."""
    page = context.new_page()
    page.goto(PORTAL)
    page.get_by_label("Usuario").fill(usuario)
    page.get_by_label("Contraseña").fill(contrasena)
    page.get_by_role("button", name="Iniciar sesión").click()
    page.get_by_role("heading", name="Panel de tickets").wait_for()
    return page


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=HEADLESS)

    # TODO 1: cree dos BrowserContext independientes.
    contexto_solicitante = None
    contexto_agente = None

    # TODO 2: inicie sesión como maria.solicitante / rpa123 en el primer contexto.
    pagina_solicitante = None

    # TODO 3: inicie sesión como ana.agente / soporte123 en el segundo contexto.
    pagina_agente = None

    # TODO 4: imprima el rol y el número de tickets visibles en cada página.

    # TODO 5: abra INC-1001 en ambas páginas y compruebe que las herramientas del
    # agente solamente sean visibles en pagina_agente.

    browser.close()
