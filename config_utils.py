import os
import pandas as pd
import pyperclip

CSV_FILE = "configuraciones.csv"

# === Inicialización ===
def inicializar_csv():
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=["config", "numero", "texto"])
        df.to_csv(CSV_FILE, index=False)

def cargar_configuraciones():
    if not os.path.exists(CSV_FILE):
        inicializar_csv()
    return pd.read_csv(CSV_FILE, dtype=str).fillna("")

def guardar_configuraciones(df):
    df.to_csv(CSV_FILE, index=False)

# === Operaciones básicas ===
def agregar_texto(config, numero, texto):
    df = cargar_configuraciones()
    df = df[~((df["config"] == config) & (df["numero"] == str(numero)))]
    nuevo = pd.DataFrame([[config, str(numero), texto]], columns=["config","numero","texto"])
    df = pd.concat([df, nuevo], ignore_index=True)
    guardar_configuraciones(df)

def editar_texto(config, numero, nuevo_texto):
    df = cargar_configuraciones()
    mask = (df["config"] == config) & (df["numero"] == str(numero))
    if mask.any():
        df.loc[mask, "texto"] = nuevo_texto
    else:
        df = pd.concat([df, pd.DataFrame([[config, numero, nuevo_texto]], columns=["config","numero","texto"])], ignore_index=True)
    guardar_configuraciones(df)

def eliminar_texto(config, numero):
    df = cargar_configuraciones()
    df = df[~((df["config"] == config) & (df["numero"] == str(numero)))]
    guardar_configuraciones(df)

def copiar_texto(config, numero):
    df = cargar_configuraciones()
    df_sel = df[(df["config"]==config) & (df["numero"]==str(numero))]
    if not df_sel.empty:
        pyperclip.copy(df_sel.iloc[0]["texto"])
        return True
    return False

def listar_configuraciones():
    df = cargar_configuraciones()
    return df["config"].unique().tolist()

def listar_textos(config):
    df = cargar_configuraciones()
    df_sel = df[df["config"]==config]
    textos = []
    for i in range(10):
        t = df_sel[df_sel["numero"]==str(i)]["texto"]
        textos.append(t.iloc[0] if not t.empty else "")
    return textos

# === Exportar / Importar ===
def exportar_excel(ruta):
    """Exporta todas las configuraciones a un archivo Excel"""
    df = cargar_configuraciones()
    df.to_excel(ruta, index=False)

def exportar_csv(ruta):
    """Exporta todas las configuraciones a un archivo CSV"""
    df = cargar_configuraciones()
    df.to_csv(ruta, index=False)

def importar_csv(ruta):
    """Importa configuraciones desde un CSV y evita duplicados"""
    try:
        df_nuevo = pd.read_csv(ruta, dtype=str).fillna("")
        if not {"config","numero","texto"}.issubset(df_nuevo.columns):
            return False
        df_actual = cargar_configuraciones()
        # Evitar duplicados: conservar últimos
        df_final = pd.concat([df_actual, df_nuevo]).drop_duplicates(subset=["config","numero"], keep="last")
        guardar_configuraciones(df_final)
        return True
    except Exception as e:
        print("Error importar_csv:", e)
        return False
