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

    contexto_solicitante = browser.new_context()
    contexto_agente = browser.new_context()
    pagina_solicitante = iniciar_sesion(contexto_solicitante, "maria.solicitante", "rpa123")
    pagina_agente = iniciar_sesion(contexto_agente, "ana.agente", "soporte123")

    for pagina, rol_esperado, cantidad_esperada in (
        (pagina_solicitante, "Solicitante", 2),
        (pagina_agente, "Agente", 3),
    ):
        rol = pagina.get_by_test_id("session-role").inner_text()
        cantidad = pagina.locator("[data-ticket-id]").count()
        assert (rol, cantidad) == (rol_esperado, cantidad_esperada)
        print(f"{rol}: {cantidad} tickets visibles")
        pagina.get_by_role("button", name="Abrir INC-1001").click()
        assert pagina.get_by_test_id("ticket-detail").is_visible()

    assert not pagina_solicitante.get_by_role("heading", name="Herramientas del agente").is_visible()
    assert pagina_agente.get_by_role("heading", name="Herramientas del agente").is_visible()
    print("INC-1001 visible en ambos contextos; herramientas disponibles solo para Agente.")

    browser.close()
