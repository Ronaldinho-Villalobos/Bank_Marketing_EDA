# 🏦 advanced-bank-marketing-analytics-dashboard  
## 📊 Advanced Exploratory Data Analysis Dashboard with Streamlit  

---

## 📝 Descripción

Aplicación analítica interactiva desarrollada con **Streamlit** que implementa un **Análisis Exploratorio de Datos (EDA) completo, estructurado y profesional** sobre el dataset Bank Marketing.

El proyecto está orientado a **análisis estratégico y toma de decisiones comerciales**, no a modelos predictivos.

Se integra:

- ✅ Python aplicado a Data Analytics  
- ✅ Programación Orientada a Objetos (POO)  
- ✅ Análisis Exploratorio estructurado en 10 módulos  
- ✅ Visualización estadística avanzada  
- ✅ Dashboard interactivo profesional  
- ✅ Segmentación dinámica con filtros  

---

## 🎯 Objetivo del Proyecto

Analizar los factores que influyen en la aceptación de campañas de marketing bancario, identificando:

- Variables con mayor impacto en la conversión  
- Diferencias entre grupos de clientes  
- Patrones demográficos relevantes  
- Influencia de variables económicas  
- Oportunidades estratégicas de segmentación  

El enfoque es **analítico–estratégico**, orientado a negocio.

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

## 🧠 Arquitectura del Sistema (POO)

El análisis está encapsulado dentro de una clase principal:

```python
class DataAnalyzer:

    def clasificar_variables(self):
        """Identifica variables numéricas y categóricas"""

    def estadisticas_descriptivas(self):
        """Resumen estadístico general"""

    def mediana(self):
        """Mediana para variables numéricas"""

    def moda(self):
        """Valor más frecuente"""

    def valores_nulos(self):
        """Conteo de valores faltantes"""

    def tasa_aceptacion(self):
        """Cálculo porcentual de aceptación"""

    def histograma(self, columna):
        """Distribución con KDE, media y mediana"""

    def boxplot(self, columna):
        """Comparación numérica vs resultado campaña"""

    def grafico_categorico(self, columna):
        """Frecuencia de variable categórica"""
```

### ✔️ Beneficios de la arquitectura

- Código modular y limpio  
- Fácil mantenimiento  
- Escalable para futuras mejoras  
- Separación entre lógica analítica y visualización  

---

## 📊 Funcionalidades del Dashboard

El sistema está organizado en un menú lateral con navegación completa.

---

## 🏠 1. Home

- Presentación del proyecto  
- Objetivo del análisis  
- Imagen representativa  
- Información del autor  
- Tecnologías utilizadas  

---

## 📂 2. Carga de Datos

- Subida dinámica de archivo CSV  
- Lectura con separador `;`  
- Renombrado automático de variables técnicas:

| Original | Nuevo nombre |
|----------|-------------|
| age | edad |
| duration | duracion_llamada |
| campaign | numero_contactos |
| pdays | dias_desde_ultimo_contacto |
| previous | contactos_previos |

- Métricas de filas y columnas  
- Vista previa del dataset  
- Almacenamiento en `st.session_state` para persistencia  

---

## 📊 3. Análisis Exploratorio Completo (10 Tabs)

El EDA está estructurado en 10 módulos analíticos:

---

### 1️⃣ Información General

- Métricas generales del dataset  
- Tipos de datos organizados en tabla  
- Conteo total de valores nulos  
- Visualización de faltantes  
- `.info()` técnico en panel expandible  

---

### 2️⃣ Clasificación Automática

- Identificación automática de:
  - Variables numéricas  
  - Variables categóricas  
- Conteo por tipo  
- Listado detallado  

---

### 3️⃣ Estadísticas Descriptivas

Incluye:

- `.describe()` completo  
- Mediana  
- Moda  
- Comparación de tendencia central  
- Análisis de dispersión  

---

### 4️⃣ Análisis de Valores Faltantes

- Conteo por variable  
- Visualización en gráfico de barras  
- Evaluación estructural del dataset  

---

### 5️⃣ Distribución de Variables Numéricas

- Histogramas con KDE  
- Línea de media (roja)  
- Línea de mediana (verde)  
- Detección visual de asimetrías  

---

### 6️⃣ Variables Categóricas

- Conteo de frecuencias  
- Gráficos de barras  
- Proporciones porcentuales  
- Comparación de categorías  

---

### 7️⃣ Numérico vs Resultado (y)

- Boxplots comparativos  
- Comparación de medias por grupo  
- Identificación de diferencias significativas  

---

### 8️⃣ Categórico vs Resultado

- Tablas cruzadas normalizadas (%)  
- Comparación proporcional por categoría  
- Análisis de conversión segmentada  

---

### 9️⃣ Análisis Dinámico Interactivo

Implementa widgets:

- `st.slider`
- `st.multiselect`
- `st.selectbox`
- `st.checkbox`
- `st.columns`
- `st.tabs`
- `st.sidebar`

Permite:

- Filtrar por rango de edad  
- Filtrar por tipo de trabajo  
- Calcular tasa de aceptación dinámica  
- Visualizar matriz de correlación opcional  
- Análisis segmentado en tiempo real  

---

### 🔟 Hallazgos Clave

- Tasa general de aceptación  
- Visualización resumen  
- Métrica estratégica principal  
- Insights finales ejecutivos  

---

## 📈 Variables Analizadas

- Edad  
- Tipo de trabajo  
- Estado civil  
- Educación  
- Duración de la llamada  
- Número de contactos  
- Contactos previos  
- Días desde último contacto  
- Variables macroeconómicas  
- Resultado de campaña anterior  
- Variable objetivo `y`  

---

## 📊 Conceptos Estadísticos Aplicados

- Media  
- Mediana  
- Moda  
- Distribución  
- Comparación de grupos  
- Análisis bivariado  
- Proporciones  
- Asimetría  
- Correlación  
- Segmentación dinámica  

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

```bash
git clone https://github.com/tuusuario/advanced-bank-marketing-analytics-dashboard.git
cd advanced-bank-marketing-analytics-dashboard
pip install -r requirements.txt
```

---

## ▶️ Ejecución

```bash
streamlit run app.py
```

---

## 📌 Resultados Estratégicos Derivados

El análisis evidencia que:

- La duración del contacto tiene fuerte relación con la conversión.
- Existen diferencias relevantes según perfil laboral.
- El canal de contacto influye en la tasa de aceptación.
- Determinados rangos etarios muestran mayor probabilidad de respuesta positiva.
- Variables económicas impactan el comportamiento del cliente.
- La segmentación mejora significativamente la interpretación estratégica.

---

## 🏆 Habilidades Demostradas

- Arquitectura basada en POO  
- Desarrollo de dashboards profesionales  
- EDA estructurado de nivel avanzado  
- Visualización ejecutiva  
- Análisis orientado a negocio  
- Manejo de estado en aplicaciones Streamlit  
- Segmentación dinámica de datos  

---

## ✍️ Autor

**Ronaldinho Agricio Villalobos Torres**  
Especialización en Python & Data Analytics – 2026  
