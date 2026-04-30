import pandas as pd
import numpy as np

def verificar_dataset(df, nombre="Dataset"):
    print(f"\n🔎 Verificación de {nombre}")
    print("Dimensiones:", df.shape)
    print("Columnas:", df.columns.tolist())
    print("\nValores nulos por columna:")
    print(df.isnull().sum())
    print("\nDuplicados:", df.duplicated().sum())
    print("\nTipos de datos:")
    print(df.dtypes)
    print("\nEstadísticas descriptivas:")
    print(df.describe(include='all'))
    print("\nValores máximos y mínimos por columna numérica:")
    print(df.describe().loc[['min','max']])

def limpiar_airbnb(df):
    df = df.copy()
    df = df.drop_duplicates()

    # Conversión numérica segura
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Filtrar outliers en log_price
    if 'log_price' in df.columns:
        df = df[(df['log_price'] > 0) & (df['log_price'] < 10)]

    # Imputación avanzada
    for col in df.columns:
        if df[col].dtype in [np.float64, np.int64]:
            if col in ['bathrooms','bedrooms','beds'] and 'property_type' in df.columns:
                df[col] = df.groupby('property_type')[col].transform(lambda x: x.fillna(x.median()))
            elif col == 'review_scores_rating' and 'city' in df.columns:
                df[col] = df.groupby('city')[col].transform(lambda x: x.fillna(x.mean()))
            else:
                df[col] = df[col].fillna(df[col].median())
        elif df[col].dtype == object:
            if df[col].isnull().sum() > 0:
                moda = df[col].mode()[0] if not df[col].mode().empty else "Unknown"
                df[col] = df[col].fillna(moda)
        elif "datetime" in str(df[col].dtype):
            df[col] = pd.to_datetime(df[col], errors="coerce")
            df[col] = df[col].fillna(pd.NaT)

    # Manejo específico
    if 'neighbourhood' in df.columns:
        df['neighbourhood'] = df['neighbourhood'].fillna('Unknown')

    for col in ['first_review','last_review']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    for col in ['description','thumbnail_url']:
        if col in df.columns:
            df[col] = df[col].fillna('Missing')

    # Normalización automática
    for col in df.select_dtypes(include=[np.number]).columns:
        max_val = df[col].max()
        if max_val > 0:
            df[col+"_norm"] = df[col] / max_val

    # Normalización explícita de columnas críticas
    if 'number_of_reviews' in df.columns:
        df['reviews_norm'] = df['number_of_reviews'] / df['number_of_reviews'].max()
    if 'review_scores_rating' in df.columns:
        df['rating_norm'] = df['review_scores_rating'] / df['review_scores_rating'].max()

    # Eliminar nulos residuales
    df = df.dropna()

    verificar_dataset(df, nombre="Airbnb (sin nulos)")
    return df
