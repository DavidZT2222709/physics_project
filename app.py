import streamlit as st
import simulacion
import matplotlib.pyplot as plt
import numpy as np
import io
import tempfile

simulador_desktop = "otros/main.exe"

def main():
    st.set_page_config(page_title="Interferencia de Ondas - Física 3", layout="wide")
    st.title("🛜 Simulación De Interfertencia de Ondas - Interferencia Constructiva y Destructiva")

    st.subheader("Autores: Angely Contreras - Juan Gabriel García - David Zapata")

    st.write("""
    Esta aplicación simula cómo dos ondas emitidas por dos fuentes diferentes se combinan 
    en el espacio, mostrando las ecuaciones individuales, la interferencia y su animación,
    pero para esto toca conocer los conceptos fisicos que van detrás de toda esta simulación.
    """)


    st.title("Reflexión y Transmisión de Onda")

    st.subheader("Reflexión")

    st.write("""
    La reflexión se presenta de dos formar y estas se pueden explicar gracias a las condiciones de fronteras, por esto imaginemos
    que tenemos una cuerda amarrada en unos de sus extremos cuando programos una onda sobre esta
    es conocida como onda incidente, cuando esta llega al otro obsservamos que una onda se devuelve por 
    la parte de abajo de esta siendo esta la onda relfejada. Ahora estudiemos el siguiente caso cuando propagamos una onda incidente en una cuerda y esta tiene la otra punta libre
    en la imagen (b) se observa que la onda reflejada se da devuelve por arriba, esto 
    """)

    st.image("imagenes/Reflexión.jpeg", caption= "Reflexión con condiciones de frontera. Fuente: OpenStax")

    st.subheader("Transmisión")

    st.write("""
    Existen casos en los cuales la frontera del medio no es fija ni tampoco esta libre, pero se nos dan los casos
    donde podemos tener dos cuerdas. Obsersvemos la imagen (a) donde se considera una cuerda de densisdad lineal baja
    y esta atada a una cuerda de mayor densidad lineal. En estos casos las ondas reflejadas se desfasa con respecto a
    la onda incidente. También hay una onda transmitida la cual esta en fase don respecto a la onda incidente.
    """)

    st.image("imagenes/Transmisión.jpeg", caption="Transmisión y Reflexión de onda en cuerdas de diferentes densisdad. Fuente: OpenStax")



    st.title("Interferencia")

    st.write("""
    La interferencia es un fenomeno que se produce entre dos ondas identicas, cuando analizamos este podemos observarlo en
    ondas sonoras, ondas electromagneticas como ondas de luz o incluso en las ondas producidas en un charco de agua. Estas dos
    ondas llegan al mismo punto de exactamente en fase, por conceptos la interferencia es la suma algebraica de dos ondas que en
    este caso son iguales por lo tanto estas se rigen la siguientes formulas y se representan visualmente así:
    """)

    st.latex(r"Y_1(x,t) = A\sin(kx - \omega t)")
    st.latex(r"Y_2(x,t) = A\sin(kx - \omega t)")

    st.subheader("Interferencia algebraica")

    st.latex(r"Y(x,t) = Y_1 + Y_2 = 2A\sin(kx-\omega t)")

    st.write("""La interferencia constructiva es aquella que se producen cuando dos ondas identicas se superponen entres si de tal forma que
    sus valles y crestas coinciden entre si dando como resultado una onda con una mayor amplitud. Estas se producen cuando están es fase
    es decir, tienen el mimso de punto de inicio en un periodo determinado.
    """)

    st.subheader("Representación Gráfica")

    A = 1          # Amplitud
    k = 2 * np.pi  # Número de onda
    w = 2 * np.pi  # Frecuencia angular
    t = 0          # Tiempo fijo (puedes animarlo si gustas)
    x = np.linspace(0, 2, 1000)  # De 0 a 2 lambda (si lambda = 1)

    y1 = A * np.sin(k * x - w * t)
    y2 = A * np.sin(k * x - w * t)
    y = y1 + y2

    fig, axs = plt.subplots(3, 1, figsize=(8, 8), sharex=True)

    axs[0].plot(x, y1, color='steelblue')
    axs[0].set_title(r'(a) $y_1(x, t) = A \sin(kx - \omega t)$')
    axs[0].set_ylabel('A(m)')
    axs[0].grid(True)
    axs[0].set_ylim(-2*A, 2*A)

    axs[1].plot(x, y2, color='indianred')
    axs[1].set_title(r'(b) $y_2(x, t) = A \sin(kx - \omega t)$')
    axs[1].set_ylabel('A(m)')
    axs[1].grid(True)
    axs[1].set_ylim(-2*A, 2*A)

    axs[2].plot(x, y, color='black')
    axs[2].set_title(r'(c) $y(x, t) = y_1 + y_2 = 2A \sin(kx - \omega t)$')
    axs[2].set_ylabel('A(m)')
    axs[2].set_xlabel('λ(m)')
    axs[2].grid(True)
    axs[2].set_ylim(-2*A, 2*A)

    plt.tight_layout()
    plt.savefig("imagenes/ondas_superpuestas.png")

    st.image("imagenes/ondas_superpuestas.png", caption="Interferencia Constructiva. Fuente: Autores")

    st.write("""
    La interferencia destructuva es aquella que se da cuando dos ondas se superponen de tal forma que
    sus crestas y valler se cancelan mutuamente, dando como resultado una onda con menos amplitud o
    amplitud 0, en terminos mas tecnicos cuando las ondas estan totalmente desfasadas, las crestas de
    una onda coinciden con el valle de la otra, generando una onda resultante más pequeña o nula.
    """)

    A = 1
    k = 2 * np.pi
    w = 2 * np.pi
    t = 0
    x = np.linspace(0, 2, 1000)  # 0 a 2 lambda si lambda = 1

    # Ondas
    y1 = A * np.sin(k * x - w * t + np.pi)  # desfase de pi
    y2 = A * np.sin(k * x - w * t)
    y = y1 + y2  # suma de ondas

    # Crear la figura y subgráficas
    fig, axs = plt.subplots(3, 1, figsize=(8, 8), sharex=True)

    # Gráfica (a)
    axs[0].plot(x, y1, color='steelblue')
    axs[0].set_title(r'(a) $y_1(x, t) = A \sin(kx - \omega t + \pi)$')
    axs[0].set_ylabel('y(m)')
    axs[0].grid(True)
    axs[0].set_ylim(-2*A, 2*A)

    # Gráfica (b)
    axs[1].plot(x, y2, color='indianred')
    axs[1].set_title(r'(b) $y_2(x, t) = A \sin(kx - \omega t)$')
    axs[1].set_ylabel('y(m)')
    axs[1].grid(True)
    axs[1].set_ylim(-2*A, 2*A)

    # Gráfica (c)
    axs[2].plot(x, y, color='black')
    axs[2].set_title(r'(c) $y(x, t) = y_1 + y_2 = 0$')
    axs[2].set_ylabel('y(m)')
    axs[2].set_xlabel('λ(m)')
    axs[2].grid(True)
    axs[2].set_ylim(-2*A, 2*A)

    plt.tight_layout()
    plt.savefig("imagenes/interferencia_destructiva.png")

    st.image("imagenes/interferencia_destructiva.png", caption="Interferencia Destructiva. Fuente: Autores")

    st.write("""Cuando se presenta interferencia constructiva en ondas se observa que la amplitud de la interferencia
    es del doble de la amplitud de la onda original, la longitud de onda es aquella que nos dice la distancia que hay
    entre cresta y cresta en una onda también conocida como 'λ' si queremos hallar la interferencia que se presenta cierto
    se tiene en cuenta lo siguiente:""")

    A = (-3, 0)
    B = (3, 0)
    C = (0, 2)

    # Crear figura y ejes
    fig, ax = plt.subplots(figsize=(8, 6))

    # Dibujar líneas (vectores) AC y BC
    ax.plot([A[0], C[0]], [A[1], C[1]], 'k-', linewidth=2)  # Línea AC
    ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', linewidth=2)  # Línea BC

    # Dibujar puntos
    ax.plot(*A, 'o', color='blue')
    ax.plot(*B, 'o', color='blue')
    ax.plot(*C, 'o', color='blue')

    # Etiquetas de los puntos
    ax.text(A[0]-0.3, A[1]-0.3, 'A', color='blue')
    ax.text(B[0]+0.1, B[1]-0.3, 'B', color='blue')
    ax.text(C[0]+0.1, C[1]+0.1, 'C', color='blue')

    # Textos adicionales
    ax.text(A[0], A[1]-0.6, 'Fuente 1', fontsize=10, ha='center')
    ax.text(B[0], B[1]-0.6, 'Fuente 2', fontsize=10, ha='center')
    ax.text(C[0], C[1]-0.4, 'Interferencia', fontsize=10, ha='center')
    ax.text(C[0]-0.2, C[1]+0.4, 'A = 2A', fontsize=12, fontweight='bold')

    # Etiquetas de los vectores
    ax.text(-1.8, 1.2, 'u', fontsize=12)
    ax.text(1.4, 1.2, 'v', fontsize=12)

    # Configurar cuadrícula y ejes
    ax.set_xlim(-5, 5)
    ax.set_ylim(-2, 3)
    ax.set_xticks(range(-5, 6))
    ax.set_yticks(range(-2, 4))
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.set_aspect('equal', adjustable='box')

    # Centrar los ejes en el origen
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.savefig("imagenes/plano_cartesiano.png")

    st.image("imagenes/plano_cartesiano.png", caption="Plano con posición de fuente en igual dirección. Fuentes:Autores")

    st.write("""Como se observa en la imagen cuando se presenta interferencia constructuva el las ondas se encuentran
    en fase por la longitud de onda que estas presentan lo cual hace que su amplitud sea el doble de la amplitud inicial.
    cuando se presentan estos casos de que existe interferencia contructiva y queremos que hallar la interferencia en un punto cualquiera
    donde se de IC se deben tomar la siguiente ecuación:""")

    st.latex(r"\Delta S = S_2 - S_1 ")

    st.write("""Cuando debido a que esta se encuentran en fase por la condición de sus longitud de onda que es 'λ' esta ecuació se puede
    reescribir de la siguiente manera:""")

    st.latex(r"\Delta S = m \lambda ")
    st.latex(r"m = 0, 1, 2, 3, ..., \infty")

    st.write("La representación gráfica es ls siguiente:")

    A = (-3, 0)
    B = (3, 0)
    C = (-2, 3)

    # Crear figura y ejes
    fig, ax = plt.subplots(figsize=(8, 6))

    # Dibujar vectores como líneas
    ax.plot([A[0], C[0]], [A[1], C[1]], color='black', linewidth=2)  # Vector u (AC)
    ax.plot([B[0], C[0]], [B[1], C[1]], color='black', linewidth=2)  # Vector v (BC)

    # Dibujar puntos
    ax.plot(*A, 'o', color='blue')
    ax.plot(*B, 'o', color='blue')
    ax.plot(*C, 'o', color='blue')

    # Etiquetas de puntos
    ax.text(A[0]-0.2, A[1]-0.5, 'A', color='blue')
    ax.text(B[0]+0.1, B[1]-0.5, 'B', color='blue')
    ax.text(C[0], C[1]+0.2, 'C', color='blue')

    # Texto de vectores
    ax.text(-2.7, 1.5, 'u', fontsize=12)
    ax.text(0.7, 1.7, 'v', fontsize=12)

    # Texto de fuentes
    ax.text(A[0], A[1]-1, 'Fuente 1', fontsize=12, ha='center')
    ax.text(B[0], B[1]-1, 'Fuente 2', fontsize=12, ha='center')

    # Configurar cuadrícula
    ax.grid(True, linestyle='--', linewidth=0.5)

    # Limitar y centrar ejes
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-3.5, 4.5)
    ax.set_xticks(range(-5, 6))
    ax.set_yticks(range(-4, 6))
    ax.set_aspect('equal', adjustable='box')

    # Mover los ejes al centro
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.savefig("imagenes/interferencia_sin_origen.png")

    st.image("imagenes/interferencia_sin_origen.png", caption="Interferencia fuera del eje optico. Fuente: Autores")

    st.write("""La interferencia destructiva se da cuando las ondas no estan en fase con respecto a su longitud de onda, cuando una de las ondas esra desfasada
    tan solo 'λ/2' con respecto a la otra, en estos casos  cuando se presenta desfase la amplitud en estos puntos es 0, la expresión para esta es la siguiente:""")

    st.latex(r"\Delta S = (2m + 1) \frac{\lambda}{2} ")
    st.latex(r"m = 0, 1, 2, 3, ..., \infty")

    st.write("Nota: Cuando el desfase no es 'λ' o 'λ/2' la amplitud tiene la siguiente condición:")

    st.latex(r"0 < A < 2A")

    st.info("Para mas información sobre ondas consulte lo siguiente 💡")

    st.link_button("Phet - Interfrencia de Ondas", url="https://phet.colorado.edu/sims/html/wave-interference/latest/wave-interference_all.html?locale=es")
    st.link_button("OpenStax - Interferencia de Ondas", url="https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/16-5-interferencia-de-ondas")
    # --- Barra lateral de configuración ---
    st.sidebar.header("⚙️ Parámetros de la simulación")

    x_min = st.sidebar.number_input("x mínimo (m)", value=-10.0)
    x_max = st.sidebar.number_input("x máximo (m)", value=10.0)
    y_min = st.sidebar.number_input("y mínimo (m)", value=-10.0)
    y_max = st.sidebar.number_input("y máximo (m)", value=10.0)
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

        try:
            with open(simulador_desktop, "rb") as archivo:
                app_exe = archivo.read()

            st.download_button(
                label= "📥 Dercargar simulador para escritorio",
                data = app_exe,
                file_name="otros/main.exe",
                mime = "application/octet-stream"
            )
        except FileNotFoundError:
            st.error(f"Archivo {simulador_desktop} no se encontró.")
        except Exception as e:
            st.error(f"Error con el archivo{e}")

    st.markdown("---")

if __name__ == "__main__":
    main()