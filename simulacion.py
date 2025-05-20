import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def crear_malla(x_min, x_max, y_min, y_max, resolucion):
    """Crea la malla 2D del espacio."""
    x = np.linspace(x_min, x_max, resolucion)
    y = np.linspace(y_min, y_max, resolucion)
    X, Y = np.meshgrid(x, y)
    return X, Y

def calcular_ondas(X, Y, fuente1, fuente2, frecuencia, tiempo, velocidad_sonido=343):
    """Calcula las ondas individuales y la suma en un instante de tiempo."""
    lambda_onda = velocidad_sonido / frecuencia
    k = 2 * np.pi / lambda_onda
    omega = 2 * np.pi * frecuencia

    r1 = np.sqrt((X - fuente1[0])**2 + (Y - fuente1[1])**2)
    r2 = np.sqrt((X - fuente2[0])**2 + (Y - fuente2[1])**2)

    onda1 = np.sin(k * r1 - omega * tiempo)
    onda2 = np.sin(k * r2 - omega * tiempo)
    onda_total = onda1 + onda2

    return onda1, onda2, onda_total

def graficar_interferencia(X, Y, onda, titulo="Interferencia", mostrar_ejes=True):
    """Genera el gráfico de una onda."""
    fig, ax = plt.subplots(figsize=(8, 6))
    mapa = ax.pcolormesh(X, Y, onda, shading='auto', cmap='seismic', vmin=-2, vmax=2)
    fig.colorbar(mapa, ax=ax, label='Amplitud')
    ax.set_title(titulo)
    if mostrar_ejes:
        ax.set_xlabel('x (m)')
        ax.set_ylabel('y (m)')
    else:
        ax.axis('off')
    return fig

def crear_animacion(X, Y, fuente1, fuente2, frecuencia, frames=60, velocidad_sonido=343):
    """Crea una animación de la interferencia."""
    fig, ax = plt.subplots(figsize=(8, 6))
    k = 2 * np.pi * frecuencia / velocidad_sonido
    omega = 2 * np.pi * frecuencia

    r1 = np.sqrt((X - fuente1[0])**2 + (Y - fuente1[1])**2)
    r2 = np.sqrt((X - fuente2[0])**2 + (Y - fuente2[1])**2)

    # Inicializar gráfico vacío
    mapa = ax.pcolormesh(X, Y, np.zeros_like(X), shading='auto', cmap='seismic', vmin=-2, vmax=2)
    fig.colorbar(mapa, ax=ax, label='Amplitud')
    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_title('Animación de Interferencia de Ondas')

    def actualizar(frame):
        t = frame / frames  # tiempo normalizado
        onda1 = np.sin(k * r1 - omega * t)
        onda2 = np.sin(k * r2 - omega * t)
        onda_total = onda1 + onda2
        mapa.set_array(onda_total.ravel())
        return mapa,

    ani = animation.FuncAnimation(fig, actualizar, frames=frames, interval=50, blit=True)

    return ani



if __name__ == "__main__":
    print("Este módulo es para ser usado desde app.py")
