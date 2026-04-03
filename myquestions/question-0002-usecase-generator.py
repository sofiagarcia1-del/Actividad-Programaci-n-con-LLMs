import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_detectar_solapamientos():
    contextos = {
        "quirofanos":  ("quirofano", "cirugia"),
        "salas_conf":  ("sala", "reunion"),
        "vehiculos":   ("vehiculo", "ruta"),
        "servidores":  ("servidor", "tarea"),
    }
    nombre, (entidad_label, evento_label) = random.choice(list(contextos.items()))
    n_entidades = random.randint(3, 7)
    rows = []
    base = pd.Timestamp("2024-06-01 08:00")

    for eid in range(1, n_entidades + 1):
        n_eventos = random.randint(3, 7)
        cursor = base
        for _ in range(n_eventos):
            dur   = random.randint(30, 180)
            gap   = random.randint(-30, 90)   # gap negativo → solapamiento
            fin   = cursor + pd.Timedelta(minutes=dur)
            rows.append({
                "entidad_id": f"{entidad_label}_{eid:02d}",
                "inicio":     cursor,
                "fin":        fin,
            })
            cursor = fin + pd.Timedelta(minutes=gap)

    df = pd.DataFrame(rows).sample(frac=1).reset_index(drop=True)
    print(f"Contexto: '{nombre}' | Entidades: {n_entidades} | Intervalos: {len(df)}")
    print(df.head(8).to_string(index=False))
    return df
