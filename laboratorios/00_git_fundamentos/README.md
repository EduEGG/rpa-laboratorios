# Laboratorio: Git para gestionar cambios y colaborar

En este laboratorio utilizarás Git para construir y mantener un pequeño catálogo de cursos. El objetivo no es memorizar comandos, sino comprender **dónde está cada cambio**, **qué se ha guardado** y **qué pueden ver otras personas**.

## Resultado de aprendizaje

Al terminar podrás:

1. distinguir el directorio de trabajo, el área de preparación (*staging*) y el repositorio;
2. crear commits pequeños con mensajes claros;
3. inspeccionar diferencias y consultar el historial;
4. recuperar archivos y revertir cambios sin borrar la historia;
5. desarrollar una modificación en una rama;
6. integrar ramas y resolver un conflicto;
7. publicar y sincronizar trabajo mediante GitHub;
8. explicar el estado de un repositorio usando evidencia de Git.

## Duración y modalidad

- Duración estimada: 3 horas.
- Primera parte: individual.
- Conflicto e integración remota: en parejas.
- Alternativa individual disponible en la práctica 7.
- Entorno: terminal integrada de VS Code y GitHub.

## El modelo que debes conservar

```text
directorio de trabajo  --git add-->  staging  --git commit-->  repositorio local
                                                                  |
                                                               git push
                                                                  v
                                                         repositorio remoto
```

`git status` indica dónde están los cambios. `git diff` muestra los cambios que todavía no están preparados y `git diff --staged` muestra los que formarán parte del siguiente commit.

> Regla del laboratorio: antes de ejecutar un comando que cambie el estado del repositorio, predice el resultado. Después, compruébalo con Git.

## Prerrequisitos

Completa esta sección **antes de la sesión**. El laboratorio no requiere Python, Node.js, Docker ni extensiones de VS Code.

### Equipo y acceso obligatorios

- Computadora con Windows 10/11 de 64 bits o una versión de macOS que todavía reciba actualizaciones de seguridad.
- Permiso para crear y modificar archivos en una carpeta propia, por ejemplo `Documentos`.
- Git 2.23 o posterior. El laboratorio utiliza `git switch`, incorporado en esa versión.
- Editor de texto. Se recomienda Visual Studio Code, pero no se requieren extensiones.
- Terminal: PowerShell o Git Bash en Windows; Terminal en macOS. También puede utilizarse la terminal integrada de VS Code.
- Cuenta personal de GitHub con acceso confirmado al correo asociado.
- Conexión a internet para crear el repositorio, publicar ramas y abrir el Pull Request.
- Carpeta ZIP del laboratorio entregada por el docente.

> No necesitas comprar software. Git, Visual Studio Code y las cuentas personales de GitHub utilizadas en este laboratorio pueden obtenerse sin costo.

### Instalación en Windows 10 u 11

#### 1. Instalar Git

1. Descarga **Git for Windows** desde <https://git-scm.com/install/windows>.
2. Elige el instalador `x64` para la mayoría de los equipos. Utiliza `ARM64` solamente si Windows indica que el procesador es ARM.
3. Ejecuta el instalador. Para este laboratorio puedes conservar las opciones predeterminadas.
4. Cierra y vuelve a abrir PowerShell o VS Code después de instalar.
5. Comprueba la instalación en PowerShell o Git Bash:

   ```powershell
   git --version
   ```

También puede instalarse desde PowerShell mediante `winget`, si está habilitado por la institución:

```powershell
winget install --id Git.Git -e --source winget
```

Si `git` no se reconoce después de reiniciar la terminal, reinicia el equipo. Si continúa el problema, solicita apoyo; no avances hasta que `git --version` funcione.

#### 2. Instalar Visual Studio Code

1. Descarga **Visual Studio Code – User Installer** desde <https://code.visualstudio.com/download>.
2. Ejecuta el archivo `.exe`. La instalación por usuario normalmente no requiere permisos de administrador.
3. Cierra y vuelve a abrir la terminal.
4. Comprueba, de manera opcional:

   ```powershell
   code --version
   ```

Si `code` no se reconoce, todavía puedes abrir VS Code desde el menú Inicio y seleccionar **Archivo > Abrir carpeta**. El comando `code` es conveniente, pero no es obligatorio.

### Instalación en macOS

#### 1. Instalar Git

Abre **Terminal** y ejecuta:

```bash
git --version
```

- Si aparece una versión 2.23 o posterior, Git ya está listo.
- Si macOS ofrece instalar las herramientas de línea de comandos, acepta la instalación y, al terminar, ejecuta nuevamente `git --version`.
- Si la versión es anterior, utiliza el instalador vigente publicado en <https://git-scm.com/install/mac> y vuelve a comprobarla.

No necesitas instalar el entorno completo de Xcode para este laboratorio; las herramientas de línea de comandos son suficientes.

#### 2. Instalar Visual Studio Code

1. Descarga la versión para macOS desde <https://code.visualstudio.com/download>. La descarga universal funciona en equipos Apple silicon e Intel.
2. Abre el archivo `.dmg` y arrastra **Visual Studio Code.app** a **Aplicaciones**.
3. Abre VS Code desde Aplicaciones.
4. Para habilitar el comando opcional `code`, presiona `Cmd+Shift+P`, busca `Shell Command: Install 'code' command in PATH` y ejecútalo.
5. Abre una Terminal nueva y comprueba:

   ```bash
   code --version
   ```

### Preparar la cuenta de GitHub

1. Crea una cuenta o inicia sesión en <https://github.com/>.
2. Verifica la dirección de correo de la cuenta antes de la sesión.
3. Conserva disponible tu método de autenticación y, si está activada, la verificación en dos pasos.
4. No compartas tu contraseña, códigos de recuperación ni tokens con el docente o tus compañeros.

GitHub ya no acepta la contraseña de la cuenta como autenticación de Git por HTTPS. Cuando publiques por primera vez, sigue el inicio de sesión que muestre el navegador o el administrador de credenciales. Si la institución bloquea ese flujo, notifícalo antes del laboratorio.

### Configuración inicial de Git en ambos sistemas

Abre PowerShell, Git Bash o Terminal y configura la identidad que aparecerá en tus commits. Sustituye los valores de ejemplo:

```bash
git config --global user.name "Tu nombre y apellido"
git config --global user.email "tu-correo@example.com"
git config --global init.defaultBranch main
```

Puedes utilizar el correo verificado de GitHub o el correo privado `noreply` que GitHub muestra en la configuración de tu cuenta. Esto no configura una contraseña.

Comprueba los valores:

```bash
git config --global user.name
git config --global user.email
git config --global init.defaultBranch
```

### Comprobación previa obligatoria

Marca cada punto antes de llegar a la sesión:

- [ ] `git --version` muestra Git 2.23 o posterior.
- [ ] Puedo abrir VS Code u otro editor.
- [ ] Puedo abrir una terminal desde el editor.
- [ ] `git config --global user.name` muestra mi nombre.
- [ ] `git config --global user.email` muestra mi correo elegido.
- [ ] Tengo acceso a mi cuenta de GitHub y su correo está verificado.
- [ ] Puedo crear archivos dentro de una carpeta propia.
- [ ] Descargué y descomprimí el laboratorio; no estoy trabajando dentro del ZIP.

### Lo que no debes instalar

Para evitar confusiones, este laboratorio **no requiere**:

- GitHub Desktop;
- Python, Java, Node.js ni otro lenguaje;
- Docker o máquinas virtuales;
- WSL en Windows;
- extensiones de Git para VS Code;
- una clave SSH.

GitHub Desktop puede estar instalado, pero todas las actividades se realizarán en la terminal para que los estados de Git sean visibles.

## Estructura inicial

```text
git_fundamentos/
├── catalogo/
│   ├── README.md
│   ├── cursos/
│   │   ├── automatizacion.md
│   │   └── fundamentos-programacion.md
│   └── docentes.md
├── evidencias/
│   └── .gitkeep
├── INSTRUCCIONES_ENTREGA.md
├── RUBRICA.md
└── reflexion.md
```

Los archivos `GUIA_DOCENTE.md` y `soluciones_docente/` no deben incluirse en la copia entregada al estudiante.

## Preparación del repositorio

### 1. Verifica nuevamente Git

```bash
git --version
git config --global user.name
git config --global user.email
```

Si los dos últimos comandos no muestran tu identidad, vuelve a la sección **Configuración inicial de Git en ambos sistemas**. Como alternativa, configúrala ahora:

```bash
git config --global user.name "Tu nombre"
git config --global user.email "tu-correo@example.com"
```

Utiliza el correo asociado con GitHub si deseas que los commits aparezcan vinculados con tu cuenta. No compartas contraseñas ni tokens.

### 2. Prepara tu copia

Copia la carpeta distribuida por el docente, abre la copia en VS Code y entra en ella desde la terminal. Los comandos del laboratorio se ejecutan desde la raíz de `git_fundamentos`.

Comprueba tu ubicación:

```bash
pwd
```

En PowerShell puedes utilizar:

```powershell
Get-Location
```

## Práctica 1. Crear el repositorio y leer su estado (15 min)

### Predicción

Antes de comenzar, responde en `reflexion.md`: ¿qué esperas que contenga un repositorio recién inicializado?

### Actividad

```bash
git init
git status
```

Examina la salida. Los archivos existen en tu directorio, pero Git todavía no los sigue.

Agrega solamente el catálogo y vuelve a consultar el estado:

```bash
git add catalogo
git status
```

Ahora crea el primer commit:

```bash
git commit -m "Crea catálogo inicial de cursos"
git branch -M main
git status
git log --oneline
```

### Punto de control

Debes poder explicar:

- qué cambió después de `git add`;
- qué cambió después de `git commit`;
- por qué los demás archivos del laboratorio siguen apareciendo como no rastreados.

Registra ahora los materiales de trabajo para que el repositorio pueda terminar limpio:

```bash
git add README.md INSTRUCCIONES_ENTREGA.md RUBRICA.md reflexion.md .gitignore evidencias/.gitkeep
git commit -m "Agrega instrucciones y formato de reflexión"
git status
```

## Práctica 2. Comparar directorio, staging y commit (25 min)

Abre `catalogo/cursos/automatizacion.md` y agrega al final:

```markdown
## Herramientas

- Python
- Playwright
- Git
```

No prepares el cambio todavía. Ejecuta:

```bash
git status
git diff
git diff --staged
```

Anota en `reflexion.md` cuál de los dos comandos `diff` muestra la modificación y por qué.

Prepara el archivo y repite las comparaciones:

```bash
git add catalogo/cursos/automatizacion.md
git diff
git diff --staged
```

Modifica nuevamente el mismo archivo: cambia `Git` por `Git y GitHub`, pero **no ejecutes `git add` otra vez**. Después ejecuta:

```bash
git status
git diff
git diff --staged
```

El mismo archivo debe aparecer en dos estados: una versión está preparada y otra permanece en el directorio de trabajo.

Incluye la versión más reciente en staging y crea el commit:

```bash
git add catalogo/cursos/automatizacion.md
git commit -m "Documenta herramientas del curso de automatización"
```

### Punto de control

```bash
git show --stat
git show
```

Comprueba que el commit contiene `Git y GitHub`.

## Práctica 3. Commits pequeños e historial (20 min)

Realiza estas dos solicitudes como **dos commits separados**:

1. Agrega a `catalogo/docentes.md` una docente ficticia y su área.
2. Crea `catalogo/cursos/control-versiones.md` con nombre, propósito, duración y tres resultados de aprendizaje.

Utiliza mensajes que describan la intención. Por ejemplo:

```text
Agrega docente del área de ingeniería de software
Incorpora curso de control de versiones
```

Inspecciona el resultado:

```bash
git log --oneline --decorate --graph --all
git show HEAD
git show HEAD~1
```

### Pregunta de análisis

¿Por qué sería menos útil registrar ambas solicitudes en un solo commit llamado `cambios`?

## Práctica 4. Recuperar cambios sin guardar (15 min)

Agrega temporalmente esta línea al título de `catalogo/README.md`:

```text
BORRADOR NO PUBLICAR
```

Comprueba la diferencia y descártala:

```bash
git diff catalogo/README.md
git restore catalogo/README.md
git status
```

> `git restore` elimina modificaciones no guardadas del archivo indicado. Antes de usarlo, revisa `git diff` y confirma que no necesitas conservarlas.

Ahora modifica `catalogo/docentes.md`, agrégalo a staging y retíralo de staging sin perder la modificación:

```bash
git add catalogo/docentes.md
git status
git restore --staged catalogo/docentes.md
git status
git diff catalogo/docentes.md
```

Descarta esa modificación cuando hayas comprobado que permanece en el directorio de trabajo:

```bash
git restore catalogo/docentes.md
```

## Práctica 5. Revertir un cambio publicado (20 min)

Simula una decisión incorrecta. En `catalogo/README.md`, cambia el periodo a `2024` y crea un commit:

```bash
git add catalogo/README.md
git commit -m "Actualiza periodo del catálogo"
git log --oneline -3
```

Supón que ese commit ya fue compartido y no debes reescribir el historial. Revierte el commit más reciente:

```bash
git revert --no-edit HEAD
git log --oneline -4
git show --stat HEAD
```

Comprueba que el periodo correcto volvió al archivo y que tanto el error como su reversión permanecen en el historial.

## Práctica 6. Desarrollar en una rama (25 min)

Crea una rama para agregar prerrequisitos:

```bash
git switch -c feature/prerrequisitos
```

En `catalogo/cursos/automatizacion.md`, agrega:

```markdown
## Prerrequisitos

- Fundamentos de programación
- Uso básico de la terminal
```

Registra el cambio:

```bash
git add catalogo/cursos/automatizacion.md
git commit -m "Agrega prerrequisitos de automatización"
git log --oneline --decorate --graph --all
```

Regresa a la rama principal e integra la característica:

```bash
git switch main
git merge feature/prerrequisitos
git log --oneline --decorate --graph --all
```

## Práctica 7. Provocar y resolver un conflicto (30 min)

### Opción A: trabajo en parejas

Cada integrante crea una rama desde `main`:

- estudiante A: `feature/modalidad`;
- estudiante B: `feature/duracion`.

Ambos modificarán la misma línea de `catalogo/README.md`:

- A cambia `Modalidad: presencial` por `Modalidad: híbrida`;
- B cambia esa misma línea por `Modalidad: en línea con sesiones síncronas`.

Cada estudiante crea un commit en su rama. Integren primero `feature/modalidad` en `main` y después intenten integrar `feature/duracion`:

```bash
git switch main
git merge feature/modalidad
git merge feature/duracion
```

### Opción B: trabajo individual

1. Crea `feature/modalidad` desde `main`, cambia la línea a `Modalidad: híbrida` y crea un commit.
2. Regresa a `main` y crea desde ahí `feature/duracion`.
3. En la nueva rama, cambia la misma línea original a `Modalidad: en línea con sesiones síncronas` y crea otro commit.
4. Regresa a `main` e integra las ramas en este orden:

   ```bash
   git switch main
   git merge feature/modalidad
   git merge feature/duracion
   ```

La segunda integración debe detenerse para solicitar tu decisión.

### Resolver el conflicto

1. Ejecuta `git status` y lee la salida completa.
2. Abre `catalogo/README.md` y localiza `<<<<<<<`, `=======` y `>>>>>>>`.
3. Decide una modalidad final; no conserves los marcadores.
4. Prepara el archivo resuelto y concluye la integración.

```bash
git add catalogo/README.md
git commit
git status
git log --oneline --decorate --graph --all
```

En `reflexion.md`, explica qué versiones estaban en conflicto y cuál fue tu decisión. Un conflicto no significa que Git esté dañado: significa que necesita una decisión humana.

## Práctica 8. Publicar y colaborar en GitHub (25 min)

### Crear el remoto

En GitHub crea un repositorio vacío llamado `git-laboratorio-apellido-nombre`. No agregues README, licencia ni `.gitignore` desde GitHub.

Conecta tu repositorio local. Sustituye la URL por la de tu repositorio:

```bash
git remote add origin https://github.com/USUARIO/git-laboratorio-apellido-nombre.git
git remote -v
git push -u origin main
```

Nunca incluyas una contraseña o token dentro de la URL.

### Pull Request

1. Crea una rama llamada `docs/reflexion-final`.
2. Completa `reflexion.md`.
3. Crea un commit y publica la rama:

   ```bash
   git switch -c docs/reflexion-final
   git add reflexion.md
   git commit -m "Documenta aprendizajes del laboratorio"
   git push -u origin docs/reflexion-final
   ```

4. Abre un Pull Request hacia `main`.
5. En la descripción explica qué cambiaste y cómo lo verificaste.
6. Solicita revisión a tu pareja o al docente.
7. Integra el Pull Request cuando esté aprobado.
8. Sincroniza tu copia local:

   ```bash
   git switch main
   git pull --ff-only
   ```

## Reto integrador (15 min)

Sin consultar las instrucciones anteriores, completa esta solicitud:

> Agrega al catálogo un curso llamado **Pruebas de software**, con duración de 24 horas, modalidad híbrida y tres resultados de aprendizaje. Desarrolla el cambio en `feature/pruebas-software`, crea un commit descriptivo, intégralo en `main` y publícalo.

Entrega evidencia mediante estas salidas:

```bash
git status
git log --oneline --decorate --graph --all -12
git remote -v
git rev-parse HEAD
```

## Diagnóstico rápido

### Git dice `nothing to commit`

Ejecuta `git status` y confirma que guardaste el archivo correcto. Si el cambio ya está en un commit, `git log -1 --stat` lo mostrará.

### Git dice `pathspec ... did not match`

Comprueba la ruta y el nombre del archivo. En sistemas sensibles a mayúsculas, `README.md` y `readme.md` son distintos.

### No puedo cambiar de rama

Git puede impedirlo si tus modificaciones se sobrescribirían. Ejecuta `git status` y decide si debes crear un commit, descartar el cambio o guardarlo temporalmente. No uses comandos al azar para forzar el cambio.

### El push fue rechazado

Lee el motivo. Si el remoto contiene trabajo nuevo, usa `git fetch` para inspeccionarlo antes de integrar. No utilices `push --force` en este laboratorio.

### Quiero cancelar una integración con conflicto

```bash
git merge --abort
```

Esto devuelve el repositorio al estado anterior al intento de merge.

## Cierre

Revisa `INSTRUCCIONES_ENTREGA.md`, completa `reflexion.md` y utiliza `RUBRICA.md` para autoevaluar tu trabajo.
