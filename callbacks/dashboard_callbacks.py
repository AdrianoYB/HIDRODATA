from dash import Input, Output, dcc


from components.export import exportar_excel
from components.pdf_export import exportar_pdf


from components.cards import crear_kpis
from components.table import tabla_datos
from components.alerts import crear_alertas


from components.graphs import (

    grafico_humedad,
    grafico_temperatura,
    grafico_consumo,
    grafico_tanque

)



def register_dashboard_callbacks(app):



    # ==========================================================
    # ACTUALIZACIÓN AUTOMÁTICA DEL DASHBOARD
    # ==========================================================


    @app.callback(

        Output(
            "kpis-container",
            "children"
        ),

        Output(
            "tabla-container",
            "children"
        ),

        Output(
            "alertas-container",
            "children"
        ),

        Output(
            "grafico-humedad-container",
            "children"
        ),

        Output(
            "grafico-tanque-container",
            "children"
        ),

        Output(
            "grafico-temperatura-container",
            "children"
        ),

        Output(
            "grafico-consumo-container",
            "children"
        ),


        Input(

            "interval-update",

            "n_intervals"

        )

    )


    def actualizar_dashboard(n):


        print(
            "Actualizando dashboard:",
            n
        )



        return (

            crear_kpis(),

            tabla_datos(),

            crear_alertas(),

            grafico_humedad(),

            grafico_tanque(),

            grafico_temperatura(),

            grafico_consumo()

        )





    # ==========================================================
    # EXPORTAR EXCEL
    # ==========================================================


    @app.callback(

        Output(
            "download-excel",
            "data"
        ),

        Input(
            "btn-exportar-excel",
            "n_clicks"
        ),

        prevent_initial_call=True

    )


    def descargar_excel(n_clicks):


        if not n_clicks:

            return None



        return exportar_excel()





    # ==========================================================
    # EXPORTAR PDF
    # ==========================================================


    @app.callback(

        Output(
            "download-pdf",
            "data"
        ),

        Input(
            "btn-exportar-pdf",
            "n_clicks"
        ),

        prevent_initial_call=True

    )


    def descargar_pdf(n_clicks):


        if not n_clicks:

            return None



        print(
            "1 - Entrando al callback PDF"
        )



        pdf = exportar_pdf()



        print(
            "2 - PDF generado"
        )



        print(

            "Bytes:",

            len(pdf.getvalue())

        )



        return dcc.send_bytes(

            pdf.getvalue(),

            "Reporte_HIDRODATA.pdf"

        )