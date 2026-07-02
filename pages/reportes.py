from dash import html, dcc
import dash_bootstrap_components as dbc


from components.sidebar import sidebar
from components.navbar import navbar
from components.table import tabla_datos
from components.statistics import crear_estadisticas



reportes_layout = html.Div(

    className="dashboard-page",

    children=[


        # =====================================
        # DESCARGAS
        # =====================================

        dcc.Download(
            id="download-excel"
        ),

        dcc.Download(
            id="download-pdf"
        ),



        # =====================================
        # SIDEBAR
        # =====================================

        sidebar(),



        # =====================================
        # CONTENIDO
        # =====================================

        html.Div(

            className="main-content",

            children=[


                navbar(),



                dbc.Container(

                    [

                        html.Br(),



                        html.H2(

                            "📄 Reportes",

                            className="dashboard-title"

                        ),



                        html.P(

                            "Consulta, análisis y exportación del historial registrado por HIDRODATA.",

                            className="dashboard-subtitle"

                        ),



                        html.Hr(),




                        # =====================================
                        # SELECTOR DE PERIODO
                        # =====================================


                        dbc.Card(

                            dbc.CardBody(

                                [

                                    html.H5(

                                        "📅 Periodo de análisis",

                                        className="mb-3"

                                    ),



                                    dcc.Dropdown(

                                        id="periodo-reporte",

                                        options=[


                                            {
                                                "label": "Últimas 24 horas",
                                                "value": "24h"
                                            },


                                            {
                                                "label": "Últimos 7 días",
                                                "value": "7d"
                                            },


                                            {
                                                "label": "Últimos 30 días",
                                                "value": "30d"
                                            },


                                            {
                                                "label": "Todo el histórico",
                                                "value": "todo"
                                            }

                                        ],


                                        value="todo",


                                        clearable=False

                                    )

                                ]

                            ),

                            className="graph-card"

                        ),



                        html.Br(),




                        # =====================================
                        # BOTONES EXPORTACION
                        # =====================================


                        dbc.Row(

                            [

                                dbc.Col(

                                    dbc.Button(

                                        [

                                            html.I(

                                                className="bi bi-file-earmark-excel-fill me-2"

                                            ),

                                            "Exportar Excel"

                                        ],


                                        id="btn-exportar-excel",

                                        color="success",

                                        size="lg",

                                        className="w-100"

                                    ),

                                    md=3

                                ),




                                dbc.Col(

                                    dbc.Button(

                                        [

                                            html.I(

                                                className="bi bi-file-earmark-pdf-fill me-2"

                                            ),

                                            "Exportar PDF"

                                        ],


                                        id="btn-exportar-pdf",

                                        color="danger",

                                        size="lg",

                                        className="w-100"

                                    ),

                                    md=3

                                )


                            ],

                            className="g-3 mb-4"

                        ),





                        # =====================================
                        # ESTADISTICAS DINAMICAS
                        # =====================================


                        dbc.Card(

                            dbc.CardBody(

                                [

                                    html.H4(

                                        "📊 Resumen del periodo",

                                        className="mb-3"

                                    ),



                                    html.P(

                                        "Indicadores calculados según el periodo seleccionado.",

                                        className="text-muted"

                                    ),



                                    html.Div(

                                        id="estadisticas-reporte",

                                        children=crear_estadisticas("todo")

                                    )


                                ]

                            ),

                            className="graph-card"

                        ),




                        html.Br(),




                        # =====================================
                        # GRAFICOS REPORTE
                        # =====================================


                        dbc.Card(

                            dbc.CardBody(

                                [

                                    html.H4(

                                        "📈 Evolución del periodo",

                                        className="mb-3"

                                    ),



                                    html.Div(

                                        id="graficos-reporte"

                                    )

                                ]

                            ),

                            className="graph-card"

                        ),





                        html.Br(),




                        # =====================================
                        # TABLA DINAMICA
                        # =====================================


                        dbc.Card(

                            dbc.CardBody(

                                [

                                    html.H4(

                                        "📋 Historial de Mediciones",

                                        className="mb-3"

                                    ),



                                    html.P(

                                        "Registros correspondientes al periodo seleccionado.",

                                        className="text-muted"

                                    ),



                                    html.Div(

                                        id="tabla-reporte",

                                        children=tabla_datos()

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