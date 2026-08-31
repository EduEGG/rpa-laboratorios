"""Reto: consulta, valida, descarga y conserva evidencia."""

from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PORTAL = "http://127.0.0.1:8000"

# Cambie esta entrada para probar el camino feliz o una excepción de negocio.
MATRICULA = "IAI0003"
EVIDENCIAS = ROOT / "evidencias"
DESCARGAS = ROOT / "descargas"
EVIDENCIAS.mkdir(exist_ok=True)
DESCARGAS.mkdir(exist_ok=True)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    page = browser.new_page()

    # try contiene el flujo que se desea ejecutar. Si alguna instrucción
    # técnica falla, Python transfiere el control al bloque except.
    try:
        # TODO 1: navegar al portal.
        # Esta operación establece la aplicación con la que trabajará el bot.

        # TODO 2: capturar MATRICULA y buscar.
        # Utilice localizadores semánticos por etiqueta, rol y nombre.

        # TODO 3: decidir si es éxito o excepción de negocio.
        # Lea el texto del panel. Una matrícula inexistente no es necesariamente
        # un error técnico: es un resultado previsto por las reglas del proceso.

        # TODO 4: si es éxito, descargar el kárdex.
        # Prepare expect_download() antes del clic y controle la ruta final.

        # TODO 5: guardar una captura con la matrícula en el nombre.
        # Incluir el identificador del caso facilita relacionar la evidencia.

        # TODO 6: imprimir un resultado comprensible.
        # La salida debería distinguir éxito, excepción de negocio y fallo.
        pass

    # Esta captura genérica simplifica el laboratorio. En un sistema real se
    # utilizarían excepciones más específicas y logs estructurados.
    except Exception as error:
        # TODO 7: guardar evidencia técnica antes de informar el error.
        # full_page=True permite conservar mayor contexto para el diagnóstico.
        print("Error técnico:", error)

    # finally siempre se ejecuta, haya éxito o error. Es el lugar adecuado para
    # liberar recursos que no deben permanecer activos.
    finally:
        browser.close()
