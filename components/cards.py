from dash import html
import dash_bootstrap_components as dbc

from utils.data_loader import ultimo_registro


def crear_kpis():

    dato = ultimo_registro()

    humedad = dato["HumedadSuelo_%"]
    temperatura = dato["Temperatura_C"]
    tanque = dato["NivelTanque_%"]
    estado = dato["EstadoSistema"]

    # ==========================
    # COLORES DINÁMICOS
    # ==========================

    # Humedad
    if humedad >= 60:
        color_humedad = "success"
        icono_humedad = "bi bi-droplet-fill"

    elif humedad >= 40:
        color_humedad = "warning"
        icono_humedad = "bi bi-droplet-half"

    else:
        color_humedad = "danger"
        icono_humedad = "bi bi-exclamation-triangle-fill"

    # Temperatura
    if temperatura <= 30:
        color_temperatura = "info"
        icono_temperatura = "bi bi-thermometer-half"

    elif temperatura <= 35:
        color_temperatura = "warning"
        icono_temperatura = "bi bi-thermometer-sun"

    else:
        color_temperatura = "danger"
        icono_temperatura = "bi bi-thermometer-high"

    # Tanque
    if tanque >= 60:
        color_tanque = "primary"
        icono_tanque = "bi bi-water"

    elif tanque >= 30:
        color_tanque = "warning"
        icono_tanque = "bi bi-water"

    else:
        color_tanque = "danger"
        icono_tanque = "bi bi-exclamation-diamond-fill"

    # Estado
    if estado.lower() == "activo":
        color_estado = "success"
        icono_estado = "bi bi-cpu-fill"

    else:
        color_estado = "secondary"
        icono_estado = "bi bi-cpu"

    return dbc.Row(

        [

            # ==========================
            # HUMEDAD
            # ==========================

            dbc.Col(

                dbc.Card(

                    dbc.CardBody(

                        [

                            html.Div(

                                [

                                    html.I(

                                        className=icono_humedad,

                                        style={
                                            "fontSize": "32px",
                                            "color": "white"
                                        }

                                    ),

                                    html.Div(

                                        [

                                            html.H6(

                                                "Humedad",

                                                style={"color": "white"}

                                            ),

                                            html.H3(

                                                f"{humedad} %",

                                                style={
                                                    "color": "white",
                                                    "fontWeight": "bold"
                                                }

                                            )

                                        ]

                                    )

                                ],

                                className="d-flex justify-content-between align-items-center"

                            )

                        ]

                    ),

                    color=color_humedad,

                    inverse=True,

                    className="shadow"

                ),

                lg=3

            ),

            # ==========================
            # TEMPERATURA
            # ==========================

            dbc.Col(

                dbc.Card(

                    dbc.CardBody(

                        [

                            html.Div(

                                [

                                    html.I(

                                        className=icono_temperatura,

                                        style={
                                            "fontSize": "32px",
                                            "color": "white"
                                        }

                                    ),

                                    html.Div(

                                        [

                                            html.H6(

                                                "Temperatura",

                                                style={"color": "white"}

                                            ),

                                            html.H3(

                                                f"{temperatura} °C",

                                                style={
                                                    "color": "white",
                                                    "fontWeight": "bold"
                                                }

                                            )

                                        ]

                                    )

                                ],

                                className="d-flex justify-content-between align-items-center"

                            )

                        ]

                    ),

                    color=color_temperatura,

                    inverse=True,

                    className="shadow"

                ),

                lg=3

            ),

            # ==========================
            # TANQUE
            # ==========================

            dbc.Col(

                dbc.Card(

                    dbc.CardBody(

                        [

                            html.Div(

                                [

                                    html.I(

                                        className=icono_tanque,

                                        style={
                                            "fontSize": "32px",
                                            "color": "white"
                                        }

                                    ),

                                    html.Div(

                                        [

                                            html.H6(

                                                "Nivel Tanque",

                                                style={"color": "white"}

                                            ),

                                            html.H3(

                                                f"{tanque} %",

                                                style={
                                                    "color": "white",
                                                    "fontWeight": "bold"
                                                }

                                            )

                                        ]

                                    )

                                ],

                                className="d-flex justify-content-between align-items-center"

                            )

                        ]

                    ),

                    color=color_tanque,

                    inverse=True,

                    className="shadow"

                ),

                lg=3

            ),

            # ==========================
            # ESTADO
            # ==========================

            dbc.Col(

                dbc.Card(

                    dbc.CardBody(

                        [

                            html.Div(

                                [

                                    html.I(

                                        className=icono_estado,

                                        style={
                                            "fontSize": "32px",
                                            "color": "white"
                                        }

                                    ),

                                    html.Div(

                                        [

                                            html.H6(

                                                "Estado",

                                                style={"color": "white"}

                                            ),

                                            html.H3(

                                                estado,

                                                style={
                                                    "color": "white",
                                                    "fontWeight": "bold"
                                                }

                                            )

                                        ]

                                    )

                                ],

                                className="d-flex justify-content-between align-items-center"

                            )

                        ]

                    ),

                    color=color_estado,

                    inverse=True,

                    className="shadow"

                ),

                lg=3

            )

        ],

        className="g-4"

    )