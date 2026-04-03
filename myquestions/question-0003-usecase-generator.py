import numpy as np
import random
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

def generar_caso_de_uso_detectar_por_reconstruccion():
    escenarios = {
        "sensores_industriales": dict(n_features=12, n_informative=5, n_redundant=4),
        "señales_EEG":           dict(n_features=20, n_informative=6, n_redundant=8),
        "telemetria_satelite":   dict(n_features=15, n_informative=4, n_redundant=6),
        "logs_red":              dict(n_features=10, n_informative=3, n_redundant=4),
    }
    nombre, params = random.choice(list(escenarios.items()))
    n_train = random.choice([200, 300, 400])
    n_test  = random.choice([50, 80, 100])
    pct     = random.choice([90, 92, 95, 97])

    rng = np.random.default_rng(random.randint(0, 999))
    X_train = rng.standard_normal((n_train, params["n_features"]))
    # Inyectar anomalías en test: ~10% de filas con ruido extra
    X_test  = rng.standard_normal((n_test,  params["n_features"]))
    n_anom  = max(1, n_test // 10)
    idx_anom = rng.choice(n_test, n_anom, replace=False)
    X_test[idx_anom] += rng.standard_normal((n_anom, params["n_features"])) * 5

    print(f"Escenario: '{nombre}'")
    print(f"X_train: {X_train.shape} | X_test: {X_test.shape}")
    print(f"Percentil umbral: {pct} | Anomalías inyectadas en test: {n_anom} filas")
    return X_train, X_test, pct
