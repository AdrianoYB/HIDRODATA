from dash import (
    Input,
    Output,
    State,
    ctx,
    ALL
)

from dash.exceptions import PreventUpdate


from pages.usuarios import tabla_usuarios


from utils.usuarios_data import (
    guardar_usuario,
    eliminar_usuario,
    actualizar_usuario
)



def register_usuarios_callbacks(app):


    # ======================================================
    # ACTUALIZAR TABLA
    # ======================================================

    @app.callback(

        Output(
            "tabla-usuarios",
            "children"
        ),

        Input(
            "actualizar-usuarios",
            "data"
        )

    )

    def refrescar_tabla(valor):

        return tabla_usuarios()



    # ======================================================
    # CREAR USUARIO
    # ======================================================

    @app.callback(

        Output(
            "actualizar-usuarios",
            "data"
        ),

        Input(
            "guardar-nuevo-usuario",
            "n_clicks"
        ),

        State(
            "input-usuario",
            "value"
        ),

        State(
            "input-nombre",
            "value"
        ),

        State(
            "input-password",
            "value"
        ),

        State(
            "select-rol",
            "value"
        ),

        prevent_initial_call=True

    )

    def crear_usuario(

        clicks,
        usuario,
        nombre,
        password,
        rol

    ):


        if not clicks:

            raise PreventUpdate



        guardar_usuario(

            usuario,

            nombre,

            password,

            rol

        )


        return clicks




    # ======================================================
    # ELIMINAR USUARIO
    # ======================================================

    @app.callback(

        Output(
            "actualizar-usuarios",
            "data",
            allow_duplicate=True
        ),


        Input(

            {
                "type":"eliminar-usuario",

                "id":ALL

            },

            "n_clicks"

        ),


        prevent_initial_call=True

    )

    def eliminar_usuario_callback(clicks):


        if not clicks or not any(clicks):

            raise PreventUpdate



        boton = ctx.triggered_id


        id_usuario = boton["id"]



        eliminar_usuario(

            id_usuario

        )


        return id_usuario





    # ======================================================
    # ABRIR MODAL EDITAR
    # ======================================================

    @app.callback(

        Output(
            "modal-editar-usuario",
            "is_open"
        ),

        Output(
            "editar-id",
            "data"
        ),


        Input(

            {
                "type":"editar-usuario",

                "id":ALL

            },

            "n_clicks"

        ),


        prevent_initial_call=True

    )

    def abrir_modal_editar(clicks):


        if not clicks or not any(clicks):

            raise PreventUpdate



        boton = ctx.triggered_id



        return True, boton["id"]