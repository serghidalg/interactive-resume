#!/bin/bash


#!/bin/bash

# Verificar si python3 está instalado
if command -v python3 &>/dev/null; then
    python_executable="python3"
elif command -v python &>/dev/null; then
    python_executable="python"
else
    echo "Python 3 no está instalado."
    exit 1
fi

# Crear el entorno virtual
$python_executable -m venv venv

# Activar el entorno virtual
source venv/bin/activate

# Instalar los requisitos
pip install -r requirements.txt

# Ejecutar setup_variables.py
$python_executable setup_variables.py

