import matplotlib.pyplot as plt
import pandas as pd

def mostrar_resultados(r2, mse, y_test, y_pred):
    print("\n📢 Comunicación de resultados del modelo Airbnb:")
    print(f"Coeficiente de determinación (R²): {r2:.4f}")
    print(f"Error cuadrático medio (MSE): {mse:.2f}")

    # Comparación de valores reales vs predichos
    comparison = pd.DataFrame({"Precio real": y_test, "Precio predicho": y_pred})
    print("\nComparación de precios reales vs predichos:")
    print(comparison.head())

    # Gráfico de dispersión
    plt.figure(figsize=(8,6))
    plt.scatter(y_test, y_pred, alpha=0.7, color="blue")
    plt.xlabel("Precios reales")
    plt.ylabel("Precios predichos")
    plt.title("Predicciones de precios Airbnb vs Valores reales")
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.savefig("resultados_prediccion.png", format="png")
    plt.close()

    print("\n✅ Resultados comunicados con métricas y gráfica guardada como 'resultados_prediccion.png'.")

