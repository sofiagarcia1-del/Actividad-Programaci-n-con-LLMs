def detectar_fuera_de_limites(df_medidas, lcl, ucl):
    fuera = df_medidas[
        (df_medidas["medida_mm"] < lcl) | (df_medidas["medida_mm"] > ucl)
    ]["id_lote"].tolist()
    return {
        "total_lotes": len(df_medidas),
        "fuera_de_control": fuera
    }
