import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ============================================================
# CONFIGURACION GENERAL
# ============================================================
st.set_page_config(
    page_title="Bank Marketing EDA",
    layout="wide",
    page_icon="📊"
)

# ============================================================
# DICCIONARIO DE ALIAS ENTENDIBLES
# ============================================================
column_alias = {
    "age": "Edad (Años)",
    "job": "Tipo de Trabajo",
    "marital": "Estado Civil",
    "education": "Nivel Educativo",
    "default": "¿Tiene Crédito en Mora?",
    "housing": "¿Tiene Crédito Hipotecario?",
    "loan": "¿Tiene Crédito Personal?",
    "contact": "Canal de Contacto",
    "month": "Mes del Último Contacto",
    "day_of_week": "Día del Último Contacto",
    "duration": "Duración de la Llamada (segundos)",
    "campaign": "Número de Contactos en la Campaña",
    "pdays": "Días desde Último Contacto",
    "previous": "Contactos Previos",
    "poutcome": "Resultado Campaña Anterior",
    "emp.var.rate": "Tasa Variación del Empleo",
    "cons.price.idx": "Índice Precio Consumidor",
    "cons.conf.idx": "Índice Confianza Consumidor",
    "euribor3m": "Tasa Euribor 3 Meses",
    "nr.employed": "Número de Empleados",
    "y": "Aceptó la Campaña"
}

alias_to_column = {v: k for k, v in column_alias.items()}

# ============================================================
# CLASE POO
# ============================================================
class DataAnalyzer:

    def __init__(self, df):
        self.df = df

    def classify_variables(self):
        num_vars = self.df.select_dtypes(include=np.number).columns.tolist()
        cat_vars = self.df.select_dtypes(exclude=np.number).columns.tolist()
        return num_vars, cat_vars

    def descriptive_stats(self):
        return self.df.describe()

    def null_values(self):
        return self.df.isnull().sum()

    def acceptance_rate(self):
        return (self.df["y"].value_counts(normalize=True) * 100)

# ============================================================
# SIDEBAR
# ============================================================
st.sidebar.title("📊 Navegación")
menu = st.sidebar.radio(
    "Ir a:",
    ["🏠 Home", "📂 Carga de Datos", "📊 Análisis EDA", "📌 Conclusiones"]
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
    Analizar los factores que influyen en la aceptación de campañas bancarias.
    """)

    st.markdown("""
    **Autor:** Ronaldinho Agricio Villalobos Torres  
    Especialización Python for Analytics - 2026
    """)

    st.markdown("### 🛠 Herramientas")
    st.success("Python")
    st.info("Pandas / NumPy")
    st.warning("Streamlit / Plotly")

# ============================================================
# CARGA
# ============================================================
elif menu == "📂 Carga de Datos":

    uploaded_file = st.file_uploader("Sube el archivo BankMarketing.csv", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, sep=";")
        st.session_state["df"] = df

        st.success("Archivo cargado correctamente ✅")

        df_alias = df.rename(columns=column_alias)
        st.dataframe(df_alias.head())

        col1, col2 = st.columns(2)
        col1.metric("Filas", df.shape[0])
        col2.metric("Columnas", df.shape[1])

    else:
        st.warning("Debe cargar el archivo.")

# ============================================================
# EDA COMPLETO
# ============================================================
elif menu == "📊 Análisis EDA":

    if "df" not in st.session_state:
        st.warning("Primero cargue el dataset.")
        st.stop()

    df = st.session_state["df"]
    analyzer = DataAnalyzer(df)
    df_alias = df.rename(columns=column_alias)

    st.title("📊 Análisis Exploratorio Completo")

    tabs = st.tabs([
        "1️⃣ Información General",
        "2️⃣ Distribuciones Numéricas",
        "3️⃣ Variables Categóricas",
        "4️⃣ Análisis Bivariado",
        "5️⃣ Análisis Dinámico"
    ])

    # ------------------------------------------------ TAB 1
    with tabs[0]:
        st.subheader("Resumen del Dataset")

        col1, col2 = st.columns(2)
        col1.dataframe(df.dtypes)
        col2.dataframe(analyzer.null_values())

        st.write("Estadísticas descriptivas")
        st.dataframe(analyzer.descriptive_stats())

        st.write("Tasa de aceptación (%)")
        st.dataframe(analyzer.acceptance_rate())

    # ------------------------------------------------ TAB 2
    with tabs[1]:
        num_vars, _ = analyzer.classify_variables()
        alias_numericos = [column_alias[col] for col in num_vars]

        var_alias = st.selectbox("Selecciona variable numérica", alias_numericos)
        fig = px.histogram(
            df_alias,
            x=var_alias,
            color="Aceptó la Campaña",
            marginal="box"
        )
        st.plotly_chart(fig, use_container_width=True)

    # ------------------------------------------------ TAB 3
    with tabs[2]:
        _, cat_vars = analyzer.classify_variables()
        alias_cat = [column_alias[col] for col in cat_vars if col != "y"]

        var_alias = st.selectbox("Selecciona variable categórica", alias_cat)

        fig = px.histogram(
            df_alias,
            x=var_alias,
            color="Aceptó la Campaña",
            barmode="group"
        )
        st.plotly_chart(fig, use_container_width=True)

    # ------------------------------------------------ TAB 4
    with tabs[3]:
        st.subheader("Numérico vs Aceptación")

        num_vars, _ = analyzer.classify_variables()
        alias_numericos = [column_alias[col] for col in num_vars]

        var_alias = st.selectbox("Variable numérica", alias_numericos, key="bivariado")

        fig = px.box(
            df_alias,
            x="Aceptó la Campaña",
            y=var_alias
        )
        st.plotly_chart(fig, use_container_width=True)

    # ------------------------------------------------ TAB 5
    with tabs[4]:
        st.subheader("Filtros Interactivos")

        edad_min, edad_max = st.slider(
            "Rango Edad",
            int(df["age"].min()),
            int(df["age"].max()),
            (25, 60)
        )

        df_filtrado = df_alias[
            (df_alias["Edad (Años)"] >= edad_min) &
            (df_alias["Edad (Años)"] <= edad_max)
        ]

        fig = px.histogram(
            df_filtrado,
            x="Edad (Años)",
            color="Aceptó la Campaña"
        )
        st.plotly_chart(fig, use_container_width=True)

# ============================================================
# CONCLUSIONES
# ============================================================
elif menu == "📌 Conclusiones":

    st.title("📌 Conclusiones")

    st.markdown("""
    1. La duración del contacto tiene fuerte impacto.
    2. Determinados perfiles laborales aceptan más.
    3. El canal de contacto influye en el resultado.
    4. La edad muestra patrones interesantes.
    5. Factores económicos presentan correlación.
    """)