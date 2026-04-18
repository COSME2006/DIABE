import streamlit as st

st.set_page_config(page_title="Evaluación de Riesgo - Diabetes", layout="centered")

st.markdown(
    """
    <style>
    .main-title {
        font-size: 2rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        color: #334155;
        margin-bottom: 1rem;
    }
    .section-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1rem 1rem 0.4rem 1rem;
        margin-bottom: 1rem;
    }
    .medical-note {
        background-color: #ecfeff;
        border-left: 4px solid #0891b2;
        padding: 0.8rem;
        border-radius: 8px;
        color: #0f172a;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">🩺 Evaluación de Factores de Riesgo</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Modelo educativo - Diabetes Mellitus (Tipo 1 y Tipo 2)</div>', unsafe_allow_html=True)

st.write("Ingresa valores entre 0 y 1:")
st.write("0 = Sin riesgo | 1 = Riesgo máximo")

# Nombre
nombre = st.text_input("Nombre del paciente (opcional)")

# ==============================
# FACTORES BIOLÓGICOS
# ==============================
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.header("Factores Biológicos")

edad_risk = st.slider("Edad (>50 años)", 0.0, 1.0, 0.0)
genetic_risk = st.slider("Predisposición genética (antecedentes familiares)", 0.0, 1.0, 0.0)
base_metabolic = 0.10
st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# ESTILO DE VIDA
# ==============================
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.header("Estilo de Vida")

dieta = st.slider("Dieta (alto en azúcar/grasas)", 0.0, 1.0, 0.0)
actividad = st.slider("Actividad física (sedentarismo)", 0.0, 1.0, 0.0)
adherencia = st.slider("Adherencia terapéutica", 0.0, 1.0, 0.0)
estres = st.slider("Estrés", 0.0, 1.0, 0.0)
st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# FACTORES ADICIONALES
# ==============================
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.header("Factores Adicionales")

imc = st.slider("Índice de Masa Corporal (IMC)", 0.0, 1.0, 0.0)
alcohol = st.slider("Consumo de alcohol", 0.0, 1.0, 0.0)
tabaco = st.slider("Tabaquismo", 0.0, 1.0, 0.0)
presion = st.slider("Presión arterial elevada", 0.0, 1.0, 0.0)
st.markdown('</div>', unsafe_allow_html=True)

total_inputs = 10
completion_ratio = (
    edad_risk
    + genetic_risk
    + dieta
    + actividad
    + adherencia
    + estres
    + imc
    + alcohol
    + tabaco
    + presion
) / total_inputs
st.progress(completion_ratio, text=f"Nivel de riesgo global capturado: {completion_ratio * 100:.0f}%")

# ==============================
# BOTÓN DE RESULTADO
# ==============================
if st.button("Calcular resultados"):

    biological_factors = {
        'Genética': genetic_risk,
        'Edad': edad_risk,
        'Función Base': base_metabolic
    }

    lifestyle_factors = {
        'Dieta': dieta,
        'Actividad Física': actividad,
        'Adherencia': adherencia,
        'Estrés': estres,
        'IMC': imc,
        'Alcohol': alcohol,
        'Tabaquismo': tabaco,
        'Presión Arterial': presion
    }

    total_bio = sum(biological_factors.values())
    total_life = sum(lifestyle_factors.values())
    total = total_bio + total_life

    pct_bio = (total_bio / total) * 100
    pct_life = (total_life / total) * 100

    st.subheader("Resultados")

    if nombre:
        st.write(f"Paciente: {nombre}")

    col1, col2 = st.columns(2)
    col1.metric("Factores Biológicos", f"{pct_bio:.1f}%")
    col2.metric("Estilo de Vida", f"{pct_life:.1f}%")

    # GRÁFICA DE PASTEL
    st.subheader("Gráfica de distribución")

    chart_data = {
        "Categoría": ["Biológicos", "Estilo de Vida"],
        "Porcentaje": [pct_bio, pct_life]
    }

    st.bar_chart(chart_data, x="Categoría", y="Porcentaje")

    # INTERPRETACIÓN
    st.subheader("Interpretación")

    if pct_life > pct_bio:
        st.success("Predominan factores modificables. Se recomienda mejorar hábitos.")
    else:
        st.warning("Predominan factores biológicos. Se recomienda control médico.")

    st.markdown(
        '<div class="medical-note"><strong>Nota importante:</strong> Este modelo es educativo y no sustituye diagnóstico clínico.</div>',
        unsafe_allow_html=True,
    )

    with st.expander("Recomendaciones generales de prevención"):
        st.markdown(
            """
            - Mantener controles médicos periódicos.
            - Mejorar alimentación y actividad física regular.
            - Evitar tabaco y reducir alcohol.
            - Seguir indicaciones terapéuticas del personal de salud.
            """
        )
