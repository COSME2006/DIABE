import streamlit as st


def main() -> None:
    st.set_page_config(page_title="Evaluación de Riesgo - Diabetes", layout="centered")

    st.title("🩺 Evaluación de Factores de Riesgo")
    st.subheader("Modelo educativo - Diabetes Mellitus (Tipo 1 y Tipo 2)")
    st.caption("Ingresa valores entre 0 y 1, donde 0 = sin riesgo y 1 = riesgo máximo.")

    nombre = st.text_input("Nombre del paciente (opcional)")

    st.markdown("### Factores Biológicos")
    edad_risk = st.slider("Edad (>50 años)", 0.0, 1.0, 0.0)
    genetic_risk = st.slider("Predisposición genética (antecedentes familiares)", 0.0, 1.0, 0.0)
    base_metabolic = 0.10

    st.markdown("### Estilo de Vida")
    dieta = st.slider("Dieta (alto en azúcar/grasas)", 0.0, 1.0, 0.0)
    actividad = st.slider("Actividad física (sedentarismo)", 0.0, 1.0, 0.0)
    adherencia = st.slider("Adherencia terapéutica", 0.0, 1.0, 0.0)
    estres = st.slider("Estrés", 0.0, 1.0, 0.0)

    st.markdown("### Factores Adicionales")
    imc = st.slider("Índice de Masa Corporal (IMC)", 0.0, 1.0, 0.0)
    alcohol = st.slider("Consumo de alcohol", 0.0, 1.0, 0.0)
    tabaco = st.slider("Tabaquismo", 0.0, 1.0, 0.0)
    presion = st.slider("Presión arterial elevada", 0.0, 1.0, 0.0)

    input_values = [
        edad_risk,
        genetic_risk,
        dieta,
        actividad,
        adherencia,
        estres,
        imc,
        alcohol,
        tabaco,
        presion,
    ]
    input_ratio = sum(input_values) / len(input_values)
    st.progress(input_ratio, text=f"Índice relativo ingresado: {input_ratio * 100:.0f}%")

    if st.button("Calcular resultados"):
        biological_factors = {
            "Genética": genetic_risk,
            "Edad": edad_risk,
            "Función Base": base_metabolic,
        }
        lifestyle_factors = {
            "Dieta": dieta,
            "Actividad Física": actividad,
            "Adherencia": adherencia,
            "Estrés": estres,
            "IMC": imc,
            "Alcohol": alcohol,
            "Tabaquismo": tabaco,
            "Presión Arterial": presion,
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

        chart_data = {
            "Categoría": ["Biológicos", "Estilo de Vida"],
            "Porcentaje": [pct_bio, pct_life],
        }
        st.bar_chart(chart_data, x="Categoría", y="Porcentaje")

        if pct_life > pct_bio:
            st.success("Predominan factores modificables. Se recomienda mejorar hábitos.")
        else:
            st.warning("Predominan factores biológicos. Se recomienda control médico.")

        st.info("Este modelo es educativo y no sustituye diagnóstico clínico.")


if __name__ == "__main__":
    main()
