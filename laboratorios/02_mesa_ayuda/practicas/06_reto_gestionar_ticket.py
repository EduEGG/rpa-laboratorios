"""Reto: un agente clasifica y asigna un ticket conservando evidencia."""

import os
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PORTAL = "http://127.0.0.1:8010/login.html"
EVIDENCIAS = ROOT / "evidencias"
HEADLESS = os.getenv("CODESPACES") == "true"
EVIDENCIAS.mkdir(exist_ok=True)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=HEADLESS, slow_mo=200)
    context = browser.new_context()
    page = context.new_page()

    try:
        # TODO 1: inicie sesión como ana.agente / soporte123.

        # TODO 2: compruebe el rol Agente y abra el ticket INC-1001.

        # TODO 3: cambie la prioridad a Alta, el grupo a Seguridad y el estado a
        # En proceso mediante select_option(label=...) o select_option(value=...).

        # TODO 4: guarde los cambios y verifique el mensaje de confirmación.

        # TODO 5: valide en el detalle los nuevos valores.

        # TODO 6: capture únicamente el panel data-testid="ticket-detail" como
        # evidencias/INC-1001-actualizado.png.

        # TODO 7: imprima un resumen del resultado.
        pass
    except Exception as error:
        page.screenshot(path=EVIDENCIAS / "error-tecnico.png", full_page=True)
        print("Error técnico:", error)
        raise
    finally:
        browser.close()
