import pandas as pd

from dash import dcc

from utils.data_loader import cargar_datos


def exportar_excel():

    df = cargar_datos()

    return dcc.send_data_frame(

        df.to_excel,

        "Reporte_HIDRODATA.xlsx",

        sheet_name="Reporte",

        index=False

    )