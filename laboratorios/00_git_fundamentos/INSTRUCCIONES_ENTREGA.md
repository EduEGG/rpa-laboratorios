# Entrega: laboratorio de Git

## Producto

Entrega un repositorio de GitHub que muestre el proceso completo del laboratorio. La evaluación considera tanto el estado final como la calidad del historial.

## Elementos requeridos

1. Enlace al repositorio de GitHub.
2. SHA del commit final de `main`.
3. Pull Request de `docs/reflexion-final`, integrado o aprobado.
4. `reflexion.md` completo.
5. Curso **Pruebas de software** incorporado mediante la rama solicitada.
6. Historial que conserve el commit del periodo incorrecto y su reversión.
7. Merge del ejercicio de conflicto visible en el historial.

Obtén el SHA final con:

```bash
git rev-parse HEAD
```

## Evidencia verificable

Antes de entregar, ejecuta:

```bash
git status
git log --oneline --decorate --graph --all -15
git remote -v
git branch --merged main
```

La salida esperada debe demostrar que:

- el directorio de trabajo está limpio;
- `HEAD` está en `main`;
- las ramas del laboratorio fueron integradas;
- `origin` apunta al repositorio del estudiante;
- los commits tienen mensajes comprensibles.

Incluye en el comentario de entrega:

```text
Repositorio: <URL>
Commit final: <SHA>
Pull Request: <URL>
Modalidad del conflicto: pareja / individual
```

## Lista de verificación

- [ ] El repositorio es accesible para el docente.
- [ ] No contiene contraseñas, tokens ni datos personales reales.
- [ ] El árbol de trabajo está limpio.
- [ ] Los cambios se distribuyen en commits con una intención reconocible.
- [ ] El historial conserva la reversión solicitada.
- [ ] La integración con conflicto fue resuelta y documentada.
- [ ] El reto integrador está presente en `main`.
- [ ] La reflexión usa evidencia concreta de Git.
- [ ] El enlace, Pull Request y SHA final fueron entregados.

## Integridad académica

Puedes consultar documentación y discutir conceptos con otras personas. La entrega debe contener tus propios commits y debes poder explicar cualquier comando utilizado. Si recibiste ayuda para resolver un conflicto o recuperar trabajo, descríbela brevemente en `reflexion.md`.
