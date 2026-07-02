from dash import Input, Output


def register_login_callbacks(app):

    @app.callback(

        Output("url", "pathname"),

        Input("btn-login", "n_clicks"),

        prevent_initial_call=True

    )
    def iniciar_sesion(n_clicks):

        return "/dashboard"