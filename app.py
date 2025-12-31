import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="TechStore Predictivo",
    page_icon="🚀",
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True) # CORREGIDO: de stdio a html

# --- TÍTULO Y HEADER ---
st.title("🚀 TechStore: Sistema de Analytics Predictivo")
st.markdown("### Panel de Control Ejecutivo y Simulador de Estrategia")
st.info("Plataforma integral para la optimización de ventas y segmentación de clientes.")

# --- SECCIÓN 1: KPIs PRINCIPALES ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Precisión (R²)", "92%", "+5% vs Q3")
with col2:
    st.metric("ROI Marketing", "2.4x", "Óptimo")
with col3:
    st.metric("Tasa de Churn", "12%", "-2% vs 2024")
with col4:
    st.metric("Clientes Activos", "2,000", "Base Fiel")

st.markdown("---")

# --- SECCIÓN 2: SIMULADOR DE ESCENARIOS (FASE 4) ---
st.sidebar.header("🛠️ Configuración de Escenarios")
st.sidebar.markdown("Ajuste los parámetros para ver el impacto en tiempo real.")

presupuesto = st.sidebar.slider("Inversión Marketing (€)", 10000, 50000, 18000)
cambio_precio = st.sidebar.slider("Variación de Precio (%)", -20, 20, 0)

# Lógica del simulador (Basada en Fase 2)
venta_base = 150000
impacto_mkt = (presupuesto - 18000) * 0.45
elasticidad = -1.8  # Sensibilidad promedio
ajuste_precio = 1 + (cambio_precio / 100 * elasticidad)
proyeccion = (venta_base + impacto_mkt) * ajuste_precio

c1, c2 = st.columns([2, 1])

with c1:
    st.subheader("📊 Proyección de Ventas Mensuales")
    # Generar un gráfico de tendencia simple
    meses = ['Mes Actual', 'Proyección']
    valores = [venta_base, proyeccion]
    fig_ventas = px.bar(x=meses, y=valores, color=meses, 
                        labels={'x': 'Escenario', 'y': 'Ventas (€)'},
                        color_discrete_sequence=['#AEC6CF', '#1a5fb4'])
    st.plotly_chart(fig_ventas, use_container_width=True)

with c2:
    st.subheader("💰 Resultado")
    st.write(f"Con los ajustes seleccionados, la venta proyectada es de:")
    st.header(f"€{proyeccion:,.2f}")
    diferencia = proyeccion - venta_base
    color = "green" if diferencia >= 0 else "red"
    st.markdown(f"<p style='color:{color}; font-size:20px;'><b>Impacto: €{diferencia:,.2f}</b></p>", unsafe_allow_html=True)

# --- SECCIÓN 3: SEGMENTACIÓN (FASE 3) ---
st.markdown("---")
st.subheader("👥 Distribución de Segmentos de Clientes")

df_segmentos = pd.DataFrame({
    'Segmento': ['VIP', 'En Riesgo', 'Potencial', 'Nuevos'],
    'Cantidad': [450, 240, 600, 710],
    'ROI': [4.5, 2.1, 3.2, 1.8]
})

fig_pie = px.pie(df_segmentos, values='Cantidad', names='Segmento', hole=0.4,
                 color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig_pie, use_container_width=True)

# --- PIE DE PÁGINA ---
st.sidebar.markdown("---")
st.sidebar.caption("⚖️ Protocolo de Auditoría Ética Activo")
st.sidebar.caption("TechStore Analytics © 2025")
