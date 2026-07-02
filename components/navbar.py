from dash import html
import dash_bootstrap_components as dbc
from datetime import datetime


def navbar():

    fecha = datetime.now().strftime("%d/%m/%Y")
    hora = datetime.now().strftime("%H:%M")

    return dbc.Navbar(

        dbc.Container(

            [

                # ===========================
                # TITULO (SIN LOGO)
                # ===========================

                html.Div(

                    [

                        html.H4(

                            "Panel de Control",

                            className="navbar-title"

                        ),

                        html.Small(

                            "Sistema Inteligente de Gestión Hídrica",

                            className="navbar-subtitle"

                        )

                    ],

                    className="navbar-left"

                ),

                # ===========================
                # LADO DERECHO
                # ===========================

                html.Div(

                    [

                        html.Div(

                            [

                                html.I(
                                    className="bi bi-calendar3 me-2"
                                ),

                                html.Span(fecha)

                            ],

                            className="navbar-chip"

                        ),

                        html.Div(

                            [

                                html.I(
                                    className="bi bi-clock me-2"
                                ),

                                html.Span(hora)

                            ],

                            className="navbar-chip"

                        ),

                        html.Div(

                            [

                                html.I(
                                    className="bi bi-bell-fill me-2"
                                ),

                                html.Span("3")

                            ],

                            className="navbar-chip notification"

                        ),

                        dbc.DropdownMenu(

                            label="👤 Adriano",

                            color="success",

                            align_end=True,

                            children=[

                                dbc.DropdownMenuItem("Mi Perfil"),

                                dbc.DropdownMenuItem("Configuración"),

                                dbc.DropdownMenuItem(divider=True),

                                dbc.DropdownMenuItem(

                                    "Cerrar Sesión",

                                    id="logout"

                                )

                            ]

                        )

                    ],

                    className="navbar-right"

                )

            ],

            fluid=True

        ),

        className="navbar-dashboard"

    )