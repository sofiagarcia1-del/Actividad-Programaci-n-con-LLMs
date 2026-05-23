def clasificar_envios(df):
    import pandas as pd, numpy as np
    # Eliminar duplicados y nulos
    df_limpio = df.drop_duplicates().dropna().reset_index(drop=True)
    # Definir condiciones (orden importa)
    condiciones = [
        (df_limpio["dias_transito"] >= 10) | (df_limpio["manipulaciones"] >= 8),
        (df_limpio["dias_transito"] >= 6)  | (df_limpio["temperatura_almacenamiento"] >= 30),
    ]
    categorias = ["retraso_critico", "en_riesgo"]
    df_limpio["estado_envio"] = np.select(condiciones, categorias, default="en_tiempo")
    return df_limpio.sort_values("dias_transito").reset_index(drop=True)
