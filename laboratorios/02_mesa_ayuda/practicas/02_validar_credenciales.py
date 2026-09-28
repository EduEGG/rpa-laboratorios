"""Práctica 2: diferencia un resultado esperado de un error técnico."""

import os
from playwright.sync_api import sync_playwright

PORTAL = "http://127.0.0.1:8010/login.html"
HEADLESS = os.getenv("CODESPACES") == "true"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=HEADLESS)
    page = browser.new_page()
    page.goto(PORTAL)

    page.get_by_label("Usuario").fill("maria.solicitante")
    page.get_by_label("Contraseña").fill("contraseña_incorrecta")
    page.get_by_role("button", name="Iniciar sesión").click()
    alerta = page.get_by_role("alert")
    assert alerta.is_visible()
    print("Resultado esperado:", alerta.inner_text())
    assert page.url.endswith("/login.html"), page.url

    browser.close()
