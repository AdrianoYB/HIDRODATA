from dash import html
import dash_bootstrap_components as dbc


def sidebar():

    return html.Div(

        [

            # ======================================
            # LOGO
            # ======================================

            html.Div(

                [

                    html.Img(

                        src="/assets/images/logo.png",

                        className="sidebar-logo"

                    ),

                    html.H4(

                        "HIDRODATA",

                        className="sidebar-title"

                    )

                ],

                className="sidebar-header"

            ),

            html.Hr(),

            # ======================================
            # MENÚ
            # ======================================

            dbc.Nav(

                [

                    dbc.NavLink(

                        [

                            html.I(className="bi bi-speedometer2 me-2"),

                            "Dashboard"

                        ],

                        href="/dashboard",

                        active="exact"

                    ),

                    dbc.NavLink(

                        [

                            html.I(className="bi bi-moisture me-2"),

                            "Sensores"

                        ],

                        href="/sensores",

                        active="exact"

                    ),

                    dbc.NavLink(

                        [

                            html.I(className="bi bi-bell me-2"),

                            "Alertas"

                        ],

                        href="/alertas",

                        active="exact"

                    ),

                    dbc.NavLink(

                        [

                            html.I(className="bi bi-file-earmark-bar-graph me-2"),

                            "Reportes"

                        ],

                        href="/reportes",

                        active="exact"

                    ),

                    dbc.NavLink(

                        [

                            html.I(className="bi bi-people me-2"),

                            "Usuarios"

                        ],

                        href="/usuarios",

                        active="exact"

                    ),

                    dbc.NavLink(

                        [

                            html.I(className="bi bi-gear me-2"),

                            "Configuración"

                        ],

                        href="/configuracion",

                        active="exact"

                    )

                ],

                vertical=True,

                pills=True,

                className="sidebar-menu"

            )

        ],

        className="sidebar"

    )