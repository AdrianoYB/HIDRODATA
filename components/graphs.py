from dash import dcc
import plotly.express as px
import plotly.graph_objects as go

from utils.data_loader import cargar_datos


# ==========================================================
# ESTILO GENERAL
# ==========================================================

COLOR_AZUL = "#2196F3"
COLOR_VERDE = "#2E7D32"
COLOR_NARANJA = "#FB8C00"
COLOR_TURQUESA = "#26A69A"

FONDO = "#FFFFFF"
GRID = "#E8EEF5"


# ==========================================================
# HUMEDAD
# ==========================================================

def grafico_humedad():

    df = cargar_datos()

    fig = px.line(
        df,
        x="FechaHora",
        y="HumedadSuelo_%",
        title="💧 Humedad del Suelo",
        markers=True
    )

    fig.update_traces(

        line=dict(
            color=COLOR_AZUL,
            width=4
        ),

        marker=dict(
            size=8,
            color=COLOR_AZUL,
            line=dict(color="white", width=2)
        ),

        fill="tozeroy",

        fillcolor="rgba(33,150,243,0.18)"

    )

    promedio = df["HumedadSuelo_%"].mean()

    fig.add_hline(

        y=promedio,

        line_dash="dash",

        line_color="#EF5350",

        annotation_text=f"Promedio ({promedio:.1f}%)",

        annotation_position="top left"

    )

    fig.update_layout(

        template="plotly_white",

        height=360,

        plot_bgcolor=FONDO,

        paper_bgcolor=FONDO,

        margin=dict(l=20, r=20, t=60, b=20),

        title_font=dict(size=22)

    )

    fig.update_xaxes(

        showgrid=True,

        gridcolor=GRID,

        title=None

    )

    fig.update_yaxes(

        showgrid=True,

        gridcolor=GRID,

        title="Humedad (%)"

    )

    return dcc.Graph(
        figure=fig,
        config={"displayModeBar": False}
    )


# ==========================================================
# TEMPERATURA
# ==========================================================

def grafico_temperatura():

    df = cargar_datos()

    fig = px.area(

        df,

        x="FechaHora",

        y="Temperatura_C",

        title="🌡 Temperatura"

    )

    fig.update_traces(

        line=dict(
            color=COLOR_NARANJA,
            width=4
        ),

        fillcolor="rgba(251,140,0,.25)"

    )

    promedio = df["Temperatura_C"].mean()

    fig.add_hline(

        y=promedio,

        line_dash="dash",

        line_color="#E53935",

        annotation_text=f"Promedio ({promedio:.1f}°C)"

    )

    fig.update_layout(

        template="plotly_white",

        height=360,

        plot_bgcolor=FONDO,

        paper_bgcolor=FONDO,

        margin=dict(l=20, r=20, t=60, b=20),

        title_font=dict(size=22)

    )

    fig.update_xaxes(

        showgrid=True,

        gridcolor=GRID,

        title=None

    )

    fig.update_yaxes(

        showgrid=True,

        gridcolor=GRID,

        title="Temperatura (°C)"

    )

    return dcc.Graph(
        figure=fig,
        config={"displayModeBar": False}
    )


# ==========================================================
# CONSUMO
# ==========================================================

def grafico_consumo():

    df = cargar_datos()

    fig = px.bar(

        df.tail(15),

        x="FechaHora",

        y="ConsumoAgua_L",

        title="🚰 Consumo de Agua"

    )

    fig.update_traces(

        marker_color=COLOR_TURQUESA,

        marker_line_color="#0D47A1",

        marker_line_width=1.5

    )

    fig.update_layout(

        template="plotly_white",

        height=360,

        plot_bgcolor=FONDO,

        paper_bgcolor=FONDO,

        margin=dict(l=20, r=20, t=60, b=20),

        title_font=dict(size=22)

    )

    fig.update_xaxes(

        showgrid=False,

        title=None

    )

    fig.update_yaxes(

        showgrid=True,

        gridcolor=GRID,

        title="Litros"

    )

    return dcc.Graph(
        figure=fig,
        config={"displayModeBar": False}
    )


# ==========================================================
# TANQUE
# ==========================================================

def grafico_tanque():

    df = cargar_datos()

    nivel = df.iloc[-1]["NivelTanque_%"]

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=nivel,

            number={

                "suffix":" %",

                "font":{"size":50}

            },

            title={

                "text":"🛢 Nivel del Tanque",

                "font":{"size":22}

            },

            gauge={

                "axis":{

                    "range":[0,100]

                },

                "bar":{

                    "color":"#1565C0"

                },

                "steps":[

                    {

                        "range":[0,30],

                        "color":"#EF5350"

                    },

                    {

                        "range":[30,60],

                        "color":"#FFC107"

                    },

                    {

                        "range":[60,100],

                        "color":"#66BB6A"

                    }

                ],

                "threshold":{

                    "line":{

                        "color":"black",

                        "width":4

                    },

                    "value":nivel

                }

            }

        )

    )

    fig.update_layout(

        height=360,

        margin=dict(l=20, r=20, t=60, b=20),

        paper_bgcolor="white"

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar":False}

    )