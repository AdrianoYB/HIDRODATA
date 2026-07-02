import pandas as pd
from datetime import datetime, timedelta


ARCHIVO = "data/HIDRODATA_Datos_Demo.xlsx"



# =====================================================
# CARGAR TODO EL HISTORIAL
# =====================================================

def cargar_datos():

    df = pd.read_excel(
        ARCHIVO
    )

    df["FechaHora"] = pd.to_datetime(
        df["FechaHora"]
    )

    return df



# =====================================================
# FILTRO POR PERIODO
# =====================================================

def cargar_datos_periodo(periodo="todo"):


    df = cargar_datos()


    if periodo == "todo":

        return df



    ahora = df["FechaHora"].max()



    if periodo == "24h":

        inicio = ahora - timedelta(
            hours=24
        )


    elif periodo == "7d":

        inicio = ahora - timedelta(
            days=7
        )


    elif periodo == "30d":

        inicio = ahora - timedelta(
            days=30
        )


    else:

        return df



    df_filtrado = df[
        df["FechaHora"] >= inicio
    ]



    return df_filtrado




# =====================================================
# ULTIMO REGISTRO
# =====================================================

def ultimo_registro():

    df = cargar_datos()

    return df.iloc[-1]