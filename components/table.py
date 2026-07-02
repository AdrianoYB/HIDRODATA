from dash import dash_table

from utils.data_loader import cargar_datos_periodo



def tabla_datos(periodo="todo"):


    df = cargar_datos_periodo(
        periodo
    )


    # Ordenar por fecha más reciente

    df = df.sort_values(

        "FechaHora",

        ascending=False

    ).head(20)



    return dash_table.DataTable(


        data=df.to_dict(
            "records"
        ),



        columns=[


            {
                "name":"Fecha",
                "id":"FechaHora"
            },


            {
                "name":"Humedad Suelo (%)",
                "id":"HumedadSuelo_%"
            },


            {
                "name":"Temperatura (°C)",
                "id":"Temperatura_C"
            },


            {
                "name":"Humedad Ambiente (%)",
                "id":"HumedadAmb_%"
            },


            {
                "name":"Nivel Tanque (%)",
                "id":"NivelTanque_%"
            },


            {
                "name":"Caudal L/min",
                "id":"Caudal_Lmin"
            },


            {
                "name":"Consumo Agua (L)",
                "id":"ConsumoAgua_L"
            },


            {
                "name":"Estado",
                "id":"EstadoSistema"
            }


        ],



        page_size=10,


        sort_action="native",


        filter_action="native",



        style_table={

            "overflowX":"auto"

        },



        style_header={

            "backgroundColor":"#1F4E79",

            "color":"white",

            "fontWeight":"bold"

        },



        style_cell={

            "textAlign":"center",

            "padding":"10px"

        }


    )