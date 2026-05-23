import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture

def seleccionar_gmm_optimo(X, rango_componentes, random_state=42):
    # Estandarizar X
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Ajustar GMM para cada k y calcular BIC
    bic_por_k = {}
    modelos = {}
    for k in rango_componentes:
        gmm = GaussianMixture(n_components=k, random_state=random_state)
        gmm.fit(X_scaled)
        bic_por_k[k] = gmm.bic(X_scaled)
        modelos[k] = gmm

    # Seleccionar k con menor BIC; en empate el más pequeño
    mejor_k = min(bic_por_k, key=lambda k: (bic_por_k[k], k))
    mejor_bic = bic_por_k[mejor_k]

    # Predicciones con el modelo óptimo
    modelo_optimo = modelos[mejor_k]
    etiquetas = modelo_optimo.predict(X_scaled)
    probabilidades = modelo_optimo.predict_proba(X_scaled)

    return {
        "mejor_k":       mejor_k,
        "mejor_bic":     mejor_bic,
        "bic_por_k":     bic_por_k,
        "etiquetas":     etiquetas,
        "probabilidades": probabilidades,
    }
