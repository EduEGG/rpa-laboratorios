# Laboratorios de Automatización Robótica de Procesos

Repositorio de materiales estudiantiles para explorar automatización web con Playwright y Python. Cada laboratorio utiliza una aplicación local y datos completamente sintéticos, por lo que puede desarrollarse sin conectarse a sistemas institucionales ni utilizar información personal real.

## Ruta de laboratorios

| Laboratorio | Contexto | Capacidades principales |
|---|---|---|
| [01. Consulta de kárdex](laboratorios/01_playwright_kardex/) | Servicios escolares | Navegación, localizadores, formularios, capturas y descargas |
| [02. Mesa de ayuda](laboratorios/02_mesa_ayuda/) | Soporte tecnológico | Autenticación, sesiones, `storage_state`, contextos y roles |

Los laboratorios deben realizarse en orden. El segundo recupera los fundamentos del primero y agrega administración de sesiones y autorización.

## Requisitos generales

- Python 3.11 o posterior.
- Visual Studio Code.
- Git.
- Acceso a internet durante la instalación inicial de Playwright y Chromium.

Cada laboratorio contiene su propio `README.md`, `requirements.txt`, portal local y secuencia de prácticas.

## Forma de trabajo

1. Clone o descargue este repositorio.
2. Abra en VS Code la carpeta del laboratorio correspondiente.
3. Cree un entorno virtual dentro de esa carpeta.
4. Instale las dependencias indicadas en su guía.
5. Inicie `server.py` en una terminal.
6. Ejecute las prácticas desde una segunda terminal.
7. Complete los espacios marcados con `TODO`.

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
