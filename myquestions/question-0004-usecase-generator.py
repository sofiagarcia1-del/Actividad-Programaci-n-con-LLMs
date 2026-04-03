import numpy as np
import random
from sklearn.datasets import make_classification

def generar_caso_de_uso_calibrar_y_comparar():
    perfiles = {
        "diagnostico_medico":   dict(n_samples=400, n_features=10, n_informative=6,
                                     n_redundant=2, weights=[0.7, 0.3]),
        "deteccion_spam":       dict(n_samples=600, n_features=15, n_informative=8,
                                     n_redundant=4, weights=[0.8, 0.2]),
        "aprobacion_credito":   dict(n_samples=300, n_features=8,  n_informative=5,
                                     n_redundant=1, weights=[0.6, 0.4]),
        "fallo_equipo":         dict(n_samples=500, n_features=12, n_informative=4,
                                     n_redundant=5, weights=[0.85, 0.15]),
    }
    nombre, params = random.choice(list(perfiles.items()))
    seed = random.randint(0, 999)

    X, y = make_classification(
        random_state=seed,
        n_clusters_per_class=1,
        flip_y=random.uniform(0.02, 0.08),
        **{k: v for k, v in params.items() if k != "weights"},
    )
    # Aplicar desbalance aproximado
    print(f"Perfil: '{nombre}'")
    print(f"X shape: {X.shape} | Distribución de clases: "
          f"{dict(zip(*np.unique(y, return_counts=True)))}")
    return X, y
