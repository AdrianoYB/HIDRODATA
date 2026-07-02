from dash import html
import dash_bootstrap_components as dbc

from utils.data_loader import ultimo_registro



def sensores_layout():

    dato = ultimo_registro()



    sensores = [


        {
            "titulo": "Humedad del Suelo",
            "icono": "bi bi-droplet-fill",
            "valor": f"{dato['HumedadSuelo_%']} %",
            "progreso": dato["HumedadSuelo_%"],
            "color": (
                "success"
                if dato["HumedadSuelo_%"] >= 50
                else "warning"
            ),
            "estado": (
                "Nivel correcto"
                if dato["HumedadSuelo_%"] >= 50
                else "Humedad baja"
            )
        },



        {
            "titulo": "Temperatura",
            "icono": "bi bi-thermometer-half",
            "valor": f"{dato['Temperatura_C']} °C",
            "progreso": min(
                dato["Temperatura_C"] * 3,
                100
            ),
            "color": (
                "danger"
                if dato["Temperatura_C"] > 35
                else "info"
            ),
            "estado": (
                "Temperatura alta"
                if dato["Temperatura_C"] > 35
                else "Normal"
            )
        },



        {
            "titulo": "Humedad Ambiental",
            "icono": "bi bi-cloud-fill",
            "valor": f"{dato['HumedadAmb_%']} %",
            "progreso": dato["HumedadAmb_%"],
            "color": "primary",
            "estado": "Sensor activo"
        },



        {
            "titulo": "Nivel del Tanque",
            "icono": "bi bi-water",
            "valor": f"{dato['NivelTanque_%']} %",
            "progreso": dato["NivelTanque_%"],
            "color": (
                "danger"
                if dato["NivelTanque_%"] < 30
                else "success"
            ),
            "estado": (
                "Nivel crítico"
                if dato["NivelTanque_%"] < 30
                else "Correcto"
            )
        },



        {
            "titulo": "Caudal",
            "icono": "bi bi-speedometer",
            "valor": f"{dato['Caudal_Lmin']} L/min",
            "progreso": min(
                dato["Caudal_Lmin"] * 10,
                100
            ),
            "color": "info",
            "estado": "Flujo detectado"
        },



        {
            "titulo": "Consumo Agua",
            "icono": "bi bi-droplet",
            "valor": f"{dato['ConsumoAgua_L']} L",
            "progreso": min(
                dato["ConsumoAgua_L"],
                100
            ),
            "color": "success",
            "estado": "Medición registrada"
        },



        {
            "titulo": "Bomba",
            "icono": "bi bi-power",
            "valor": str(dato["Bomba"]),
            "progreso": 100,
            "color": (
                "success"
                if str(dato["Bomba"]).lower()
                in ["encendida", "on", "1"]
                else "secondary"
            ),
            "estado": "Funcionamiento"
        },



        {
            "titulo": "Estado Sistema",
            "icono": "bi bi-cpu-fill",
            "valor": str(dato["EstadoSistema"]),
            "progreso": 100,
            "color": (
                "success"
                if str(dato["EstadoSistema"]).lower()
                == "activo"
                else "danger"
            ),
            "estado": "Estado general"
        }

    ]



    tarjetas = []



    for s in sensores:


        tarjetas.append(

            dbc.Col(

                dbc.Card(

                    dbc.CardBody(

                        [

                            html.Div(

                                [

                                    html.I(

                                        className=s["icono"],

                                        style={

                                            "fontSize": "45px"

                                        }

                                    ),


                                    html.H5(

                                        s["titulo"],

                                        className="mt-3"

                                    ),


                                    html.H2(

                                        s["valor"],

                                        className="fw-bold"

                                    ),



                                    dbc.Progress(

                                        value=s["progreso"],

                                        color=s["color"],

                                        striped=True,

                                        animated=True,

                                        style={

                                            "height": "15px"

                                        }

                                    ),



                                    html.Br(),



                                    dbc.Badge(

                                        s["estado"],

                                        color=s["color"],

                                        className="p-2"

                                    )


                                ],

                                className="text-center"

                            )

                        ]

                    ),


                    className="shadow-lg h-100"

                ),


                lg=3,

                md=6,

                className="mb-4"

            )

        )



    return dbc.Container(

        [

            html.Br(),


            html.H2(

                "🔧 Estado de Sensores",

                className="dashboard-title"

            ),



            html.P(

                "Monitoreo individual de los sensores instalados en el sistema HIDRODATA.",

                className="dashboard-subtitle"

            ),



            html.Hr(),



            dbc.Row(

                tarjetas,

                className="g-4"

            )


        ],

        fluid=True

    )