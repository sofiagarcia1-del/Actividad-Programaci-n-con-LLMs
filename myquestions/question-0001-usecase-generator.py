import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_matriz_transicion_estados():
    escenarios = {
        "semaforo":    ["rojo", "verde", "amarillo"],
        "pedido":      ["recibido", "procesando", "enviado", "entregado", "cancelado"],
        "maquina":     ["idle", "calentando", "activa", "enfriando", "fallo"],
        "ticket":      ["abierto", "en_progreso", "en_espera", "resuelto", "cerrado"],
    }
    nombre, estados = random.choice(list(escenarios.items()))
    n_procesos = random.randint(4, 10)
    n_eventos   = random.randint(20, 50)

    rows = []
    for pid in range(n_procesos):
        n = random.randint(3, n_eventos // n_procesos + 2)
        t = pd.Timestamp("2024-01-01") + pd.to_timedelta(
            sorted(random.sample(range(200), n)), unit="h"
        )
        s = [random.choice(estados) for _ in range(n)]
        rows.append(pd.DataFrame({
            "id_proceso": pid,
            "timestamp":  t,
            "estado":     s,
        }))

    df = pd.concat(rows, ignore_index=True)
    print(f"Escenario: '{nombre}' | Procesos: {n_procesos} | Eventos totales: {len(df)}")
    print(f"Estados posibles: {estados}")
    print(df.head(8).to_string(index=False))
    return df
