import pandas as pd


ARCHIVO_USUARIOS = "data/usuarios.xlsx"



def cargar_usuarios():

    return pd.read_excel(
        ARCHIVO_USUARIOS
    )




def guardar_usuario(datos):


    df = cargar_usuarios()


    nuevo_id = int(df["ID"].max()) + 1



    nuevo = pd.DataFrame(

        [

            {

                "ID": nuevo_id,

                "Usuario": datos["usuario"],

                "Nombre": datos["nombre"],

                "Password": datos["password"],

                "Rol": datos["rol"],

                "Estado": "Activo"

            }

        ]

    )


    df = pd.concat(

        [
            df,
            nuevo
        ],

        ignore_index=True

    )


    df.to_excel(

        ARCHIVO_USUARIOS,

        index=False

    )


    return df





def eliminar_usuario(id_usuario):


    df = cargar_usuarios()


    df = df[
        df["ID"] != id_usuario
    ]


    df.to_excel(

        ARCHIVO_USUARIOS,

        index=False

    )


    return df





def actualizar_usuario(

    id_usuario,
    usuario,
    nombre,
    rol,
    estado

):


    df = cargar_usuarios()


    indice = df.index[
        df["ID"] == id_usuario
    ]


    if len(indice):

        i = indice[0]


        df.loc[i,"Usuario"] = usuario

        df.loc[i,"Nombre"] = nombre

        df.loc[i,"Rol"] = rol

        df.loc[i,"Estado"] = estado



    df.to_excel(

        ARCHIVO_USUARIOS,

        index=False

    )


    return df