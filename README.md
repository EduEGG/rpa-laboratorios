# Laboratorios de Automatización Robótica de Procesos

Repositorio de materiales estudiantiles para aprender control de versiones y explorar automatización web con Playwright y Python. Los laboratorios de automatización utilizan aplicaciones locales y datos completamente sintéticos, por lo que pueden desarrollarse sin conectarse a sistemas institucionales ni utilizar información personal real.

## Ruta de laboratorios

| Laboratorio | Contexto | Capacidades principales |
|---|---|---|
| [00. Fundamentos de Git](laboratorios/00_git_fundamentos/) | Control de versiones | Estados, commits, recuperación, ramas, conflictos, GitHub y Pull Requests |
| [01. Consulta de kárdex](laboratorios/01_playwright_kardex/) | Servicios escolares | Navegación, localizadores, formularios, capturas y descargas |
| [02. Mesa de ayuda](laboratorios/02_mesa_ayuda/) | Soporte tecnológico | Autenticación, sesiones, `storage_state`, contextos y roles |

Los laboratorios deben realizarse en orden. El laboratorio 00 establece las bases de Git que se utilizarán para registrar y entregar los siguientes trabajos. El laboratorio 02 recupera los fundamentos de Playwright del laboratorio 01 y agrega administración de sesiones y autorización.

## Requisitos generales

- Visual Studio Code.
- Git 2.23 o posterior.
- Cuenta de GitHub con correo verificado.
- Acceso a internet para publicar repositorios y preparar Playwright.

Los laboratorios 01 y 02 requieren además:

- Python 3.11 o posterior;
- Playwright y Chromium, instalados de acuerdo con cada guía.

Cada laboratorio contiene su propio `README.md` con los prerrequisitos y la secuencia de prácticas. El laboratorio de Git no requiere Python, Playwright ni Docker.

## Forma de trabajo

1. Clone o descargue este repositorio.
2. Lea el `README.md` del laboratorio correspondiente.
3. Abra en VS Code la carpeta indicada.
4. Complete la preparación y las prácticas de su guía.

Para los laboratorios de Playwright:

1. Cree un entorno virtual dentro de la carpeta del laboratorio.
2. Instale las dependencias indicadas.
3. Inicie `server.py` en una terminal.
4. Ejecute las prácticas desde una segunda terminal.
5. Complete los espacios marcados con `TODO`.

Ejemplo:

```bash
cd laboratorios/01_playwright_kardex
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Seguridad y privacidad

- Utilice exclusivamente los datos sintéticos proporcionados.
- No escriba credenciales reales en los scripts.
- No publique archivos de sesión almacenados en `.auth/`.
- No incorpore documentos académicos, laborales o personales reales.
- Revise `git status` antes de cada commit.

## Soluciones docentes

Las soluciones de referencia no forman parte de este repositorio. Se mantienen separadas del material estudiantil y pueden compartirse posteriormente según la dinámica del curso.

## Entregas

Salvo que el docente indique otra cosa, cada entrega debe incluir:

- enlace al repositorio del estudiante;
- carpeta del laboratorio correspondiente;
- SHA del commit final;
- evidencias solicitadas en la guía;
- reflexión breve sobre decisiones y dificultades.

## Licencia de uso académico

Material preparado para actividades educativas. Las aplicaciones, identidades, credenciales, matrículas y tickets incluidos son ficticios.
