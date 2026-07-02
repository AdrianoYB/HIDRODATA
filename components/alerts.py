from dash import html
import dash_bootstrap_components as dbc

from utils.data_loader import ultimo_registro


def crear_alertas():

    dato = ultimo_registro()

    alertas = []


    # ==================================================
    # HUMEDAD DEL SUELO
    # ==================================================

    humedad = dato["HumedadSuelo_%"]


    if humedad < 30:

        alertas.append(

            dbc.Alert(

                [

                    html.I(
                        className="bi bi-exclamation-triangle-fill me-2"
                    ),

                    f"Suelo seco crítico ({humedad}%). Se requiere riego inmediato."

                ],

                color="danger"

            )

        )


    elif humedad < 45:

        alertas.append(

            dbc.Alert(

                [

                    html.I(
                        className="bi bi-droplet-half me-2"
                    ),

                    f"Humedad baja ({humedad}%). Se recomienda activar riego."

                ],

                color="warning"

            )

        )


    else:

        alertas.append(

            dbc.Alert(

                [

                    html.I(
                        className="bi bi-check-circle-fill me-2"
                    ),

                    f"Humedad adecuada ({humedad}%)."

                ],

                color="success"

            )

        )



    # ==================================================
    # TEMPERATURA
    # ==================================================

    temperatura = dato["Temperatura_C"]


    if temperatura > 35:

        alertas.append(

            dbc.Alert(

                [

                    html.I(
                        className="bi bi-thermometer-high me-2"
                    ),

                    f"Temperatura crítica ({temperatura} °C). Riesgo de estrés hídrico."

                ],

                color="danger"

            )

        )


    elif temperatura > 30:

        alertas.append(

            dbc.Alert(

                [

                    html.I(
                        className="bi bi-thermometer-sun me-2"
                    ),

                    f"Temperatura elevada ({temperatura} °C)."

                ],

                color="warning"

            )

        )


    else:

        alertas.append(

            dbc.Alert(

                [

                    html.I(
                        className="bi bi-thermometer-half me-2"
                    ),

                    f"Temperatura normal ({temperatura} °C)."

                ],

                color="info"

            )

        )



    # ==================================================
    # TANQUE
    # ==================================================

    tanque = dato["NivelTanque_%"]


    if tanque < 25:

        alertas.append(

            dbc.Alert(

                [

                    html.I(
                        className="bi bi-water me-2"
                    ),

                    f"Nivel crítico del tanque ({tanque}%)."

                ],

                color="danger"

            )

        )


    elif tanque < 60:

        alertas.append(

            dbc.Alert(

                [

                    html.I(
                        className="bi bi-water me-2"
                    ),

                    f"Nivel medio del tanque ({tanque}%)."

                ],

                color="warning"

            )

        )


    else:

        alertas.append(

            dbc.Alert(

                [

                    html.I(
                        className="bi bi-water me-2"
                    ),

                    f"Tanque en nivel correcto ({tanque}%)."

                ],

                color="success"

            )

        )



    # ==================================================
    # BOMBA
    # ==================================================

    bomba = dato["Bomba"]


    if str(bomba).lower() in ["apagada", "off", "0"]:

        alertas.append(

            dbc.Alert(

                [

                    html.I(
                        className="bi bi-power me-2"
                    ),

                    "Bomba apagada."

                ],

                color="secondary"

            )

        )


    else:

        alertas.append(

            dbc.Alert(

                [

                    html.I(
                        className="bi bi-lightning-fill me-2"
                    ),

                    "Bomba funcionando correctamente."

                ],

                color="success"

            )

        )



    # ==================================================
    # CONSUMO DE AGUA
    # ==================================================

    consumo = dato["ConsumoAgua_L"]


    if consumo > 100:

        alertas.append(

            dbc.Alert(

                [

                    html.I(
                        className="bi bi-droplet me-2"
                    ),

                    f"Consumo elevado de agua ({consumo} L)."

                ],

                color="warning"

            )

        )



    # ==================================================
    # ESTADO DEL SISTEMA
    # ==================================================

    estado = dato["EstadoSistema"]


    if str(estado).lower() == "activo":

        alertas.append(

            dbc.Alert(

                [

                    html.I(
                        className="bi bi-cpu-fill me-2"
                    ),

                    "Sistema operativo correctamente."

                ],

                color="success"

            )

        )


    else:

        alertas.append(

            dbc.Alert(

                [

                    html.I(
                        className="bi bi-x-circle-fill me-2"
                    ),

                    f"Sistema detenido: {estado}"

                ],

                color="danger"

            )

        )



    return html.Div(

        alertas

    )