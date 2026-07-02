import pandas as pd


ARCHIVO_USUARIOS = "data/usuarios.xlsx"



def cargar_usuarios():

    df = pd.read_excel(
        ARCHIVO_USUARIOS
    )

    return df



def validar_usuario(usuario, password):


    df = cargar_usuarios()


    usuario_encontrado = df[

        (df["Usuario"] == usuario) &

        (df["Password"] == password) &

        (df["Estado"] == "Activo")

    ]



    if len(usuario_encontrado) == 1:

        return usuario_encontrado.iloc[0]


    return None