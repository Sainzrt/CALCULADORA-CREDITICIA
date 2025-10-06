import streamlit as st

st.write("hello")
# archivo: app.py
import streamlit as st
import requests
import base64
from io import BytesIO

st.set_page_config(page_title="Simulador Global de Créditos", layout="wide")

# ---------------------------
# Helper: descargar imagen y transformar a bytes
# ---------------------------
def fetch_image_bytes(url):
    try:
        r = requests.get(url, timeout=8)
        r.raise_for_status()
        return r.content
    except Exception as e:
        print("No se pudo descargar:", url, "->", e)
        return None

# ---------------------------
# Logos
# ---------------------------
logos_urls = {
    "Banxico": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Banxico_logo.svg/512px-Banxico_logo.svg.png",
    "Federal Reserve": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Federal_Reserve_seal.svg/512px-Federal_Reserve_seal.svg.png",
    "Banco de la República (COL)": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Banco_de_la_Republica_Colombia_logo.svg/512px-Banco_de_la_Republica_Colombia_logo.svg.png",
    "Banco Central de Chile": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Banco_Central_de_Chile_logo.svg/512px-Banco_Central_de_Chile_logo.svg.png",
    "Banco Central do Brasil": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Banco_Central_do_Brasil_logo.svg/512px-Banco_Central_do_Brasil_logo.svg.png"
}

logos_bytes = {}
for k, url in logos_urls.items():
    logos_bytes[k] = fetch_image_bytes(url)

# ---------------------------
# Pantalla de bienvenida
# ---------------------------
st.markdown(
    """
    <div style="background: linear-gradient(120deg, #0f1724 0%, #1f2a44 50%, #243b55 100%);
                color: #f7fbff; border-radius: 18px; padding: 28px; text-align:center;">
        <h1 style="font-size:34px; font-weight:700;">🌎 Bienvenido — Simulador Global de Créditos</h1>
        <p style="color: rgba(255,255,255,0.85); font-size:16px;">Tasas confiables, respaldadas por bancos centrales. Elige tu necesidad y te llevamos al simulador.</p>
    </div>
    """, unsafe_allow_html=True
)

# Mostrar logos en fila
cols = st.columns(len(logos_bytes))
for i, (name, b) in enumerate(logos_bytes.items()):
    if b:
        cols[i].image(b, use_column_width=True)
    else:
        cols[i].write(name)

st.markdown("<p style='text-align:center; color:rgba(0,0,0,0.6); font-size:13px;'>Los logos representan fuentes oficiales de referencia para tasas por país</p>", unsafe_allow_html=True)

# ---------------------------
# Opciones de crédito
# ---------------------------
options = [
    {"key":"auto","label":"Automotriz","emoji":"🚗","sub":"Compra de vehículo"},
    {"key":"hipo","label":"Hipotecario","emoji":"🏡","sub":"Compra de vivienda"},
    {"key":"deudas","label":"Reunificar deudas","emoji":"💳","sub":"Consolidar pagos"},
    {"key":"negocio","label":"Invertir en negocio","emoji":"📈","sub":"Capital para negocio"},
    {"key":"gastos","label":"Gastos personales","emoji":"🧾","sub":"Emergencias / personales"}
]

st.markdown("## ¿Para qué necesitas el crédito?")
selected_option = st.radio(
    "Elige tu opción:",
    options=[f"{opt['emoji']} {opt['label']} - {opt['sub']}" for opt in options]
)

# ---------------------------
# Botones de acción
# ---------------------------
col1, col2 = st.columns([1,1])
with col1:
    if st.button("➡️ Ir al simulador"):
        # encontrar la opción seleccionada
        selected_label = next((o['label'] for o in options if f"{o['emoji']} {o['label']}" in selected_option), None)
        if selected_label:
            st.success(f"✨ Llevándote al simulador... Tu elección: {selected_label}")
        else:
            st.warning("⚠️ Por favor selecciona primero una opción.")

with col2:
    if st.button("🔄 Reiniciar"):
        st.experimental_rerun()
     ####