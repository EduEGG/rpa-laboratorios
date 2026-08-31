"""Práctica 4: abre el área protegida sin repetir el formulario de acceso."""

import os
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
DASHBOARD = "http://127.0.0.1:8010/dashboard.html"
ESTADO = ROOT / ".auth" / "solicitante.json"
HEADLESS = os.getenv("CODESPACES") == "true"

if not ESTADO.exists():
    raise FileNotFoundError("Ejecute primero 03_guardar_sesion.py")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=HEADLESS)

    # TODO 1: cree un contexto nuevo con storage_state=ESTADO.
    context = None

    # TODO 2: cree una página dentro del contexto y visite DASHBOARD directamente.
    page = None

    # TODO 3: compruebe que el perfil visible sea Solicitante.

    # TODO 4: cuente los artículos de ticket mediante data-ticket-id.

    # TODO 5: cierre la sesión y compruebe el regreso a login.html.

    browser.close()
