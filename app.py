# ============================================================
# IMPORTACIÓN DE LIBRERÍAS
# ============================================================
# Importamos las librerías necesarias para el proyecto.
# Streamlit -> para crear la app web interactiva
# Pandas -> manejo de datos
# NumPy -> operaciones numéricas
# Matplotlib y Seaborn -> visualización
# io -> para capturar info técnica del dataframe

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================
# Aqui configuramos la pagina principal del dashboard.
# Si se quiere cambiar el titulo o el icono se modifica aki.

st.set_page_config(
    page_title="Bank Marketing EDA",
    layout="wide",
    page_icon="📊"
)

# Configuración visual de gráficos (estética general)
# Esto mejora la apariencia para q no se vea simple o plano
sns.set_theme(style="whitegrid", palette="deep")

# ============================================================
# CLASE PRINCIPAL (POO)
# Aqui organizamos todo el analisis porque asi el codigo
# queda mas limpio y profesional (y no todo mezclado).
# Si se quiere agregar mas funciones estadisticas se hace aqui.
# ============================================================

class DataAnalyzer:

    def __init__(self, df):
        # Guardamos el dataframe dentro del objeto
        # asi todas las funciones pueden usarlo
        self.df = df

    # --------------------------------------------------------
    # Clasificación automática de variables
    # --------------------------------------------------------
    # Detecta cuales columnas son numericas y cuales no
    # Esto es util para separar graficos automaticamente
    def clasificar_variables(self):
        numericas = self.df.select_dtypes(include=np.number).columns.tolist()
        categoricas = self.df.select_dtypes(exclude=np.number).columns.tolist()
        return numericas, categoricas

    # --------------------------------------------------------
    # Estadísticas descriptivas básicas
    # --------------------------------------------------------
    # Describe devuelve conteo, media, std, min, max etc.
    def estadisticas_descriptivas(self):
        return self.df.describe()

    # Calcula mediana solo en columnas numericas
    def mediana(self):
        return self.df.median(numeric_only=True)

    # Obtiene la moda (valor más frecuente)
    def moda(self):
        return self.df.mode().iloc[0]

    # Cuenta valores nulos por columna
    def valores_nulos(self):
        return self.df.isnull().sum()

    # Calcula tasa de aceptación en porcentaje
    # Se basa en la variable objetivo "y"
    def tasa_aceptacion(self):
        return self.df["y"].value_counts(normalize=True) * 100

    # --------------------------------------------------------
    # Visualizaciones
    # --------------------------------------------------------

    # Histograma con media y mediana
    # Permite ver distribucion y posible asimetria
    def histograma(self, columna):
        fig, ax = plt.subplots(figsize=(8,5))

        sns.histplot(self.df[columna], kde=True, ax=ax)

        # Linea roja = media
        ax.axvline(self.df[columna].mean(),
                   color="red",
                   linestyle="--",
                   label="Media")

        # Linea verde = mediana
        ax.axvline(self.df[columna].median(),
                   color="green",
                   linestyle="-",
                   label="Mediana")

        ax.set_title(f"Distribución de {columna}")
        ax.legend()

        return fig

    # Boxplot comparando variable numerica vs resultado campaña
    # Sirve para ver diferencias entre yes y no
    def boxplot(self, columna):
        fig, ax = plt.subplots(figsize=(8,5))
        sns.boxplot(x=self.df["y"],
                    y=self.df[columna],
                    ax=ax)
        ax.set_title(f"{columna} vs Resultado de Campaña")
        return fig

    # Gráfico para variables categóricas
    # Cuenta frecuencia de cada categoría
    def grafico_categorico(self, columna):
        fig, ax = plt.subplots(figsize=(9,5))
        sns.countplot(x=self.df[columna], ax=ax)
        plt.xticks(rotation=45)
        ax.set_title(f"Distribución de {columna}")
        return fig


# ============================================================
# SIDEBAR (MENÚ LATERAL)
# ============================================================
# Desde aqui el usuario navega por las secciones

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

    # Imagen principal decorativa para mejor estetica
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

    # Permite subir archivo CSV
    archivo = st.file_uploader("Suba el archivo BankMarketing.csv", type=["csv"])

    if archivo:

        # Leemos archivo usando separador ;
        df = pd.read_csv(archivo, sep=";")

        # Renombramos algunas variables para que sean mas entendibles
        # Si se quiere agregar mas alias se hace aqui
        df = df.rename(columns={
            "age": "edad",
            "duration": "duracion_llamada",
            "campaign": "numero_contactos",
            "pdays": "dias_desde_ultimo_contacto",
            "previous": "contactos_previos"
        })

        # Guardamos dataset en memoria de sesión
        # Esto permite usarlo en otras pestañas sin volver a cargar
        st.session_state["df"] = df

        st.success("Archivo cargado correctamente.")

        st.dataframe(df.head())

        col1, col2 = st.columns(2)
        col1.metric("Filas", df.shape[0])
        col2.metric("Columnas", df.shape[1])

    else:
        st.warning("Debe cargar el archivo para continuar.")

# ============================================================
# ANÁLISIS EDA (10 TABS COMPLETOS)
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
    # 1️⃣ INFO GENERAL
    # =========================================================
    with tabs[0]:

        # Métricas generales del dataset
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

        # Esto muestra información técnica tipo consola
        # Sirve para ver memoria, tipos exactos, etc.
        with st.expander("Ver detalle técnico (.info())"):
            buffer = io.StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())

    # =========================================================
    # Las demás pestañas se mantienen EXACTAMENTE igual
    # Solo se agregaron comentarios explicativos arriba
    # =========================================================

    with tabs[1]:
        numericas, categoricas = analizador.clasificar_variables()
        col1, col2 = st.columns(2)
        col1.info(f"Variables numéricas: {len(numericas)}")
        col2.info(f"Variables categóricas: {len(categoricas)}")
        st.write("Lista numéricas:", numericas)
        st.write("Lista categóricas:", categoricas)

    with tabs[2]:
        st.dataframe(analizador.estadisticas_descriptivas())
        st.write("Mediana:")
        st.dataframe(analizador.mediana())
        st.write("Moda:")
        st.dataframe(analizador.moda())

    with tabs[3]:
        nulos = analizador.valores_nulos()
        st.dataframe(nulos)
        fig, ax = plt.subplots(figsize=(8,4))
        nulos.plot(kind="bar", ax=ax)
        st.pyplot(fig)

    with tabs[4]:
        numericas, _ = analizador.clasificar_variables()
        variable = st.selectbox("Seleccione variable numérica", numericas)
        st.pyplot(analizador.histograma(variable))

    with tabs[5]:
        _, categoricas = analizador.clasificar_variables()
        variable = st.selectbox("Seleccione variable categórica", categoricas)
        st.pyplot(analizador.grafico_categorico(variable))
        proporciones = df[variable].value_counts(normalize=True) * 100
        st.dataframe(proporciones)

    with tabs[6]:
        variable = st.selectbox("Variable numérica vs resultado", numericas)
        st.pyplot(analizador.boxplot(variable))
        st.dataframe(df.groupby("y")[variable].mean())

    with tabs[7]:
        variable = st.selectbox("Variable categórica vs resultado", categoricas)
        tabla = pd.crosstab(df[variable], df["y"], normalize="index") * 100
        st.dataframe(tabla)

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

    with tabs[9]:
        tasa_total = analizador.tasa_aceptacion()
        st.metric("Tasa aceptación YES (%)",
                  round(tasa_total.get("yes", 0), 2))
        fig, ax = plt.subplots(figsize=(6,4))
        tasa_total.plot(kind="bar", ax=ax)
        st.pyplot(fig)

# ============================================================
# CONCLUSIONES (SIN CAMBIAR TUS 5)
# ============================================================

elif menu == "📌 Conclusiones":

    st.title("📌 Conclusiones Finales")

    st.markdown("""
    ### 1️⃣ Impacto de la duración del contacto
    El análisis evidencia mayor duración promedio en clientes que aceptan.
    **Decisión:** fortalecer técnicas comerciales.

    ### 2️⃣ Canal de contacto
    Existen diferencias según canal utilizado.
    **Decisión:** priorizar canales más efectivos.

    ### 3️⃣ Perfil laboral
    Algunos trabajos presentan mayor conversión.
    **Decisión:** segmentación estratégica.

    ### 4️⃣ Edad
    Determinados rangos responden mejor.
    **Decisión:** enfocar recursos en segmentos más rentables.

    ### 5️⃣ Contexto económico
    Variables macroeconómicas influyen en comportamiento.
    **Decisión:** considerar entorno antes de lanzar campaña.
    """)