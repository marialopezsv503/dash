import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# 1. Configuración de la página (opcional) ahora
st.set_page_config(page_title='Mi Dashboard', layout='wide')

# 2. Cargar o generar datos (ejemplo con datos aleatorios)
np.random.seed(42)
df = pd.DataFrame({
    'Fecha': pd.date_range('2024-01-01', periods=100),
    'Ventas': np.random.randint(500, 2000, size=100),
    'Region': np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], size=100),
    'Producto': np.random.choice(['Producto A', 'Producto B', 'Producto C'], size=100)
})

# 3. Filtros en la barra lateral
st.sidebar.title('Filtros')
regiones_seleccionadas = st.sidebar.multiselect('Selecciona Región', df['Region'].unique(), default=df['Region'].unique())
productos_seleccionados = st.sidebar.multiselect('Selecciona Producto', df['Producto'].unique(), default=df['Producto'].unique())

# 4. Aplicar filtros a los datos
datos_filtrados = df[(df['Region'].isin(regiones_seleccionadas)) & (df['Producto'].isin(productos_seleccionados))]

# 5. Mostrar métricas principales (en columnas)
col1, col2, col3 = st.columns(3)
col1.metric("Ventas Totales", f"${datos_filtrados['Ventas'].sum():,}")
col2.metric("Ventas Promedio", f"${datos_filtrados['Ventas'].mean():.0f}")
col3.metric("Número de Registros", len(datos_filtrados))

# 6. Crear y mostrar gráficos con Plotly (en dos columnas)
col1, col2 = st.columns(2)

with col1:
    fig_line = px.line(datos_filtrados, x='Fecha', y='Ventas', color='Region', title='Ventas a lo largo del tiempo')
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    ventas_por_region = datos_filtrados.groupby('Region')['Ventas'].sum().reset_index()
    fig_bar = px.bar(ventas_por_region, x='Region', y='Ventas', title='Ventas Totales por Región')
    st.plotly_chart(fig_bar, use_container_width=True)


## Poniendo color de fondo y config de barra superior
st.set_page_config(
    page_title="Mi Dashboard de Ventas",  
    page_icon="📊",  
    layout="wide",  
    initial_sidebar_state="expanded"  
)

st.markdown("""
<style>
.stApp {
    background-color: #f3f1ac 
}
</style>
""", unsafe_allow_html=True)

# 7. Mostrar los datos filtrados en una tabla
st.subheader("Datos Filtrados")
st.dataframe(datos_filtrados)