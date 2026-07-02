from dash import html
import dash_bootstrap_components as dbc

from utils.data_loader import cargar_datos_periodo


def crear_estadisticas(periodo="todo"):

    df = cargar_datos_periodo(periodo)

    # ==========================================
    # CALCULOS
    # ==========================================

    humedad_prom = round(
        df["HumedadSuelo_%"].mean(),
        1
    )

    humedad_min = round(
        df["HumedadSuelo_%"].min(),
        1
    )


    temperatura_prom = round(
        df["Temperatura_C"].mean(),
        1
    )

    temperatura_max = round(
        df["Temperatura_C"].max(),
        1
    )


    humedad_amb = round(
        df["HumedadAmb_%"].mean(),
        1
    )


    tanque_prom = round(
        df["NivelTanque_%"].mean(),
        1
    )


    consumo_total = round(
        df["ConsumoAgua_L"].sum(),
        1
    )


    consumo_prom = round(
        df["ConsumoAgua_L"].mean(),
        1
    )


    caudal_prom = round(
        df["Caudal_Lmin"].mean(),
        1
    )


    total_registros = len(df)



    # ==========================================
    # TARJETAS
    # ==========================================

    tarjetas = [


        (
            "bi bi-droplet-fill",
            "Humedad Promedio",
            f"{humedad_prom} %",
            "primary"
        ),


        (
            "bi bi-exclamation-circle",
            "Humedad Mínima",
            f"{humedad_min} %",
            "warning"
        ),


        (
            "bi bi-thermometer-half",
            "Temperatura Media",
            f"{temperatura_prom} °C",
            "danger"
        ),


        (
            "bi bi-thermometer-high",
            "Temperatura Máxima",
            f"{temperatura_max} °C",
            "dark"
        ),


        (
            "bi bi-cloud",
            "Humedad Ambiental",
            f"{humedad_amb} %",
            "info"
        ),


        (
            "bi bi-water",
            "Nivel Tanque",
            f"{tanque_prom} %",
            "success"
        ),


        (
            "bi bi-droplet",
            "Consumo Total",
            f"{consumo_total} L",
            "primary"
        ),


        (
            "bi bi-speedometer",
            "Caudal Medio",
            f"{caudal_prom} L/min",
            "secondary"
        ),


        (
            "bi bi-bar-chart",
            "Consumo Promedio",
            f"{consumo_prom} L",
            "warning"
        ),


        (
            "bi bi-database-fill",
            "Registros",
            total_registros,
            "dark"
        )

    ]



    # ==========================================
    # GENERAR COMPONENTES
    # ==========================================

    componentes = []


    for icono, titulo, valor, color in tarjetas:


        componentes.append(

            dbc.Col(

                dbc.Card(

                    dbc.CardBody(

                        [

                            html.I(

                                className=icono,

                                style={

                                    "fontSize": "30px"

                                }

                            ),


                            html.H6(

                                titulo,

                                className="mt-3"

                            ),


                            html.H3(

                                valor,

                                className="fw-bold"

                            )

                        ]

                    ),

                    color=color,

                    inverse=True,

                    className="shadow"

                ),

                lg=3,

                md=6

            )

        )



    return dbc.Row(

        componentes,

        className="g-4"

    )