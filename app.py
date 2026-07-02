from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc


# =====================================================
# LOGIN
# =====================================================

from components.login import login_layout


# =====================================================
# PÁGINAS
# =====================================================

from pages.dashboard import dashboard_layout
from pages.sensores import sensores_layout
from pages.alertas import alertas_layout
from pages.reportes import reportes_layout
from pages.usuarios import usuarios_layout


# =====================================================
# CALLBACKS
# =====================================================

from callbacks.login_callbacks import register_login_callbacks
from callbacks.dashboard_callbacks import register_dashboard_callbacks
from callbacks.reportes_callbacks import register_reportes_callbacks
from callbacks.usuarios_callbacks import register_usuarios_callbacks


# =====================================================
# APP
# =====================================================

app = Dash(

    __name__,

    external_stylesheets=[

        dbc.themes.BOOTSTRAP,
        dbc.icons.BOOTSTRAP

    ],

    suppress_callback_exceptions=True

)

# =====================================================
# IMPORTANTE PARA RENDER
# =====================================================

server = app.server

app.title = "HIDRODATA"


# =====================================================
# LAYOUT PRINCIPAL
# =====================================================

app.layout = html.Div(

    [

        dcc.Location(

            id="url",

            refresh=False

        ),

        html.Div(

            id="page-content"

        )

    ]

)


# =====================================================
# REGISTRO CALLBACKS
# =====================================================

register_login_callbacks(app)
register_dashboard_callbacks(app)
register_reportes_callbacks(app)
register_usuarios_callbacks(app)


# =====================================================
# NAVEGACIÓN
# =====================================================

@app.callback(

    Output(

        "page-content",

        "children"

    ),

    Input(

        "url",

        "pathname"

    )

)

def mostrar_pagina(pathname):

    if pathname == "/dashboard":

        return dashboard_layout

    elif pathname == "/sensores":

        return sensores_layout()

    elif pathname == "/alertas":

        return alertas_layout()

    elif pathname == "/reportes":

        return reportes_layout

    elif pathname == "/usuarios":

        return usuarios_layout

    else:

        return login_layout


# =====================================================
# EJECUCIÓN
# =====================================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=8050,

        debug=False

    )