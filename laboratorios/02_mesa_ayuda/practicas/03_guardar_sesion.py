"""Práctica 3: guarda cookies y almacenamiento local de una sesión autenticada."""

import os
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PORTAL = "http://127.0.0.1:8010/login.html"
ESTADO = ROOT / ".auth" / "solicitante.json"
HEADLESS = os.getenv("CODESPACES") == "true"
ESTADO.parent.mkdir(exist_ok=True)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=HEADLESS)
    context = browser.new_context()
    page = context.new_page()
    page.goto(PORTAL)

    page.get_by_label("Usuario").fill("maria.solicitante")
    page.get_by_label("Contraseña").fill("rpa123")
    page.get_by_role("button", name="Iniciar sesión").click()
    page.get_by_role("heading", name="Panel de tickets").wait_for()

    # TODO 1: use context.storage_state(path=ESTADO) para guardar la sesión.
    # El estado puede contener cookies y almacenamiento local; por ello .auth/ está
    # excluida del repositorio mediante .gitignore.

    browser.close()

# TODO 2: compruebe que ESTADO existe e imprima su ruta y tamaño.
