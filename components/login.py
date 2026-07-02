from dash import html, dcc
import dash_bootstrap_components as dbc


login_layout = html.Div(

    className="login-page",

    children=[

        html.Div(

            className="login-overlay",

            children=[

                html.Div(

                    className="login-right",

                    children=[

                        html.Div(

                            className="login-card",

                            children=[

                                html.Img(
                                    src="/assets/images/logo.png",
                                    className="login-logo"
                                ),

                                html.H1(
                                    "HIDRODATA",
                                    className="login-title"
                                ),

                                html.P(
                                    "Sistema Inteligente de Gestión Hídrica",
                                    className="login-subtitle"
                                ),

                                dbc.Input(
                                    id="Adriano Bayona",
                                    type="text",
                                    placeholder="usuario",
                                    className="login-input"
                                ),

                                dbc.Input(
                                    id="password",
                                    type="password",
                                    placeholder="Contraseña",
                                    className="login-input"
                                ),

                                dbc.Button(

                                    "Iniciar Sesión",

                                    id="btn-login",

                                    n_clicks=0,

                                    color="success",

                                    className="login-button"

                                )

                            ]

                        )

                    ]

                )

            ]

        )

    ]

)