# ============================================================
# IMPORTACIÓN DE LIBRERÍAS
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="Bank Marketing EDA",
    layout="wide",
    page_icon="📊"
)

sns.set_theme(style="whitegrid", palette="deep")

# ============================================================
# CLASE PRINCIPAL (POO)
# Aqui organizamos todo el analisis porque asi el codigo
# queda mas limpio y profesional (y no todo mezclado)
# ============================================================

class DataAnalyzer:

    def __init__(self, df):
        self.df = df

    # -------------------------
    # Clasificación de variables
    # -------------------------
    def clasificar_variables(self):
        numericas = self.df.select_dtypes(include=np.number).columns.tolist()
        categoricas = self.df.select_dtypes(exclude=np.number).columns.tolist()
        return numericas, categoricas

    # -------------------------
    # Estadísticas descriptivas
    # -------------------------
    def estadisticas_descriptivas(self):
        return self.df.describe()

    def mediana(self):
        return self.df.median(numeric_only=True)

    def moda(self):
        return self.df.mode().iloc[0]

    def valores_nulos(self):
        return self.df.isnull().sum()

    def tasa_aceptacion(self):
        return self.df["y"].value_counts(normalize=True) * 100

    # -------------------------
    # Visualizaciones
    # -------------------------
    def histograma(self, columna):
        fig, ax = plt.subplots(figsize=(8,5))
        sns.histplot(self.df[columna], kde=True, ax=ax)
        ax.axvline(self.df[columna].mean(), color="red", linestyle="--", label="Media")
        ax.axvline(self.df[columna].median(), color="green", linestyle="-", label="Mediana")
        ax.set_title(f"Distribución de {columna}")
        ax.legend()
        return fig

    def boxplot(self, columna):
        fig, ax = plt.subplots(figsize=(8,5))
        sns.boxplot(x=self.df["y"], y=self.df[columna], ax=ax)
        ax.set_title(f"{columna} vs Resultado de Campaña")
        return fig

    def grafico_categorico(self, columna):
        fig, ax = plt.subplots(figsize=(9,5))
        sns.countplot(x=self.df[columna], ax=ax)
        plt.xticks(rotation=45)
        ax.set_title(f"Distribución de {columna}")
        return fig


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📊 Navegación")
menu = st.sidebar.radio(
    "Seleccione una sección:",
    ["🏠 Home", "📂 Cargar Datos", "📊 Análisis EDA", "📌 Conclusiones"]
)

# ============================================================
# HOME
# ============================================================

if menu == "🏠 Home":

    st.title("📈 Análisis Exploratorio - Bank Marketing")

    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
        use_container_width=True
    )

    st.markdown("""
    ### 🎯 Objetivo
    Analizar los factores que influyen en la aceptación de campañas bancarias,
    ya que la tasa de efectividad disminuyó en los últimos meses.
    """)

    st.markdown("""
    **Autor:** Ronaldinho Agricio Villalobos Torres  
    Especialización Python for Analytics - 2026
    """)

    st.success("Tecnologías utilizadas: Python, Pandas, NumPy, Matplotlib, Seaborn y Streamlit")


# ============================================================
# CARGA DE DATOS
# ============================================================

elif menu == "📂 Cargar Datos":

    archivo = st.file_uploader("Suba el archivo BankMarketing.csv", type=["csv"])

    if archivo:

        df = pd.read_csv(archivo, sep=";")

        # Renombramos variables para que sean mas entendibles
        df = df.rename(columns={
            "age": "edad",
            "duration": "duracion_llamada",
            "campaign": "numero_contactos",
            "pdays": "dias_desde_ultimo_contacto",
            "previous": "contactos_previos"
        })

        st.session_state["df"] = df

        st.success("Archivo cargado correctamente.")

        st.dataframe(df.head())

        col1, col2 = st.columns(2)
        col1.metric("Filas", df.shape[0])
        col2.metric("Columnas", df.shape[1])

    else:
        st.warning("Debe cargar el archivo para continuar.")


# ============================================================
# ANÁLISIS EDA
# ============================================================

elif menu == "📊 Análisis EDA":

    if "df" not in st.session_state:
        st.warning("Primero debe cargar el dataset.")
        st.stop()

    df = st.session_state["df"]
    analizador = DataAnalyzer(df)

    st.title("📊 Análisis Exploratorio Completo")

    tabs = st.tabs([
        "1️⃣ Info General",
        "2️⃣ Clasificación",
        "3️⃣ Estadísticas",
        "4️⃣ Faltantes",
        "5️⃣ Numéricas",
        "6️⃣ Categóricas",
        "7️⃣ Num vs Cat",
        "8️⃣ Cat vs Cat",
        "9️⃣ Dinámico",
        "🔟 Hallazgos"
    ])

    # =========================================================
    # 1️⃣ INFORMACIÓN GENERAL
    # =========================================================
    with tabs[0]:

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Registros", df.shape[0])
        col2.metric("Total Variables", df.shape[1])
        col3.metric("Valores Nulos Totales", int(analizador.valores_nulos().sum()))

        st.divider()

        st.subheader("Tipos de Datos")

        tipos_df = pd.DataFrame({
            "Variable": df.columns,
            "Tipo de Dato": df.dtypes.values
        })

        st.dataframe(tipos_df, use_container_width=True)

        st.subheader("Valores Nulos por Variable")

        nulos = analizador.valores_nulos().reset_index()
        nulos.columns = ["Variable", "Cantidad Nulos"]

        st.dataframe(nulos, use_container_width=True)

        fig, ax = plt.subplots(figsize=(10,4))
        sns.barplot(data=nulos, x="Variable", y="Cantidad Nulos", ax=ax)
        plt.xticks(rotation=45)
        ax.set_title("Distribución de Valores Nulos")
        st.pyplot(fig)

        with st.expander("Ver detalle técnico (.info())"):
            buffer = io.StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())

    # =========================================================
    # 2️⃣ CLASIFICACIÓN
    # =========================================================
    with tabs[1]:

        numericas, categoricas = analizador.clasificar_variables()

        col1, col2 = st.columns(2)
        col1.info(f"Variables numéricas: {len(numericas)}")
        col2.info(f"Variables categóricas: {len(categoricas)}")

        st.write("Lista numéricas:", numericas)
        st.write("Lista categóricas:", categoricas)

    # =========================================================
    # 3️⃣ ESTADÍSTICAS
    # =========================================================
    with tabs[2]:

        st.dataframe(analizador.estadisticas_descriptivas())
        st.write("Mediana:")
        st.dataframe(analizador.mediana())
        st.write("Moda:")
        st.dataframe(analizador.moda())

        st.markdown("""
        Se observan diferencias entre media y mediana en algunas variables,
        lo que indica posibles asimetrías en la distribución.
        """)

    # =========================================================
    # 4️⃣ FALTANTES
    # =========================================================
    with tabs[3]:

        nulos = analizador.valores_nulos()
        st.dataframe(nulos)

        fig, ax = plt.subplots(figsize=(8,4))
        nulos.plot(kind="bar", ax=ax)
        ax.set_title("Valores faltantes")
        st.pyplot(fig)

    # =========================================================
    # 5️⃣ NUMÉRICAS
    # =========================================================
    with tabs[4]:

        numericas, _ = analizador.clasificar_variables()
        variable = st.selectbox("Seleccione variable numérica", numericas)

        st.pyplot(analizador.histograma(variable))

    # =========================================================
    # 6️⃣ CATEGÓRICAS
    # =========================================================
    with tabs[5]:

        _, categoricas = analizador.clasificar_variables()
        variable = st.selectbox("Seleccione variable categórica", categoricas)

        st.pyplot(analizador.grafico_categorico(variable))

        proporciones = df[variable].value_counts(normalize=True) * 100
        st.write("Proporciones (%)")
        st.dataframe(proporciones)

    # =========================================================
    # 7️⃣ NUM VS CAT
    # =========================================================
    with tabs[6]:

        variable = st.selectbox("Variable numérica vs resultado", numericas)

        st.pyplot(analizador.boxplot(variable))
        st.write("Comparación de medias por grupo:")
        st.dataframe(df.groupby("y")[variable].mean())

    # =========================================================
    # 8️⃣ CAT VS CAT
    # =========================================================
    with tabs[7]:

        variable = st.selectbox("Variable categórica vs resultado", categoricas)

        tabla = pd.crosstab(df[variable], df["y"], normalize="index") * 100
        st.dataframe(tabla)

    # =========================================================
    # 9️⃣ DINÁMICO
    # =========================================================
    with tabs[8]:

        edad_min, edad_max = st.slider(
            "Rango de edad",
            int(df["edad"].min()),
            int(df["edad"].max()),
            (25, 60)
        )

        trabajos = st.multiselect(
            "Filtrar por tipo de trabajo",
            df["job"].unique()
        )

        df_filtrado = df[
            (df["edad"] >= edad_min) &
            (df["edad"] <= edad_max)
        ]

        if trabajos:
            df_filtrado = df_filtrado[df_filtrado["job"].isin(trabajos)]

        tasa = df_filtrado["y"].value_counts(normalize=True) * 100
        st.metric("Tasa aceptación YES (%)",
                  round(tasa.get("yes", 0), 2))

        if st.checkbox("Mostrar matriz de correlación"):
            fig, ax = plt.subplots(figsize=(10,6))
            sns.heatmap(df_filtrado.corr(numeric_only=True),
                        cmap="coolwarm",
                        ax=ax)
            st.pyplot(fig)

    # =========================================================
    # 🔟 HALLAZGOS
    # =========================================================
    with tabs[9]:

        tasa_total = analizador.tasa_aceptacion()

        st.metric("Tasa aceptación YES (%)",
                  round(tasa_total.get("yes", 0), 2))

        fig, ax = plt.subplots(figsize=(6,4))
        tasa_total.plot(kind="bar", ax=ax)
        ax.set_title("Resumen aceptación campaña")
        st.pyplot(fig)

        st.markdown("""
        La duración de la llamada presenta fuerte relación con la aceptación.
        Se recomienda priorizar segmentos con mayor conversión histórica.
        """)


# ============================================================
# CONCLUSIONES FINALES
# ============================================================

elif menu == "📌 Conclusiones":

    st.title("📌 Conclusiones Finales")

    st.markdown("""
    ### 1️⃣ Impacto de la duración del contacto
    El análisis evidencia que los clientes que aceptan la campaña presentan mayor
    duración promedio de llamada. Esto sugiere que una interacción más prolongada
    incrementa la probabilidad de conversión.
    
    **Decisión:** fortalecer técnicas de comunicación y cierre comercial.
    """)

    st.markdown("""
    ### 2️⃣ Canal de contacto más efectivo
    Se observan diferencias en tasas de aceptación según el canal utilizado,
    destacando el canal celular con mejor desempeño.
    
    **Decisión:** priorizar el contacto vía celular en futuras campañas.
    """)

    st.markdown("""
    ### 3️⃣ Segmentación por perfil laboral
    Existen variaciones en la aceptación según el tipo de trabajo del cliente,
    lo que evidencia oportunidades de segmentación estratégica.
    
    **Decisión:** diseñar campañas focalizadas en perfiles con mayor conversión.
    """)

    st.markdown("""
    ### 4️⃣ Influencia del rango etario
    Determinados grupos de edad presentan mayor tasa de respuesta positiva.
    
    **Decisión:** orientar recursos comerciales hacia segmentos etarios
    con mejor desempeño histórico.
    """)

    st.markdown("""
    ### 5️⃣ Contexto económico
    Variables macroeconómicas muestran relación con el comportamiento del cliente,
    lo que sugiere que el entorno influye en la decisión final.
    
    **Decisión:** considerar el contexto económico al planificar campañas futuras.
    """)