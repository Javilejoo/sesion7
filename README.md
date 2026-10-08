# sesion7
Poner en práctica Git, las pruebas unitarias y la integración continua con GitHub Actions mediante la construcción de un proyecto pequeño. 

## Requisitos

- Python 3.10 o superior
- Git

## Configuración del entorno (paso a paso)

### 1. Clonar el repositorio

```bash
git clone https://github.com/Javilejoo/sesion7.git
cd sesion7
```

### 2. Crear el entorno virtual

```bash
python3 -m venv .venv
```

> La carpeta `.venv/` está incluida en `.gitignore`, por lo que no se sube al repositorio. Cada developer debe crear la suya.

### 3. Activar el entorno virtual

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Al activarlo verás `(.venv)` al inicio de la línea de la terminal.

### 4. Instalar las dependencias (pytest)

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Verificar la instalación

```bash
pytest --version
```

Debería mostrar `pytest 9.1.1`.

### 6. Ejecutar las pruebas

```bash
pytest
```

### Desactivar el entorno

```bash
deactivate
```
