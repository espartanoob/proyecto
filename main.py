import os
import pandas as pd
from limpieza import limpiar_airbnb
from graficas import graficar_airbnb
from prediccion import entrenar_modelo
from resultados import mostrar_resultados

def main():
    # Ruta Descargas en Windows vista desde WSL
    # base_descargas = "/mnt/c/Users/Mendo/Downloads"

    # 1. Cargar dataset desde Descargas
    base_descargas = "./"
    ruta = os.path.join(base_descargas, "train.csv")
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encontró train.csv en {ruta}. Verifica que esté en Descargas de Windows.")

    print(f"📥 Cargando dataset desde: {ruta}")
    airbnb = pd.read_csv(ruta)
    print(f"✅ Dataset cargado con {airbnb.shape[0]} filas y {airbnb.shape[1]} columnas")

    # 2. Limpieza
    print("🧹 Iniciando limpieza...")
    base_limpia = limpiar_airbnb(airbnb)

    # 3. Guardar dataset limpio en Descargas
    salida = os.path.join(base_descargas, "airbnb_limpio.csv")
    base_limpia.to_csv(salida, index=False, mode="w")
    print(f"✅ Archivo limpio guardado en: {salida}")

    # 4. Graficar usando el archivo limpio
    print("📊 Generando gráficas...")
    graficar_airbnb(salida)

    # 5. Entrenar modelo usando el archivo limpio
    print("🤖 Entrenando modelo...")
    modelo, y_test, y_pred, r2, mse = entrenar_modelo(salida)

    # 6. Mostrar resultados
    print("📈 Resultados del modelo:")
    mostrar_resultados(r2, mse, y_test, y_pred)

if __name__ == "__main__":
    main()
