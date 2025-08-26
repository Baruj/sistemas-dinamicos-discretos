import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os

#  Configuración general 
st.set_page_config(page_title="🌌Sistemas Dinámicos Discretos", layout="wide")

# Barra lateral: menú de navegación 
st.sidebar.title("🌌Sistemas Dinámicos Discretos")
st.sidebar.title("Menú")
page = st.sidebar.radio(
    "Selecciona la sección:",
    [
        "Introducción",
        "Explicación paso a paso (Parte 1)",
        "Explicación paso a paso (Parte 2)",
        "Página interactiva: Mapa Logístico",
        "Página interactiva: Caminata Aleatoria",
        "Página interactiva: Mapas Avanzados",
        "Autores"
    ]
)

# Carpeta de imágenes 
img_folder = "./imagenes_intro/"

# ======================
#  Página 1: Introducción 
# ======================
if page == "Introducción":
    st.title("🌌 Sistemas Dinámicos Discretos")
    
    st.markdown("""
    Bienvenido a la exploración de **sistemas dinámicos discretos**.  
    Esta página interactiva te permite descubrir cómo **comportamientos complejos surgen de reglas simples**, 
    un concepto fundamental en matemáticas y ciencias.
    """)

    st.subheader("🔹 Conceptos Clave")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image(os.path.join(img_folder, "estabilidad.png"), caption="Estabilidad: convergencia a un valor fijo")
        st.write("""
        🔹 La **estabilidad** aparece cuando un sistema dinámico alcanza un valor fijo, 
        sin importar pequeñas perturbaciones.  
        Ejemplo cotidiano: una **taza de café caliente** que, con el tiempo, siempre termina alcanzando la temperatura ambiente, 
    sin importar si al inicio estaba muy caliente o solo tibia.
        """)
    
    with col2:
        st.image(os.path.join(img_folder, "ciclo.png"), caption="Ciclo: oscilación periódica")
        st.write("""
        🔹 Los **ciclos** ocurren cuando el sistema oscila entre un conjunto limitado de valores.  
        Ejemplo cotidiano: el **día y la noche**. La luz solar aumenta durante el día y disminuye en la noche, en un ciclo que se repite cada 24 horas.
        """)
    
    with col3:
        st.image(os.path.join(img_folder, "caos.png"), caption="Caos determinista")
        st.write("""
        🔹 El **caos determinista** surge cuando un sistema sigue reglas simples pero su comportamiento se vuelve impredecible a largo plazo.  
        Ejemplo cotidiano: el **clima**. Aunque las leyes físicas que lo gobiernan son deterministas, una pequeña variación en las condiciones iniciales (como la temperatura o presión en un lugar) puede cambiar por completo el pronóstico días después.
    """)



# ======================
#  Página 2: Explicación Paso a Paso 1 
# ======================
if page == "Explicación paso a paso (Parte 1)":
    st.title("📘 Explicación Paso a Paso (1/2)")

    # Introducción a la ecuación logística
    st.markdown(
        """
        La **ecuación logística discreta** es un modelo sencillo que describe cómo evoluciona 
        una población limitada por los recursos disponibles.  
        Aunque la ecuación es simple, su comportamiento puede ser muy rico: puede 
        alcanzar **equilibrios estables**, entrar en **ciclos periódicos** o incluso mostrar **caos determinista**.  
        Este es un ejemplo clásico de **sistema dinámico no lineal** y sirve para estudiar 
        estabilidad y comportamiento de sistemas complejos.
        """
    )

    # Mostrar la ecuación
    st.subheader("Ecuación logística discreta")
    st.latex(r"x_{n+1} = r \, x_n \, (1 - x_n)")

    # Explicación de los términos
    st.markdown("**Interpretación de los términos:**")
    st.latex(r"x_n \in [0,1] \quad \text{fracción de la población en el paso } n \ (0=\text{extinción}, 1=\text{máxima población})")
    st.latex(r"r > 0 \quad \text{tasa de crecimiento de la población}")
    st.latex(r"(1 - x_n) \quad \text{efecto de saturación por recursos limitados}")

    # Resumen didáctico
    st.markdown(
        """
        **Resumen didáctico:**  
        
        - Para $0 < r < 1$: la población disminuye hasta extinguirse.  
        - Para $1 \le r < 3$: la población alcanza un **equilibrio estable**, donde pequeñas perturbaciones se corrigen solas.  
        - Para $r \ge 3$: comienzan a aparecer **ciclos periódicos** y eventualmente **caos**, donde la población puede variar de manera compleja.
        """
    )

    # Explorador interactivo
    st.markdown("### Explora cómo cambia la dinámica según \(r\)")
    r_example = st.slider("Parámetro r", 0.0, 3.0, 2.5, 0.01)
    x0 = st.slider("Valor inicial x₀", 0.0, 1.0, 0.5, 0.01)
    n_iter = st.slider("Número de iteraciones", 20, 200, 50, 10)

    # Simulación
    x = [x0]
    for i in range(1, n_iter):
        x.append(r_example * x[-1] * (1 - x[-1]))

    # Graficar con etiquetas
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(range(n_iter), x,  linestyle='-', color='royalblue')
    ax.set_xlabel("Paso n")
    ax.set_ylabel("Población normalizada $x_n$")
    ax.set_title("Evolución de la población según $r$ y $x_0$")
    ax.grid(True)

    st.pyplot(fig)
    st.caption(
        "La curva muestra cómo $x_n$ evoluciona paso a paso. Observa si se aproxima a un equilibrio o si aparecen ciclos/caos."
    )



# ======================
#  Página 3: Explicación Paso a Paso 2 
# ======================
elif page == "Explicación paso a paso (Parte 2)":
    st.title("📘 Explicación Paso a Paso (2/2)")
    
    st.markdown(
        """
        Cuando aumentamos el parámetro $r$ en la ecuación logística, la dinámica de la población cambia de manera sorprendente:  
        
        - Para $3 \le r < 3.57$, la población ya no se estabiliza en un solo valor, sino que oscila entre varios valores en un **ciclo periódico**.  
          Por ejemplo, puede alternar entre dos valores distintos (ciclo de período 2), luego cuatro (período 4), y así sucesivamente.  
        - Para $r \ge 3.57$, el sistema entra en **caos determinista**, donde la población varía de forma aparentemente aleatoria, aunque seguimos usando reglas simples.  

        🔹 Este fenómeno ilustra un principio fundamental de los sistemas dinámicos: **pequeñas diferencias en las condiciones iniciales pueden generar resultados muy distintos**, especialmente cuando el sistema es caótico.
        """
    )

    # Parámetros interactivos
    r_example = st.slider("Parámetro r", 3.0, 4.0, 3.65, 0.01)
    n_iter = st.slider("Número de iteraciones", 50, 200, 190, 10)
    x0_1 = st.slider("Valor inicial x₀ (trayectoria 1)", 0.0, 1.0, 0.5, 0.0001, format="%.5f")

    x0_2 = st.slider("Valor inicial x₀ (trayectoria 2)", 0.0, 1.0, 0.5001, 0.0001, format="%.5f")


    # Simulación
    x1 = [x0_1]
    x2 = [x0_2]
    for i in range(1, n_iter):
        x1.append(r_example * x1[-1] * (1 - x1[-1]))
        x2.append(r_example * x2[-1] * (1 - x2[-1]))

    # Graficar con etiquetas y leyenda
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(range(n_iter), x1,  linestyle='-', color='royalblue', label=f"x0={x0_1}")
    ax.plot(range(n_iter), x2,  linestyle='-', color='tomato', label=f"x0={x0_2}")
    ax.set_xlabel("Paso n")
    ax.set_ylabel("Población normalizada $x_n$")
    ax.set_title("Evolución de la población con condiciones iniciales cercanas")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)
    
    st.markdown(
        """
        🔍 **Interpretación didáctica:**  

        Observa cómo, a pesar de que las dos trayectorias comienzan casi con el mismo valor inicial ($x_0 = 0.5$ y $x_0 = 0.5001$), con el tiempo divergen de manera significativa.  

        Esto muestra la **sensibilidad a las condiciones iniciales**, una característica clave del **caos determinista**.  
        Para valores menores de $r$, las trayectorias convergen a un equilibrio, pero al superar ciertos umbrales, aparecen ciclos y luego caos, reflejando la riqueza de comportamientos que un sistema simple puede presentar.
        """
    )

# ======================
#  Página 4: Interactiva - Mapa Logístico 
# ======================
elif page == "Página interactiva: Mapa Logístico":
    st.title("🎛️ Simulación Interactiva: Mapa Logístico")

    st.markdown(
        """
        La ecuación logística discreta:

        $$x_{n+1} = r \, x_n \, (1 - x_n)$$

        - $x_n$: población normalizada en el paso $n$ (0 = extinción, 1 = máxima población)
        - $r$: tasa de crecimiento efectiva

        Esta ecuación permite estudiar cómo una población crece y se estabiliza, 
        o cómo puede entrar en ciclos y caos dependiendo de $r$.
        """
    )

    # Parámetros interactivos
    x0 = st.slider("Valor inicial x₀", 0.0, 1.0, 0.5, 0.01)
    r = st.slider("Parámetro r", 0.0, 4.0, 3.2, 0.01)
    n_iter = st.slider("Número de iteraciones", 50, 500, 200, 10)

    # Simulación
    x = [x0]
    for i in range(1, n_iter):
        x.append(r * x[-1] * (1 - x[-1]))

    # Graficar con etiquetas y solo líneas
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(range(n_iter), x, linestyle='-', color='royalblue')
    ax.set_xlabel("Paso n")
    ax.set_ylabel("Población normalizada $x_n$")
    ax.set_title("Evolución de la población - Mapa Logístico")
    ax.grid(True)
    st.pyplot(fig)
    st.markdown("🔹 Ajusta $r$ y $x_0$ para explorar estabilidad, ciclos y caos.")

# ======================
#  Página 5: Interactiva - Caminata Aleatoria 
# ======================
elif page == "Página interactiva: Caminata Aleatoria":
    st.title("🎲 Caminata Aleatoria 1D")

    st.markdown(
        r"""
        La **caminata aleatoria unidimensional** es un modelo estocástico que representa 
        el desplazamiento de una partícula sobre una línea discreta.  
        Sea \(X_n\) la posición de la partícula en el paso \(n\), entonces:

        $$
        X_{n+1} = X_n + \xi_n, \quad \xi_n \in \{-1, +1\}
        $$

        donde \(ξ_n\) es una variable aleatoria que toma valor \(+1\) con probabilidad \(p\) 
        y \(-1\) con probabilidad \(1-p\).  

        Este modelo permite estudiar **procesos estocásticos**, difusión y cómo pequeñas 
        diferencias en la probabilidad o el azar generan trayectorias muy distintas.
        """
    )

    # Parámetros interactivos
    n_steps = st.slider("Número de pasos (n)", 50, 500, 200)
    prob_right = st.slider("Probabilidad de moverse a la derecha (p)", 0.0, 1.0, 0.5)

    # Simulación
    X = [0]  # posición inicial
    for i in range(1, n_steps):
        movimiento = 1 if np.random.rand() < prob_right else -1
        X.append(X[-1] + movimiento)

    # Graficar con etiquetas y solo líneas
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(range(n_steps), X, linestyle='-', color='forestgreen')
    ax.set_xlabel("Paso $n$")
    ax.set_ylabel("Posición $X_n$")
    ax.set_title("Evolución de la caminata aleatoria 1D")
    ax.grid(True)

    st.pyplot(fig)
    st.markdown("🔹 Observa cómo el azar genera trayectorias distintas para cada simulación.")



# ======================
#  Página 6: Interactiva - Mapas Avanzados 
# ======================
elif page == "Página interactiva: Mapas Avanzados":
    st.title("🌀 Mapas Avanzados")

    st.markdown(
        """
        Una variante es el **mapeo seno (sine map)**:

        $$x_{n+1} = r \cdot \sin(\pi x_n)$$

        Esta ecuación introduce no linealidad extra, produciendo comportamientos más complejos 
        y caos incluso para valores moderados de $r$.
        """
    )

    # Parámetros interactivos
    x0 = st.slider("Valor inicial x₀", 0.0, 1.0, 0.5)
    r = st.slider("Parámetro r", 0.0, 4.0, 2.5)
    n_iter = st.slider("Número de iteraciones", 50, 500, 200)

    # Simulación
    x = [x0]
    for i in range(1, n_iter):
        x.append(r * np.sin(np.pi * x[-1]))

    # Graficar con etiquetas y solo líneas
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(range(n_iter), x, linestyle='-', color='purple')
    ax.set_xlabel("Paso n")
    ax.set_ylabel("Valor $x_n$")
    ax.set_title("Evolución de la población - Mapa Seno-Logístico")
    ax.grid(True)
    st.pyplot(fig)
    st.markdown("🔹 Ajusta $r$ y $x_0$ para observar comportamientos complejos y caóticos.")

# ======================
# Sección: Autores
# ======================
elif page == "Autores":
    st.title("👩‍🔬👨‍🔬 Sobre los autores")
    
    st.markdown(
        """
        Este proyecto fue desarrollado por:

        **Itzel Alejandra Ángeles Díaz De León**  
        - Ingeniera Química egresada de la Universidad Autónoma Metropolitana, Unidad Azcapotzalco.  
        - Intereses: educación, divulgación científica y desarrollo de estrategias pedagógicas innovadoras en ciencias aplicadas.  
        - Experiencia en tutorías de química y matemáticas, participación en congresos y proyectos académicos sobre química ambiental y tecnológica.

        **Baruj Furlong Oceguera**  
        - Ingeniero Químico egresado de la Universidad Autónoma Metropolitana, Unidad Azcapotzalco.  
        - Actualmente cursa la **Maestría en Ciencias Matemáticas Aplicadas e Industriales** en la UAM Iztapalapa.  
        - Intereses: teoría de control, simulación de procesos y sistemas dinámicos.  
        - Experiencia en investigación aplicada, modelado de reactores y desarrollo de visualizaciones interactivas de sistemas dinámicos.

        🔹 Ambos autores colaboraron en el desarrollo de este material interactivo para la **divulgación de sistemas dinámicos discretos** y su aplicación en educación y visualización científica.
        """
    )
