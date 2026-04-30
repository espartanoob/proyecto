#!/usr/bin/env bash
echo "Iniciando instalación y configuración..."

sudo apt install zip unzip python3-venv python3-pip python3-full -y

BASE="$PWD"

# Ruta del entorno virtual
RUTA_ENV="$BASE/env"

# Manejo del entorno virtual
if [ -d "$RUTA_ENV" ]; then
    echo "📂 Activando entorno existente en $RUTA_ENV..."
    source "$RUTA_ENV/bin/activate"
    pip install --upgrade pip --break-system-packages
    pip install pandas numpy seaborn scikit-learn matplotlib --break-system-packages
else
    echo "📂 Creando entorno en $RUTA_ENV..."
    python3 -m venv "$RUTA_ENV"
    source "$RUTA_ENV/bin/activate"
    pip install --upgrade pip --break-system-packages
    pip install pandas numpy seaborn scikit-learn matplotlib --break-system-packages
fi


if [ ! -f train.csv ]; then
    unzip train.csv.zip;
fi

# Ejecutar main.py automáticamente
echo "🚀 Ejecutando main.py..."
cd "$BASE"
python3 main.py
