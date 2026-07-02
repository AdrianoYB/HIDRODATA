from dash import html, dcc
import dash_bootstrap_components as dbc


# ==========================================================
# COMPONENTES
# ==========================================================

from components.sidebar import sidebar
from components.navbar import navbar
from components.cards import crear_kpis
from components.table import tabla_datos
from components.alerts import crear_alertas
from components.statistics import crear_estadisticas


from components.graphs import (
    grafico_humedad,
    grafico_temperatura,
    grafico_consumo,
    grafico_tanque
)



# ==========================================================
# DASHBOARD
# ==========================================================

dashboard_layout = html.Div(

    className="dashboard-page",

    children=[


        # ==================================================
        # ACTUALIZACIÓN AUTOMÁTICA
        # ==================================================

        dcc.Interval(

            id="interval-update",

            interval=5000,

            n_intervals=0

        ),



        sidebar(),



        html.Div(

            className="main-content",

            children=[


                navbar(),



                dbc.Container(

                    [

                        html.Br(),


                        html.H2(

                            "Panel de Control",

                            className="dashboard-title"

                        ),



                        html.P(

                            "Monitoreo inteligente del sistema de riego en tiempo real.",

                            className="dashboard-subtitle"

                        ),



                        html.Hr(),



                        # ==================================================
                        # KPIS DINÁMICOS
                        # ==================================================

                        html.Div(

                            id="kpis-container",

                            children=crear_kpis()

                        ),



                        html.Br(),
                                                # ==================================================
                        # GRÁFICOS SUPERIORES DINÁMICOS
                        # ==================================================

                        dbc.Row(

                            [

                                dbc.Col(

                                    dbc.Card(

                                        dbc.CardBody(

                                            html.Div(

                                                id="grafico-humedad-container",

                                                children=grafico_humedad()

                                            )

                                        ),

                                        className="graph-card"

                                    ),

                                    lg=8

                                ),



                                dbc.Col(

                                    dbc.Card(

                                        dbc.CardBody(

                                            html.Div(

                                                id="grafico-tanque-container",

                                                children=grafico_tanque()

                                            )

                                        ),

                                        className="graph-card"

                                    ),

                                    lg=4

                                )

                            ],

                            className="g-4"

                        ),



                        html.Br(),



                        # ==================================================
                        # GRÁFICOS INFERIORES DINÁMICOS
                        # ==================================================

                        dbc.Row(

                            [

                                dbc.Col(

                                    dbc.Card(

                                        dbc.CardBody(

                                            html.Div(

                                                id="grafico-temperatura-container",

                                                children=grafico_temperatura()

                                            )

                                        ),

                                        className="graph-card"

                                    ),

                                    lg=6

                                ),



                                dbc.Col(

                                    dbc.Card(

                                        dbc.CardBody(

                                            html.Div(

                                                id="grafico-consumo-container",

                                                children=grafico_consumo()

                                            )

                                        ),

                                        className="graph-card"

                                    ),

                                    lg=6

                                )

                            ],

                            className="g-4"

                        ),



                        html.Br(),
                                                # ==================================================
                        # TABLA DINÁMICA
                        # ==================================================

                        dbc.Card(

                            dbc.CardBody(

                                [

                                    html.H4(

                                        "📋 Últimas Lecturas",

                                        className="mb-2"

                                    ),



                                    html.P(

                                        "Registro de las últimas mediciones captadas por los sensores.",

                                        style={

                                            "color": "#6c757d",

                                            "marginBottom": "20px"

                                        }

                                    ),



                                    html.Div(

                                        id="tabla-container",

                                        children=tabla_datos()

                                    )


                                ]

                            ),

                            className="graph-card"

                        ),



                        html.Br(),




                        # ==================================================
                        # ALERTAS DINÁMICAS
                        # ==================================================

                        dbc.Card(

                            dbc.CardBody(

                                [

                                    html.H4(

                                        "🚨 Alertas Inteligentes",

                                        className="mb-2"

                                    ),



                                    html.P(

                                        "Estado del sistema según las últimas mediciones.",

                                        style={

                                            "color": "#6c757d",

                                            "marginBottom": "20px"

                                        }

                                    ),



                                    html.Div(

                                        id="alertas-container",

                                        children=crear_alertas()

                                    )


                                ]

                            ),

                            className="graph-card"

                        ),



                        html.Br(),




                        # ==================================================
                        # ESTADÍSTICAS
                        # ==================================================

                        dbc.Card(

                            dbc.CardBody(

                                [

                                    html.H4(

                                        "📊 Estadísticas Generales",

                                        className="mb-2"

                                    ),



                                    html.P(

                                        "Indicadores calculados a partir del histórico de datos registrados.",

                                        style={

                                            "color": "#6c757d",

                                            "marginBottom": "20px"

                                        }

                                    ),



                                    crear_estadisticas()


                                ]

                            ),

                            className="graph-card"

                        ),



                        html.Br()




                    ],

                    fluid=True

                )

            ]

        )

    ]

)