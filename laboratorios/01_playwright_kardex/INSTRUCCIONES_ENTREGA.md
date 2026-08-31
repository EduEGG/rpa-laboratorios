# Entrega del laboratorio: automatización web con Playwright y Python

## Propósito

Desarrollar y documentar un bot de automatización web capaz de navegar por un portal escolar sintético, localizar elementos, consultar matrículas, clasificar resultados, descargar un kárdex y conservar evidencias de ejecución.

Las soluciones de referencia pueden consultarse como apoyo. Sin embargo, la entrega deberá demostrar que el estudiante comprende el flujo y puede adaptarlo para procesar más de un caso.

## Modalidad de trabajo

- Actividad individual.
- Puede desarrollarse localmente con VS Code o desde un GitHub Codespace.
- Utilice exclusivamente las matrículas y los datos sintéticos incluidos en el laboratorio.
- No publique nombres, matrículas ni documentos académicos reales.

## Preparación

1. Obtenga una copia del proyecto proporcionado por el docente.
2. Cree un repositorio de GitHub para su trabajo.
3. Nombre el repositorio con el formato:

   ```text
   rpa-playwright-apellido-nombre
   ```

4. Si el repositorio es privado, agregue al docente como colaborador antes de entregar.
5. Abra el proyecto en VS Code.
6. Prepare el entorno siguiendo el archivo `README.md`.
7. Mantenga `server.py` activo mientras ejecuta las prácticas.

## Desarrollo del laboratorio

Complete las prácticas en el orden indicado:

1. `00_verificar_entorno.py`: comprobar Python, Playwright, Chromium y el portal local.
2. `01_navegar.py`: abrir el portal y recuperar su título y URL.
3. `02_localizadores.py`: identificar elementos mediante roles, etiquetas y nombres accesibles.
4. `03_evidencia.py`: generar capturas de la página y de elementos específicos.
5. `04_consultar_estudiante.py`: enviar una matrícula y clasificar el resultado.
6. `05_descargar_kardex.py`: esperar y guardar una descarga controlada.
7. `06_reto_integrador.py`: integrar consulta, validación, descarga y evidencia.

La práctica 00 es una comprobación técnica. No debe copiarse como solución de la práctica 01.

## Adaptación obligatoria del reto integrador

Modifique `practicas/06_reto_integrador.py` para procesar consecutivamente los siguientes casos:

- una matrícula válida, como `IAI0002`;
- una matrícula inexistente: `IAI9999`.

Para cada matrícula, el bot deberá:

1. completar el campo de consulta;
2. pulsar el botón **Buscar**;
3. leer el resultado mostrado por el portal;
4. clasificarlo como éxito, excepción de negocio o error técnico;
5. descargar el kárdex solamente cuando la matrícula sea válida;
6. generar una captura cuyo nombre incluya la matrícula;
7. imprimir un resultado comprensible en la terminal.

Una salida posible es:

```text
IAI0002 -> Éxito -> descargas/kardex-IAI0002.pdf
IAI9999 -> Excepción de negocio: matrícula inexistente
```

No utilice `time.sleep()` para ocultar problemas de sincronización. Aproveche las esperas automáticas de Playwright y `page.expect_download()` cuando corresponda.

## Evidencias requeridas

Conserve dentro del repositorio, como mínimo:

```text
evidencias/
├── consulta-exitosa.png
├── excepcion-negocio.png
└── ejecucion-final.png

descargas/
└── kardex-<MATRICULA>.pdf
```

### Descripción de las evidencias

- `consulta-exitosa.png`: portal mostrando el resultado de una matrícula válida.
- `excepcion-negocio.png`: portal mostrando el resultado de una matrícula inexistente.
- `ejecucion-final.png`: terminal con la ejecución completa, los casos procesados y la ruta del PDF.
- `kardex-<MATRICULA>.pdf`: archivo descargado automáticamente por el bot.

Las capturas respaldan la ejecución, pero no sustituyen al código funcional. No se requiere grabación de video.

> **Importante:** el archivo `.gitignore` original excluye el contenido de `evidencias/` y `descargas/`. Para incluir las evidencias requeridas en la entrega, puede agregarlas explícitamente con:
>
> ```bash
> git add -f evidencias/consulta-exitosa.png
> git add -f evidencias/excepcion-negocio.png
> git add -f evidencias/ejecucion-final.png
> git add -f descargas/kardex-IAI0002.pdf
> ```

## Historial de trabajo

Realice al menos un commit por práctica. Utilice mensajes que expliquen el avance, por ejemplo:

```text
Completa práctica 01: navegación
Completa práctica 02: localizadores
Agrega evidencias de consulta
Implementa descarga controlada del kárdex
Adapta reto integrador para procesar dos casos
```

No se penalizarán los errores intermedios visibles en el historial. Se valorará que los commits permitan observar el proceso de desarrollo.

## Reflexión

Complete `reflexion.txt` y responda también, en el comentario de entrega de Google Classroom:

> ¿Qué parte del código modificaste o comprendiste mejor y qué error encontraste durante el desarrollo?

La respuesta debe referirse a decisiones o dificultades concretas de su implementación.

## Entrega en Google Classroom

Entregue los siguientes elementos:

1. enlace al repositorio de GitHub;
2. SHA del commit final;
3. confirmación de que el archivo principal es `practicas/06_reto_integrador.py`;
4. indicación del entorno utilizado: equipo local o GitHub Codespaces;
5. respuesta breve a la pregunta de reflexión.

Para obtener el SHA del commit final puede ejecutar:

```bash
git rev-parse HEAD
```

Antes de entregar, compruebe que el docente pueda abrir el repositorio y que las evidencias estén presentes en GitHub.

## Lista de verificación

- [ ] El portal local se inicia correctamente.
- [ ] Las prácticas 01 a 06 contienen una implementación funcional.
- [ ] El reto procesa una matrícula válida y una inexistente.
- [ ] El bot descarga el PDF solamente para la matrícula válida.
- [ ] Las capturas incluyen la matrícula correspondiente.
- [ ] `reflexion.txt` está completo.
- [ ] El repositorio contiene un historial progresivo de commits.
- [ ] Las evidencias y el PDF están visibles en GitHub.
- [ ] El enlace y el SHA final se entregaron en Google Classroom.

## Rúbrica de evaluación

| Criterio | Valor |
|---|---:|
| Prácticas ejecutables y completas | 25 puntos |
| Adaptación para procesar ambos casos | 20 puntos |
| Clasificación correcta de resultados | 15 puntos |
| Evidencias y PDF generados por el bot | 15 puntos |
| Uso adecuado de Playwright | 10 puntos |
| Historial progresivo de commits | 5 puntos |
| Explicación y reflexión personal | 10 puntos |
| **Total** | **100 puntos** |

## Criterio de integridad académica

Puede consultar el material y las soluciones de referencia proporcionadas. La evaluación no se basa únicamente en reproducir ese código, sino en:

- adaptar el reto para procesar dos casos;
- explicar las decisiones tomadas;
- generar evidencias propias;
- conservar un historial de trabajo coherente;
- demostrar que la solución puede ejecutarse nuevamente.

Si utiliza código o recursos adicionales, indíquelo en `reflexion.txt`.
