#!/usr/bin/env bash
echo "Iniciando instalación y configuración..."

# Verificación de versión de Ubuntu
UBUNTU_VERSION=$(grep VERSION_ID /etc/os-release | cut -d '"' -f2)

if [ "$UBUNTU_VERSION" != "24.04" ]; then
    echo "❌ Error: Este script solo puede ejecutarse en Ubuntu 24.04 (detectado $UBUNTU_VERSION)."
    exit 1
fi

# Actualizar paquetes e instalar dependencias necesarias
sudo apt-get update
sudo apt-get install -y zip unzip python3-venv python3-pip

# Carpeta base = directorio actual
BASE="$PWD"

# Ruta del entorno virtual
RUTA_ENV="$BASE/env"

# Manejo del entorno virtual
if [ -d "$RUTA_ENV" ]; then
    echo "📂 Activando entorno existente en $RUTA_ENV..."
    source "$RUTA_ENV/bin/activate"
    pip install --upgrade pip
    pip install pandas numpy seaborn scikit-learn matplotlib
else
    echo "📂 Creando entorno en $RUTA_ENV..."
    python3 -m venv "$RUTA_ENV"
    source "$RUTA_ENV/bin/activate"
    pip install --upgrade pip
    pip install pandas numpy seaborn scikit-learn matplotlib
fi

# Descomprimir dataset si existe el zip pero no el csv
if [ -f "$BASE/train.csv.zip" ] && [ ! -f "$BASE/train.csv" ]; then
    echo "📦 Descomprimiendo train.csv.zip..."
    unzip "$BASE/train.csv.zip" -d "$BASE"
fi

# Ejecutar main.py automáticamente
if [ -f "$BASE/main.py" ]; then
    echo "🚀 Ejecutando main.py..."
    python3 "$BASE/main.py"
else
    echo "⚠️ No se encontró main.py en $BASE"
fi
