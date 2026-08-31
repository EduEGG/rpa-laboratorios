"""Práctica 1: automatiza un inicio de sesión correcto e identifica el perfil."""

import os
from playwright.sync_api import sync_playwright

PORTAL = "http://127.0.0.1:8010/login.html"
HEADLESS = os.getenv("CODESPACES") == "true"
USUARIO = "maria.solicitante"
CONTRASENA = "rpa123"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=HEADLESS, slow_mo=250)
    page = browser.new_page()
    page.goto(PORTAL)

    # TODO 1: localice el campo Usuario mediante su etiqueta y escriba USUARIO.
    # fill() reemplaza cualquier contenido previo del campo.

    # TODO 2: complete el campo Contraseña sin utilizar selectores CSS.

    # TODO 3: pulse el botón Iniciar sesión mediante su rol y nombre accesible.

    # TODO 4: compruebe que el encabezado Panel de tickets sea visible.
    # La navegación se espera automáticamente porque la acción anterior la provoca.

    # TODO 5: obtenga el texto de data-testid="session-role" e imprímalo.

    browser.close()
