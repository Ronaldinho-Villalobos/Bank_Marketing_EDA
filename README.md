# 🏦 advanced-bank-marketing-analytics-dashboard
## 📊 Advanced Exploratory Data Analysis with Streamlit

---

## 📝 Descripción

Aplicación analítica desarrollada con **Streamlit** que implementa un Análisis Exploratorio de Datos (EDA) completo y profesional sobre el dataset de campañas de marketing bancario.

Este proyecto no se enfoca en predicción, sino en **análisis estratégico para la toma de decisiones**, utilizando métricas estadísticas, comparación de grupos y visualizaciones dinámicas.

Se aplican principios de:

- ✅ Python Fundamentals  
- ✅ Análisis Exploratorio de Datos (EDA) estructurado  
- ✅ Programación Orientada a Objetos (POO)  
- ✅ Visualización estadística con Matplotlib y Seaborn  
- ✅ Dashboards interactivos con Streamlit  
- ✅ Enfoque analítico orientado a negocio  

---

## 🎯 Objetivo del Proyecto

Identificar patrones y variables clave que influyen en la aceptación de campañas de marketing bancario.

El análisis busca:

- Comprender el comportamiento del cliente  
- Detectar variables influyentes en la conversión  
- Analizar diferencias entre grupos  
- Evaluar impacto de variables demográficas y económicas  
- Generar conclusiones estratégicas basadas en evidencia  

---

## 🧱 Estructura del Proyecto

```
advanced-bank-marketing-analytics-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── BankMarketing.csv
```

---

## 🧠 Arquitectura del Sistema

El proyecto implementa **Programación Orientada a Objetos (POO)** para estructurar el análisis.

Clase principal:

```python
class DataAnalyzer:

    def clasificar_variables(self):
        """Identifica variables numéricas y categóricas"""
        pass

    def estadisticas_descriptivas(self):
        """Genera resumen estadístico (.describe())"""
        pass

    def mediana(self):
        """Calcula mediana de variables numéricas"""
        pass

    def moda(self):
        """Calcula moda cuando aplica"""
        pass

    def valores_nulos(self):
        """Conteo de valores faltantes"""
        pass

    def tasa_aceptacion(self):
        """Calcula porcentaje de aceptación"""
        pass

    def histograma(self, columna):
        """Visualización de distribución con media y mediana"""
        pass

    def boxplot(self, columna):
        """Comparación numérica vs variable objetivo"""
        pass

    def grafico_categorico(self, columna):
        """Frecuencias de variable categórica"""
        pass
```

La clase encapsula:

- Clasificación de variables  
- Estadísticas descriptivas  
- Medidas de tendencia central (media, mediana, moda)  
- Análisis de valores faltantes  
- Visualizaciones estadísticas  

---

## 📊 Funcionalidades del Dashboard

### 🏠 1. Home
- Presentación del proyecto  
- Objetivo del análisis  
- Imagen representativa  
- Información del autor  
- Tecnologías utilizadas  

---

### 📂 2. Carga de Datos
- Subida dinámica de archivo CSV  
- Vista previa del dataset  
- Métricas generales (filas y columnas)  
- Renombrado de variables técnicas a nombres más entendibles (ej: `age → edad`)  

---

### 📊 3. Análisis Exploratorio Completo (EDA)

El sistema implementa 10 módulos analíticos organizados en pestañas.

---

### 1️⃣ Información General
- `.info()` mostrado en panel expandible  
- Tipos de datos organizados en tabla  
- Conteo de valores nulos  
- Visualización de faltantes  
- Métricas generales del dataset  

---

### 2️⃣ Clasificación de Variables
- Identificación automática de:
  - Variables numéricas  
  - Variables categóricas  
- Conteo de cada grupo  
- Visualización clara y estructurada  

---

### 3️⃣ Estadísticas Descriptivas
- `.describe()` completo  
- Media  
- Mediana  
- Moda  
- Interpretación básica de dispersión y asimetría  

---

### 4️⃣ Análisis de Valores Faltantes
- Conteo por variable  
- Visualización en gráfico de barras  
- Discusión interpretativa  

---

### 5️⃣ Distribución de Variables Numéricas
- Histogramas con curva KDE  
- Línea de media y mediana  
- Interpretación visual  
- Detección de asimetrías  

---

### 6️⃣ Análisis de Variables Categóricas
- Conteo de frecuencias  
- Gráficos de barras  
- Proporciones porcentuales  
- Interpretación comparativa  

---

### 7️⃣ Análisis Bivariado (Numérico vs Categórico)
Ejemplos:
- Edad vs Aceptación  
- Duración de llamada vs Aceptación  

Incluye:
- Boxplots comparativos  
- Comparación de medias por grupo  
- Identificación de diferencias significativas  

---

### 8️⃣ Análisis Bivariado (Categórico vs Categórico)
Ejemplos:
- Educación vs Aceptación  
- Canal de contacto vs Aceptación  

Incluye:
- Tablas cruzadas normalizadas  
- Comparación porcentual por grupo  

---

### 9️⃣ Análisis Dinámico
Uso obligatorio de widgets:

- `st.selectbox`  
- `st.multiselect`  
- `st.slider`  
- `st.checkbox`  
- `st.columns`  
- `st.sidebar`  
- `st.tabs`  

Permite:

- Filtrar por rango de edad  
- Segmentar por tipo de trabajo  
- Visualizar tasa de aceptación dinámica  
- Mostrar matriz de correlación opcional  

---

### 🔟 Hallazgos Clave
- Tasa general de aceptación  
- Visualización resumen  
- Insights derivados del análisis  
- Enfoque estratégico  

---

## 📈 Variables Analizadas

Incluye variables como:

- Edad  
- Tipo de Trabajo  
- Estado Civil  
- Nivel Educativo  
- Duración de la llamada  
- Número de contactos  
- Días desde último contacto  
- Indicadores económicos  
- Resultado de campaña anterior  

---

## 📊 Conceptos Estadísticos Aplicados

- Media  
- Mediana  
- Moda  
- Distribución  
- Comparación de grupos  
- Proporciones  
- Asimetría  
- Relación entre variables  

---

## 🛠️ Tecnologías Utilizadas

- Python 3.x  
- Streamlit  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  

---

## ⚙️ Instalación

Clona el repositorio:

```bash
git clone https://github.com/tuusuario/advanced-bank-marketing-analytics-dashboard.git
```

Instala dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución

Desde la carpeta del proyecto:

```bash
streamlit run app.py
```

---

## 📌 Resultados Estratégicos

El análisis permite concluir que:

- La duración del contacto tiene fuerte relación con la conversión.
- Existen diferencias significativas según perfil laboral.
- El canal de contacto influye en la tasa de aceptación.
- Determinados rangos etarios presentan mayor respuesta positiva.
- Variables macroeconómicas muestran relación con el comportamiento del cliente.

El proyecto está orientado a **mejorar la toma de decisiones comerciales**, no a generar modelos predictivos.

---

## 🏆 Habilidades Demostradas

- Estructuración profesional de EDA  
- Diseño de dashboard interactivo  
- Arquitectura basada en clases (POO)  
- Interpretación estadística  
- Visualización clara y ejecutiva  
- Desarrollo orientado a negocio  

---

## ✍️ Autor

**Ronaldinho Agricio Villalobos Torres**  
Especialización en Python & Data Analytics – 2026  

---
