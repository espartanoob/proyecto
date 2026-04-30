import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

def entrenar_modelo(ruta_csv="airbnb_limpio.csv"):
    df = pd.read_csv(ruta_csv)

    # Variables predictoras disponibles
    posibles = [
        'accommodates_norm',
        'bathrooms_norm',
        'bedrooms_norm',
        'beds_norm',
        'reviews_norm',
        'rating_norm'
    ]
    X = df[[col for col in posibles if col in df.columns]]

    if 'log_price' not in df.columns:
        raise KeyError("La columna 'log_price' no está en el dataset limpio.")
    y = df['log_price']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    print("\n📊 Evaluación del modelo Airbnb:")
    print("R²:", r2)
    print("MSE:", mse)

    return model, y_test, y_pred, r2, mse
