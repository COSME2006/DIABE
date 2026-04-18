import streamlit as st

st.set_page_config(page_title="Evaluación de Riesgo - Diabetes", layout="centered")

st.title("🧠 Evaluación de Factores de Riesgo")
st.subheader("Modelo educativo - Diabetes Mellitus (Tipo 1 y 2)")

st.write("Ingresa valores entre 0 y 1:")
st.write("0 = Sin riesgo | 1 = Riesgo máximo")

# Nombre
nombre = st.text_input("Nombre del paciente (opcional)")

# ==============================
# FACTORES BIOLÓGICOS
# ==============================
st.header("Factores Biológicos")

edad_risk = st.slider("Edad (>50 años)", 0.0, 1.0, 0.0)
genetic_risk = st.slider("Predisposición genética (antecedentes familiares)", 0.0, 1.0, 0.0)
base_metabolic = 0.10

# ==============================
# ESTILO DE VIDA
# ==============================
st.header("Estilo de Vida")

dieta = st.slider("Dieta (alto en azúcar/grasas)", 0.0, 1.0, 0.0)
actividad = st.slider("Actividad física (sedentarismo)", 0.0, 1.0, 0.0)
adherencia = st.slider("Adherencia terapéutica", 0.0, 1.0, 0.0)
estres = st.slider("Estrés", 0.0, 1.0, 0.0)

# ==============================
# FACTORES ADICIONALES
# ==============================
st.header("Factores Adicionales")

imc = st.slider("Índice de Masa Corporal (IMC)", 0.0, 1.0, 0.0)
alcohol = st.slider("Consumo de alcohol", 0.0, 1.0, 0.0)
tabaco = st.slider("Tabaquismo", 0.0, 1.0, 0.0)
presion = st.slider("Presión arterial elevada", 0.0, 1.0, 0.0)

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

    st.write(f"Factores Biológicos: {pct_bio:.1f}%")
    st.write(f"Estilo de Vida: {pct_life:.1f}%")

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

    st.info("Este modelo es educativo y no sustituye diagnóstico clínico.")
