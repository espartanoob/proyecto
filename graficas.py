import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def graficar_airbnb(ruta_csv):
    carpeta = "graficas_proyecto_final"

    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        print(f"📂 Carpeta '{carpeta}' creada para guardar gráficas.")
    else:
        print(f"📂 Carpeta '{carpeta}' ya existe. Las gráficas se actualizarán.")

    df = pd.read_csv(ruta_csv)

    # Histograma de log_price
    if 'log_price' in df.columns:
        plt.figure(figsize=(8,6))
        sns.histplot(df['log_price'], bins=50, kde=True)
        plt.title("Distribución de log(precio) de Airbnb")
        plt.xlabel("log(precio por noche)")
        plt.ylabel("Frecuencia")
        plt.savefig(os.path.join(carpeta, "histograma_logprecios.png"))
        plt.close()

    # Histograma de noches mínimas
    if 'minimum_nights' in df.columns:
        plt.figure(figsize=(8,6))
        sns.histplot(df['minimum_nights'], bins=50, kde=False)
        plt.title("Distribución de noches mínimas")
        plt.xlabel("Noches mínimas")
        plt.ylabel("Frecuencia")
        plt.savefig(os.path.join(carpeta, "histograma_noches.png"))
        plt.close()

    # Conteo por vecindario
    if 'neighbourhood' in df.columns:
        plt.figure(figsize=(10,6))
        sns.countplot(y=df['neighbourhood'], order=df['neighbourhood'].value_counts().index[:20])
        plt.title("Top 20 vecindarios con más listings")
        plt.savefig(os.path.join(carpeta, "conteo_vecindarios.png"))
        plt.close()

    # Boxplot de log_price por tipo de habitación
    if 'room_type' in df.columns and 'log_price' in df.columns:
        plt.figure(figsize=(8,6))
        sns.boxplot(x='room_type', y='log_price', data=df)
        plt.title("Distribución de log(precio) por tipo de habitación")
        plt.savefig(os.path.join(carpeta, "boxplot_roomtype.png"))
        plt.close()

    # Heatmap de correlación
    variables_numericas = df.select_dtypes(include=['int64','float64'])
    if not variables_numericas.empty:
        plt.figure(figsize=(10,8))
        sns.heatmap(variables_numericas.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Mapa de correlación entre variables numéricas")
        plt.savefig(os.path.join(carpeta, "heatmap_correlacion.png"))
        plt.close()

    # Pairplot de variables clave
    columnas_clave = [c for c in ['log_price','accommodates','bathrooms','bedrooms','beds'] if c in df.columns]
    if len(columnas_clave) > 1:
        sns.pairplot(df[columnas_clave], diag_kind="kde")
        plt.savefig(os.path.join(carpeta, "pairplot_variables.png"))
        plt.close()

    # Histograma de número de reseñas
    if 'number_of_reviews' in df.columns:
        plt.figure(figsize=(8,6))
        sns.histplot(df['number_of_reviews'], bins=50, kde=False)
        plt.title("Distribución del número de reseñas")
        plt.xlabel("Número de reseñas")
        plt.ylabel("Frecuencia")
        plt.savefig(os.path.join(carpeta, "histograma_reviews.png"))
        plt.close()

    # Histograma de calificaciones
    if 'review_scores_rating' in df.columns:
        plt.figure(figsize=(8,6))
        sns.histplot(df['review_scores_rating'], bins=20, kde=True)
        plt.title("Distribución de calificaciones de reseñas")
        plt.xlabel("Calificación")
        plt.ylabel("Frecuencia")
        plt.savefig(os.path.join(carpeta, "histograma_calificaciones.png"))
        plt.close()

    print(f"✅ Todas las gráficas guardadas en formato PNG dentro de '{carpeta}'.")

