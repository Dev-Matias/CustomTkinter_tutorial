#!/bin/bash

# Asigna el argumento a una variable
directorio="venv/bin"

# Verifica que el directorio exista
if [ ! -d "$directorio" ]; then
    echo "El directorio $directorio no existe."
    exit 1
fi

# Cambia al directorio especificado
cd "$directorio" || exit

# Busca archivos que puedan ser "sourceados" (por ejemplo, archivos .sh, .bash, etc.)
# Aquí asumimos que el archivo se llama 'script.sh'
archivo="activate"

# Verifica que el archivo exista
if [ ! -f "$archivo" ]; then
    echo "El archivo $archivo no existe en el directorio $directorio."
    exit 1
fi

# Ejecuta el source del archivo
source "$archivo"
