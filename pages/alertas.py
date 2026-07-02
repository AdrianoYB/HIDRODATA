from dash import html
import dash_bootstrap_components as dbc

from components.sidebar import sidebar
from components.navbar import navbar
from components.alerts import crear_alertas

from utils.data_loader import ultimo_registro



def alertas_layout():

    dato = ultimo_registro()


    estado = dato["EstadoSistema"]


    if str(estado).lower() == "activo":

        color_estado = "success"
        icono_estado = "bi bi-check-circle-fill"
        mensaje_estado = "Sistema funcionando correctamente"


    else:

        color_estado = "danger"
        icono_estado = "bi bi-x-circle-fill"
        mensaje_estado = "Sistema detenido o requiere revisión"



    return html.Div(

        className="dashboard-page",

        children=[


            sidebar(),



            html.Div(

                className="main-content",

                children=[



                    navbar(),




                    dbc.Container(

                        [

                            html.Br(),




                            html.H2(

                                "🚨 Alertas Inteligentes",

                                className="dashboard-title"

                            ),




                            html.P(

                                "Monitoreo automático del estado del sistema hidráulico según las lecturas de sensores.",

                                className="dashboard-subtitle"

                            ),




                            html.Hr(),




                            # =====================================
                            # ESTADO GENERAL
                            # =====================================


                            dbc.Card(

                                dbc.CardBody(

                                    [

                                        html.Div(

                                            [

                                                html.I(

                                                    className=icono_estado,

                                                    style={

                                                        "fontSize": "45px"

                                                    }

                                                ),



                                                html.Div(

                                                    [

                                                        html.H4(

                                                            "Estado General"

                                                        ),


                                                        html.H5(

                                                            mensaje_estado

                                                        )

                                                    ]

                                                )

                                            ],

                                            className="d-flex gap-4 align-items-center"

                                        )

                                    ]

                                ),

                                color=color_estado,

                                inverse=True,

                                className="shadow"

                            ),




                            html.Br(),




                            # =====================================
                            # ALERTAS DETECTADAS
                            # =====================================


                            dbc.Card(

                                dbc.CardBody(

                                    [

                                        html.H4(

                                            "🚨 Análisis del Sistema",

                                            className="mb-3"

                                        ),



                                        html.P(

                                            "Las siguientes condiciones fueron evaluadas automáticamente:",

                                            className="text-muted"

                                        ),



                                        crear_alertas()

                                    ]

                                ),

                                className="graph-card"

                            ),




                            html.Br(),




                            # =====================================
                            # REFERENCIA
                            # =====================================


                            dbc.Card(

                                dbc.CardBody(

                                    [

                                        html.H4(

                                            "ℹ️ Criterios de Evaluación",

                                            className="mb-3"

                                        ),



                                        dbc.ListGroup(

                                            [

                                                dbc.ListGroupItem(
                                                    "💧 Humedad baja: posible necesidad de riego."
                                                ),

                                                dbc.ListGroupItem(
                                                    "🌡 Temperatura elevada: riesgo para el cultivo."
                                                ),

                                                dbc.ListGroupItem(
                                                    "🚰 Tanque bajo: revisar suministro de agua."
                                                ),

                                                dbc.ListGroupItem(
                                                    "⚡ Bomba apagada: verificar funcionamiento."
                                                ),

                                                dbc.ListGroupItem(
                                                    "⚙️ Estado del sistema: supervisión general."
                                                )

                                            ]

                                        )

                                    ]

                                ),

                                className="graph-card"

                            )


                        ],

                        fluid=True

                    )

                ]

            )

        ]

    )