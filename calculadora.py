from IPython.display import display, HTML

# --- CSS SUPER ELEGANTE ---
fancy_style = """
<style>
    .credit-container {
        background: linear-gradient(135deg, #f8fafc 0%, #eef2f3 100%);
        border-radius: 20px;
        padding: 35px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.12);
        max-width: 900px;
        margin: 30px auto;
        font-family: 'Segoe UI', sans-serif;
        animation: fadeIn 1s ease-in-out;
    }
    h1 {
        text-align: center;
        color: #1A5276;
        font-size: 2.5em;
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        color: #566573;
        margin-bottom: 25px;
        font-size: 1.05em;
    }
    .result-box {
        background-color: white;
        border-radius: 15px;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.1);
        padding: 20px;
        margin-top: 20px;
        font-size: 1.1em;
        opacity: 0;
        transform: translateY(10px);
        animation: slideFade 0.8s forwards;
    }
    button {
        transition: all 0.3s ease-in-out;
    }
    button:hover {
        transform: scale(1.05);
        background-color: #138d75 !important;
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(-20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    @keyframes slideFade {
        to {opacity: 1; transform: translateY(0);}
    }
</style>
"""
display(HTML(fancy_style))

# --- CONTENEDOR PRINCIPAL ---
display(HTML("<div class='credit-container'><h1>💰 CREDIT GLOBAL CALCULATOR</h1><p class='subtitle'>Simula y compara créditos en México, Colombia, Brasil, EUA y Chile</p></div>"))

# --- WIDGETS ---
tipo_credito = widgets.Dropdown(
    options=['🚗 Automotriz', '🏡 Hipotecario', '💳 Personal'],
    description='Tipo:',
    style={'description_width': '80px'}
)

plazo = widgets.IntSlider(
    value=12, min=6, max=360, step=6,
    description='Plazo:',
    style={'description_width': '80px'}
)

pais = widgets.Dropdown(
    options=['🇲🇽 México', '🇨🇴 Colombia', '🇧🇷 Brasil', '🇺🇸 EUA', '🇨🇱 Chile'],
    description='País:',
    style={'description_width': '80px'}
)

tipo_tasa = widgets.ToggleButtons(
    options=['Fija', 'Variable'],
    description='Tasa:',
    style={'description_width': '80px'},
    button_style='' # dejar neutro para usar estilo CSS
)

monto_credito = widgets.FloatText(
    value=50000,
    description='Monto:',
    style={'description_width': '80px'}
)

btn_simular = widgets.Button(
    description='✨ Simular Crédito',
    button_style='success',
    layout=widgets.Layout(width='70%', margin='25px auto 0px auto')
)

output = widgets.Output()

# --- COLORES DINÁMICOS POR PAÍS ---
colores_pais = {
    '🇲🇽 México': '#2ECC71',    # Verde
    '🇨🇴 Colombia': '#F1C40F',  # Amarillo
    '🇧🇷 Brasil': '#1ABC9C',    # Verde agua
    '🇺🇸 EUA': '#3498DB',       # Azul
    '🇨🇱 Chile': '#E74C3C'      # Rojo
}

# --- FUNCIÓN DE SIMULACIÓN ---
def simular_credito(b):
    with output:
        output.clear_output()
        color = colores_pais.get(pais.value, "#1abc9c")
        display(HTML(f"""
        <div class="result-box" style="border-left: 8px solid {color};">
        <h3 style="color:{color}; margin-top:0;">✅ Simulación creada con éxito</h3>
        <ul style="list-style:none; padding-left:0; line-height:1.8;">
            <li><b>Tipo de crédito:</b> {tipo_credito.value}</li>
            <li><b>Plazo:</b> {plazo.value} meses</li>
            <li><b>País:</b> {pais.value}</li>
            <li><b>Tasa:</b> {tipo_tasa.value}</li>
            <li><b>Monto:</b> ${monto_credito.value:,.2f}</li>
        </ul>
        </div>
        """))

btn_simular.on_click(simular_credito)

# --- ORGANIZACIÓN EN COLUMNS ---
columna_izq = widgets.VBox([tipo_credito, plazo, pais, tipo_tasa])
columna_der = widgets.VBox([monto_credito])
display(widgets.HBox([columna_izq, columna_der]))
display(btn_simular, output)

# archivo: app.py
import streamlit as st

st.set_page_config(page_title="Credit Global Calculator", layout="wide")

# ---------------------------
# CSS súper elegante
# ---------------------------
fancy_style = """
<style>
.credit-container {
    background: linear-gradient(135deg, #f8fafc 0%, #eef2f3 100%);
    border-radius: 20px;
    padding: 35px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.12);
    max-width: 900px;
    margin: 30px auto;
    font-family: 'Segoe UI', sans-serif;
    text-align:center;
}
h1 {
    color: #1A5276;
    font-size: 2.5em;
    margin-bottom: 5px;
}
.subtitle {
    color: #566573;
    margin-bottom: 25px;
    font-size: 1.05em;
}
.result-box {
    background-color: white;
    border-radius: 15px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.1);
    padding: 20px;
    margin-top: 20px;
    font-size: 1.1em;
}
</style>
"""
st.markdown(fancy_style, unsafe_allow_html=True)

# ---------------------------
# Contenedor principal
# ---------------------------
st.markdown("""
<div class='credit-container'>
    <h1>💰 CREDIT GLOBAL CALCULATOR</h1>
    <p class='subtitle'>Simula y compara créditos en México, Colombia, Brasil, EUA y Chile</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Widgets Streamlit
# ---------------------------
tipo_credito = st.selectbox(
    "Tipo de crédito:",
    ['🚗 Automotriz', '🏡 Hipotecario', '💳 Personal']
)

plazo = st.slider(
    "Plazo (meses):",
    min_value=6, max_value=360, step=6, value=12
)

pais = st.selectbox(
    "País:",
    ['🇲🇽 México', '🇨🇴 Colombia', '🇧🇷 Brasil', '🇺🇸 EUA', '🇨🇱 Chile']
)

tipo_tasa = st.radio(
    "Tipo de tasa:",
    ['Fija', 'Variable']
)

monto_credito = st.number_input(
    "Monto del crédito:",
    min_value=1000.0, value=50000.0, step=1000.0, format="%.2f"
)

# ---------------------------
# Colores dinámicos por país
# ---------------------------
colores_pais = {
    '🇲🇽 México': '#2ECC71',    # Verde
    '🇨🇴 Colombia': '#F1C40F',  # Amarillo
    '🇧🇷 Brasil': '#1ABC9C',    # Verde agua
    '🇺🇸 EUA': '#3498DB',       # Azul
    '🇨🇱 Chile': '#E74C3C'      # Rojo
}

# ---------------------------
# Botón Simular
# ---------------------------
if st.button("✨ Simular Crédito"):
    color = colores_pais.get(pais, "#1abc9c")
    st.markdown(f"""
    <div class='result-box' style='border-left: 8px solid {color};'>
        <h3 style='color:{color}; margin-top:0;'>✅ Simulación creada con éxito</h3>
        <ul style='list-style:none; padding-left:0; line-height:1.8;'>
            <li><b>Tipo de crédito:</b> {tipo_credito}</li>
            <li><b>Plazo:</b> {plazo} meses</li>
            <li><b>País:</b> {pais}</li>
            <li><b>Tasa:</b> {tipo_tasa}</li>
            <li><b>Monto:</b> ${monto_credito:,.2f}</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    

