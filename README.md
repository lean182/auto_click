# 🚂 AutoClick Pro

AutoClick Pro es un autoclicker desarrollado en Python con una arquitectura modular, pensado para ser rápido, extensible y fácil de mantener.

## Requisitos

* Python 3.12 o superior
* Windows
* Visual Studio Code (recomendado)

## Crear el entorno virtual

Desde la carpeta del proyecto:

```bash
python -m venv .venv
```

## Activar el entorno virtual

### Git Bash

```bash
source .venv/Scripts/activate
```

### CMD

```cmd
.venv\Scripts\activate
```

### PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Si todo salió bien, la terminal mostrará:

```text
(.venv)
```

## Instalar las dependencias

```bash
pip install customtkinter
pip install pynput
pip install pyautogui
pip install keyboard
pip install pyinstaller
```

O todas juntas:

```bash
pip install customtkinter pynput pyautogui keyboard pyinstaller
```

## Guardar las dependencias

Cuando se agreguen nuevas librerías:

```bash
pip freeze > requirements.txt
```

## Instalar dependencias desde requirements.txt

```bash
pip install -r requirements.txt
```

## Ejecutar el proyecto

Con el entorno virtual activado:

```bash
python main.py
```

## Estructura del proyecto

```text
AutoClicker/
│
├── .venv/
├── assets/
│
├── src/
│   ├── __init__.py
│   ├── gui.py
│   ├── clicker.py
│   ├── hotkeys.py
│   ├── config.py
│   ├── randomizer.py
│   └── stats.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Funciones implementadas

* Interfaz gráfica con CustomTkinter.
* Motor de autoclick en un hilo independiente.
* Clic izquierdo.
* Hotkey **F6** para iniciar/detener.
* Hotkey **ESC** para detener.
* Contador de clics.
* Variación aleatoria en el intervalo entre clics.

## Próximas funciones

* Intervalo configurable desde la interfaz.
* Variación configurable.
* Clic izquierdo o derecho.
* Guardar configuración en `config.json`.
* Estadísticas.
* Múltiples perfiles.
* Grabador de macros.
* Múltiples posiciones de clic.
* Exportación a ejecutable portable (.exe).

## Buenas prácticas

* Guardar siempre los archivos antes de ejecutar (`Ctrl + S`).
* Mantener la lógica separada de la interfaz.
* Probar cada cambio antes de agregar nuevas funciones.
* Hacer commits frecuentes si se utiliza Git.

## Generar el ejecutable

Cuando el proyecto esté terminado:

```bash
pyinstaller --onefile --windowed main.py
```

Si se utiliza un ícono personalizado:

```bash
pyinstaller --onefile --windowed --icon assets/icon.ico main.py
```

## Estado actual

Versión: **v0.1**

Base funcional:

* Interfaz operativa.
* Motor de autoclick funcional.
* Hotkeys funcionando.
* Proyecto preparado para seguir creciendo.

Para conservar los cambios hay que ejecutar
pyinstaller --onefile --windowed main.py
