from dash import Input, Output

from components.statistics import crear_estadisticas
from components.table import tabla_datos



def register_reportes_callbacks(app):



    @app.callback(

        Output(
            "estadisticas-reporte",
            "children"
        ),

        Output(
            "tabla-reporte",
            "children"
        ),


        Input(
            "periodo-reporte",
            "value"
        )

    )


    def actualizar_reporte(periodo):


        print(
            "Actualizando reporte:",
            periodo
        )


        return (

            crear_estadisticas(
                periodo
            ),


            tabla_datos(
                periodo
            )

        )