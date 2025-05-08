import streamlit as st
import simulacion  # Nuestro módulo
import matplotlib.pyplot as plt
import numpy as np
import io
import tempfile

def main():
    st.set_page_config(page_title="Interferencia de Ondas - Física 3", layout="wide")
    st.title("🎶 Simulación Avanzada de Interferencia de Ondas Sonoras")

    st.write("""
    Esta aplicación simula cómo dos ondas emitidas por dos fuentes diferentes se combinan 
    en el espacio, mostrando las ecuaciones individuales, la interferencia y su animación.
    """)

    # --- Barra lateral de configuración ---
    st.sidebar.header("⚙️ Parámetros de la simulación")

    x_min = st.sidebar.number_input("x mínimo (m)", value=-5.0)
    x_max = st.sidebar.number_input("x máximo (m)", value=5.0)
    y_min = st.sidebar.number_input("y mínimo (m)", value=-5.0)
    y_max = st.sidebar.number_input("y máximo (m)", value=5.0)
    resolucion = st.sidebar.slider("Resolución de la malla", min_value=100, max_value=1000, value=500, step=50)

    st.sidebar.subheader("📍 Posiciones de las fuentes")
    fuente1_x = st.sidebar.number_input("Fuente 1 - x", value=-1.0)
    fuente1_y = st.sidebar.number_input("Fuente 1 - y", value=0.0)
    fuente2_x = st.sidebar.number_input("Fuente 2 - x", value=1.0)
    fuente2_y = st.sidebar.number_input("Fuente 2 - y", value=0.0)

    st.sidebar.subheader("🎵 Parámetros de las ondas")
    frecuencia = st.sidebar.slider("Frecuencia (Hz)", min_value=100.0, max_value=2000.0, value=440.0, step=10.0)

    # --- Botón para lanzar la simulación ---
    if st.sidebar.button("Simular"):
        # Crear malla
        X, Y = simulacion.crear_malla(x_min, x_max, y_min, y_max, resolucion)

        # Elegir un tiempo fijo para ver instantáneamente
        tiempo = 0.0

        # Calcular ondas
        onda1, onda2, onda_total = simulacion.calcular_ondas(X, Y, (fuente1_x, fuente1_y), (fuente2_x, fuente2_y), frecuencia, tiempo)

        # --- Sección de ecuaciones ---
        st.header("📜 Ecuaciones de las Ondas")
        velocidad_sonido = 343  # m/s
        lambda_onda = velocidad_sonido / frecuencia
        k = 2 * np.pi / lambda_onda
        omega = 2 * np.pi * frecuencia

        st.latex(r"\text{Fuente 1:} \quad \Psi_1(x,y,t) = \sin(kr_1 - \omega t)")
        st.latex(r"\text{Fuente 2:} \quad \Psi_2(x,y,t) = \sin(k r_2 - \omega t)")
        st.latex(r"\text{Interferencia:} \quad \Psi_{\text{total}}(x,y,t) = \Psi_1 + \Psi_2")

        st.markdown(f"Donde: \n\n- $k$ (número de onda) = {k:.2f} rad/m \n- $\omega$ (frecuencia angular) = {omega:.2f} rad/s")

        # --- Sección de resultados ---
        st.header("📊 Visualización de las Ondas")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Onda 1")
            fig1 = simulacion.graficar_interferencia(X, Y, onda1, titulo="Fuente 1")
            st.pyplot(fig1)

        with col2:
            st.subheader("Onda 2")
            fig2 = simulacion.graficar_interferencia(X, Y, onda2, titulo="Fuente 2")
            st.pyplot(fig2)

        with col3:
            st.subheader("Interferencia Total")
            fig3 = simulacion.graficar_interferencia(X, Y, onda_total, titulo="Interferencia")
            st.pyplot(fig3)

        # --- Sección de animación ---
        st.header("🎥 Animación de la Interferencia")
        st.write("Visualización dinámica de cómo evolucionan las ondas en el tiempo.")

        ani = simulacion.crear_animacion(X, Y, (fuente1_x, fuente1_y), (fuente2_x, fuente2_y), frecuencia)

        # Guardar en archivo temporal .gif
        with tempfile.NamedTemporaryFile(suffix=".gif", delete=False) as tmpfile:
            ani.save(tmpfile.name, writer="pillow")
            gif_path = tmpfile.name

        # Mostrar el gif
        with open(gif_path, "rb") as f:
            gif_bytes = f.read()
            st.image(gif_bytes, use_container_width=True)

        # Botón de descarga opcional
        st.download_button(
            label="📥 Descargar animación (GIF)",
            data=gif_bytes,
            file_name="interferencia.gif",
            mime="image/gif"
        )

    st.markdown("---")

if __name__ == "__main__":
    main()
