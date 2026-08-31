"""Práctica 2: diferencia un resultado esperado de un error técnico."""

import os
from playwright.sync_api import sync_playwright

PORTAL = "http://127.0.0.1:8010/login.html"
HEADLESS = os.getenv("CODESPACES") == "true"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=HEADLESS)
    page = browser.new_page()
    page.goto(PORTAL)

    # TODO 1: escriba maria.solicitante como usuario y una contraseña incorrecta.

    # TODO 2: pulse Iniciar sesión.

    # TODO 3: localice el mensaje con role="alert" e imprima su texto.
    # Las credenciales rechazadas son un resultado previsto del proceso, no una falla
    # de Playwright ni una excepción técnica.

    # TODO 4: confirme que la URL sigue siendo login.html.

    browser.close()
