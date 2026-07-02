from io import BytesIO
from pathlib import Path
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

from utils.data_loader import cargar_datos


# ==========================================================
# COLORES CORPORATIVOS
# ==========================================================

COLOR_PRINCIPAL = colors.HexColor("#2E7D32")
COLOR_SECUNDARIO = colors.HexColor("#43A047")
COLOR_TEXTO = colors.HexColor("#212121")
COLOR_GRIS = colors.HexColor("#757575")
COLOR_FONDO = colors.HexColor("#F5F5F5")
COLOR_BORDE = colors.HexColor("#A5D6A7")



# ==========================================================
# LOGO
# ==========================================================

LOGO_PATH = (

    Path(__file__)
    .resolve()
    .parent.parent
    / "assets"
    / "images"
    / "logo.png"

)



# ==========================================================
# ESTILOS
# ==========================================================

styles = getSampleStyleSheet()


titulo = styles["Title"]
titulo.alignment = TA_CENTER
titulo.textColor = COLOR_PRINCIPAL
titulo.fontSize = 24


subtitulo = styles["Heading2"]
subtitulo.alignment = TA_CENTER
subtitulo.textColor = COLOR_TEXTO
subtitulo.fontSize = 14


normal = styles["Normal"]
normal.fontSize = 10
normal.leading = 15


pie = styles["Italic"]
pie.alignment = TA_CENTER
pie.textColor = COLOR_GRIS



# ==========================================================
# ENCABEZADO
# ==========================================================

def crear_encabezado(elementos):


    if LOGO_PATH.exists():


        logo = Image(

            str(LOGO_PATH),

            width=2.5 * cm,

            height=2.5 * cm

        )


        tabla = Table(

            [

                [

                    logo,

                    Paragraph(

                        "<b>HIDRODATA</b><br/>"
                        "<font size=11>"
                        "Sistema Inteligente de Gestión Hídrica"
                        "</font>",

                        titulo

                    )

                ]

            ],

            colWidths=[3*cm,14*cm]

        )


        tabla.setStyle(

            TableStyle(

                [

                    (
                        "VALIGN",
                        (0,0),
                        (-1,-1),
                        "MIDDLE"
                    ),

                    (
                        "ALIGN",
                        (1,0),
                        (1,0),
                        "CENTER"
                    )

                ]

            )

        )


        elementos.append(tabla)


    else:


        elementos.append(

            Paragraph(

                "HIDRODATA",

                titulo

            )

        )



    elementos.append(

        Spacer(1,10)

    )


    linea = Table(

        [[""]],

        colWidths=[18*cm],

        rowHeights=[0.15*cm]

    )


    linea.setStyle(

        TableStyle(

            [

                (
                    "BACKGROUND",
                    (0,0),
                    (-1,-1),
                    COLOR_PRINCIPAL
                )

            ]

        )

    )


    elementos.append(linea)


    elementos.append(

        Spacer(1,15)

    )





# ==========================================================
# KPI
# ==========================================================

def crear_kpis(df, elementos):


    humedad = round(
        df["HumedadSuelo_%"].mean(),
        2
    )


    temperatura = round(
        df["Temperatura_C"].mean(),
        2
    )


    tanque = round(
        df["NivelTanque_%"].mean(),
        2
    )


    consumo = round(
        df["ConsumoAgua_L"].sum(),
        2
    )


    datos = [

        [

            Paragraph(

                "<b>HUMEDAD DEL SUELO</b><br/><br/>"
                f"<font size=18 color='#2E7D32'>{humedad}%</font><br/><br/>"
                "Promedio registrado",

                normal

            ),


            Paragraph(

                "<b>TEMPERATURA</b><br/><br/>"
                f"<font size=18 color='#D32F2F'>{temperatura} °C</font><br/><br/>"
                "Temperatura media",

                normal

            )

        ],


        [

            Paragraph(

                "<b>NIVEL DEL TANQUE</b><br/><br/>"
                f"<font size=18 color='#0288D1'>{tanque}%</font><br/><br/>"
                "Disponibilidad",

                normal

            ),


            Paragraph(

                "<b>CONSUMO DE AGUA</b><br/><br/>"
                f"<font size=18 color='#388E3C'>{consumo} L</font><br/><br/>"
                "Consumo acumulado",

                normal

            )

        ]

    ]


    tabla = Table(

        datos,

        colWidths=[8*cm,8*cm],

        rowHeights=[3.5*cm,3.5*cm]

    )


    tabla.setStyle(

        TableStyle(

            [

                (
                    "BOX",
                    (0,0),
                    (-1,-1),
                    1,
                    COLOR_BORDE
                ),

                (
                    "INNERGRID",
                    (0,0),
                    (-1,-1),
                    0.8,
                    COLOR_BORDE
                ),

                (
                    "ALIGN",
                    (0,0),
                    (-1,-1),
                    "CENTER"
                ),

                (
                    "VALIGN",
                    (0,0),
                    (-1,-1),
                    "MIDDLE"
                )

            ]

        )

    )


    elementos.append(

        Paragraph(

            "Indicadores principales",

            subtitulo

        )

    )


    elementos.append(

        Spacer(1,10)

    )


    elementos.append(tabla)


    elementos.append(

        Spacer(1,20)

    )
    # ==========================================================
# ESTADO DEL SISTEMA
# ==========================================================

def crear_estado(df, elementos):


    ultimo = df.iloc[-1]


    humedad = ultimo["HumedadSuelo_%"]

    tanque = ultimo["NivelTanque_%"]

    temperatura = ultimo["Temperatura_C"]



    alertas = []



    if humedad < 30:

        alertas.append(
            "Humedad del suelo baja"
        )


    if tanque < 25:

        alertas.append(
            "Nivel del tanque crítico"
        )


    if temperatura > 35:

        alertas.append(
            "Temperatura elevada"
        )



    if len(alertas) == 0:


        estado = "SISTEMA OPERATIVO"


        mensaje = (

            "Los sensores presentan valores normales "
            "sin condiciones críticas."

        )


        color_estado = COLOR_SECUNDARIO



    else:


        estado = "ATENCIÓN REQUERIDA"


        mensaje = "<br/>".join(alertas)


        color_estado = colors.red




    contenido = Table(

        [

            [

                Paragraph(

                    f"<b>{estado}</b><br/><br/>"
                    f"{mensaje}",

                    normal

                )

            ]

        ],

        colWidths=[16*cm]

    )



    contenido.setStyle(

        TableStyle(

            [

                (
                    "BACKGROUND",
                    (0,0),
                    (-1,-1),
                    COLOR_FONDO
                ),


                (
                    "BOX",
                    (0,0),
                    (-1,-1),
                    1,
                    color_estado
                ),


                (
                    "ALIGN",
                    (0,0),
                    (-1,-1),
                    "CENTER"
                ),

                (
                    "VALIGN",
                    (0,0),
                    (-1,-1),
                    "MIDDLE"
                )

            ]

        )

    )



    elementos.append(

        Paragraph(

            "Estado del Sistema",

            subtitulo

        )

    )


    elementos.append(

        Spacer(1,10)

    )


    elementos.append(contenido)


    elementos.append(

        Spacer(1,20)

    )





# ==========================================================
# TABLA DE ÚLTIMAS LECTURAS
# ==========================================================

def crear_tabla_lecturas(df, elementos):


    datos = [

        [

            "Fecha",

            "Humedad",

            "Temp.",

            "Tanque",

            "Consumo"

        ]

    ]



    ultimos = df.tail(10)



    for _, fila in ultimos.iterrows():


        fecha = ""


        if "FechaHora" in df.columns:

            fecha = str(
                fila["FechaHora"]
            )

        else:

            fecha = "-"



        datos.append(

            [

                fecha,

                f'{fila["HumedadSuelo_%"]} %',

                f'{fila["Temperatura_C"]} °C',

                f'{fila["NivelTanque_%"]} %',

                f'{fila["ConsumoAgua_L"]} L'

            ]

        )



    tabla = Table(

        datos,

        colWidths=[4*cm,3*cm,3*cm,3*cm,3*cm]

    )



    tabla.setStyle(

        TableStyle(

            [

                (
                    "BACKGROUND",
                    (0,0),
                    (-1,0),
                    COLOR_PRINCIPAL
                ),


                (
                    "TEXTCOLOR",
                    (0,0),
                    (-1,0),
                    colors.white
                ),


                (
                    "ALIGN",
                    (0,0),
                    (-1,-1),
                    "CENTER"
                ),


                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    0.5,
                    COLOR_BORDE
                ),


                (
                    "BACKGROUND",
                    (0,1),
                    (-1,-1),
                    COLOR_FONDO
                )

            ]

        )

    )



    elementos.append(

        Paragraph(

            "Últimas lecturas registradas",

            subtitulo

        )

    )



    elementos.append(

        Spacer(1,10)

    )



    elementos.append(tabla)



    elementos.append(

        Spacer(1,20)

    )





# ==========================================================
# GENERAR PDF
# ==========================================================

def exportar_pdf():


    df = cargar_datos()



    buffer = BytesIO()



    documento = SimpleDocTemplate(

        buffer,

        rightMargin=2*cm,

        leftMargin=2*cm,

        topMargin=2*cm,

        bottomMargin=2*cm

    )



    elementos = []



    crear_encabezado(

        elementos

    )



    elementos.append(

        Paragraph(

            "Fecha de generación: "
            f"{datetime.now().strftime('%d/%m/%Y %H:%M')}",

            normal

        )

    )



    elementos.append(

        Spacer(1,15)

    )



    crear_kpis(

        df,

        elementos

    )



    crear_estado(

        df,

        elementos

    )



    crear_tabla_lecturas(

        df,

        elementos

    )



    elementos.append(

        Paragraph(

            "Reporte generado automáticamente por HIDRODATA",

            pie

        )

    )



    documento.build(

        elementos

    )



    buffer.seek(0)



    return buffer