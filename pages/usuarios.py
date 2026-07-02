from dash import html, dcc
import dash_bootstrap_components as dbc

from components.sidebar import sidebar
from components.navbar import navbar

from utils.usuarios_data import cargar_usuarios



# ==========================================================
# TABLA DE USUARIOS
# ==========================================================

def tabla_usuarios():

    df = cargar_usuarios()


    filas = []


    for _, usuario in df.iterrows():

        filas.append(

            html.Tr(

                [

                    html.Td(
                        usuario["ID"]
                    ),

                    html.Td(
                        usuario["Usuario"]
                    ),

                    html.Td(
                        usuario["Nombre"]
                    ),

                    html.Td(
                        usuario["Rol"]
                    ),

                    html.Td(
                        usuario["Estado"]
                    ),

                    html.Td(

                        [

                            dbc.Button(

                                html.I(
                                    className="bi bi-pencil-fill"
                                ),

                                color="warning",

                                size="sm",

                                className="me-2",

                                id={

                                    "type":"editar-usuario",

                                    "id":int(usuario["ID"])

                                }

                            ),


                            dbc.Button(

                                html.I(
                                    className="bi bi-trash-fill"
                                ),

                                color="danger",

                                size="sm",

                                id={

                                    "type":"eliminar-usuario",

                                    "id":int(usuario["ID"])

                                }

                            )

                        ]

                    )

                ]

            )

        )


    return dbc.Table(

        [

            html.Thead(

                html.Tr(

                    [

                        html.Th("ID"),

                        html.Th("Usuario"),

                        html.Th("Nombre"),

                        html.Th("Rol"),

                        html.Th("Estado"),

                        html.Th("Acciones")

                    ]

                )

            ),


            html.Tbody(

                filas

            )

        ],

        bordered=True,

        hover=True,

        responsive=True,

        className="usuarios-table"

    )



# ==========================================================
# PAGINA USUARIOS
# ==========================================================


usuarios_layout = html.Div(

    className="dashboard-page",

    children=[


        # permite refrescar tabla después

        dcc.Store(

            id="actualizar-usuarios",

            data=0

        ),



        # SIDEBAR

        sidebar(),



        html.Div(

            className="main-content",

            children=[


                navbar(),



                dbc.Container(

                    [

                        html.Br(),



                        html.H2(

                            [

                                html.I(

                                    className="bi bi-people-fill me-3"

                                ),

                                "Gestión de Usuarios"

                            ],

                            className="dashboard-title"

                        ),



                        html.P(

                            "Administración de usuarios del sistema HIDRODATA.",

                            className="dashboard-subtitle"

                        ),



                        html.Hr(),



                        dbc.Button(

                            [

                                html.I(

                                    className="bi bi-person-plus-fill me-2"

                                ),

                                "Nuevo Usuario"

                            ],

                            id="btn-nuevo-usuario",

                            color="success",

                            size="lg",

                            className="mb-4"

                        ),




                        dbc.Card(

                            dbc.CardBody(

                                [

                                    html.Div(

                                        id="tabla-usuarios",

                                        children=tabla_usuarios()

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