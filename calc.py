import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="🕰️ Calculadora PERT")
st.title("Calculadora de Tiempo Estimado (Método PERT)")

# Entradas como texto (vacías por defecto)
to_input = st.text_input("Tiempo Optimista (TO)",placeholder="Ingrrese Tiempo en Horas")
tm_input = st.text_input("Tiempo Más Probable (TM) ",placeholder="Ingrrese Tiempo en Horas")
tp_input = st.text_input("Tiempo Pesimista (TP)",placeholder="Ingrrese Tiempo en Horas")


if st.button("Calcular resultado"):
    try:
        to = float(to_input)
        tm = float(tm_input)
        tp = float(tp_input)

        # Cálculos PERT
        estimado = (to + 4 * tm + tp) / 6
        desviacion = (tp - to) / 6
        estimado_mas = estimado + desviacion
        estimado_menos = estimado - desviacion
        en_dias= estimado_mas /7
      

        st.info(f"🕒 Estimado: **{estimado:.2f}** horas")
        st.info(f"📉 Desviación estándar: ±**{desviacion:.2f}** horas")
        st.success(f"✅ Tiempo Estimado Real: **{estimado_mas:.2f}** horas | **{en_dias:.2f} Dias**")
        
        

        # Etiquetas y valores
        categorias = ["Optimista", "Más Probable", "Pesimista", "Estimado"]
        valores = [to, tm, tp, estimado]

        # Crear figura con barras
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=categorias,
            y=valores,
            name="Tiempos",
            marker_color='lightskyblue'
        ))

        # Agregar línea de desviación
        fig.add_trace(go.Scatter(
            x=["Estimado", "Estimado"],
            y=[estimado_menos, estimado_mas],
            mode="lines+markers",
            name="Estimado ± Desvío",
            line=dict(color="firebrick", width=3, dash="dash"),
            marker=dict(size=8)
        ))

        fig.update_layout(
            title="Comparación de Tiempos con Desviación Estándar",
            yaxis_title="Horas",
            xaxis_title="Tipo de Tiempo",
            legend_title="Referencias",
            bargap=0.4
        )

        st.plotly_chart(fig, use_container_width=True)

    except ValueError:
        st.error("⚠️ Por favor, ingresá solo números válidos en todos los campos.")
        

