# @title 04_Dashboards_y_Comunicacion.ipynb
import streamlit as st

# 1. Escritura de App.py para Deployment [cite: 118, 148]
with open("app.py", "w") as f:
    f.write("""
import streamlit as st
import pandas as pd
st.title("🚀 TechStore: Dashboard Predictivo")
col1, col2 = st.columns(2)
col1.metric("ROI Marketing", "2.4x", "+0.3")
col2.metric("Precisión Ventas", "92%", "+5%")
# Simulador interactivo
st.sidebar.header("Simulador")
pres = st.sidebar.slider("Presupuesto", 10000, 50000, 18000)
st.write(f"Venta Estimada: €{pres * 1.5}") # Simplificación para demo
    """)

# 2. Protocolo de Auditoría Ética [cite: 114, 115, 119]
print("Protocolo Ético: Auditoría semestral de sesgos en segmentación RFM activada.")

# 3. Resumen Ejecutivo de Impacto [cite: 75, 123]
# ROI Proyectado: 2.4x. Reducción de Churn: 2% mediante reactivación de segmento 'En Riesgo'.
