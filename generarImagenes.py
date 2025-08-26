import os
import numpy as np
import matplotlib.pyplot as plt

output_folder = "./imagenes_intro/"
os.makedirs(output_folder, exist_ok=True)

# Tamaño y fuente
fig_width, fig_height = 8, 5
label_fontsize = 14
title_fontsize = 16
tick_fontsize = 12

# --- 1️⃣ Estabilidad ---
x = np.arange(51)
y_stable = np.ones_like(x) * 0.6

plt.figure(figsize=(fig_width, fig_height))
plt.plot(x, y_stable, 'o-', color='blue')
plt.ylim(0,1)
plt.xlabel("Iteración n", fontsize=label_fontsize)
plt.ylabel("x_n", fontsize=label_fontsize)
plt.title("Estabilidad: convergencia a un valor fijo", fontsize=title_fontsize)
plt.xticks(fontsize=tick_fontsize)
plt.yticks(fontsize=tick_fontsize)
plt.grid(True)
plt.tight_layout()
plt.savefig(output_folder + "estabilidad.png", dpi=150)
plt.close()

# --- 2️⃣ Ciclo periódico ---
y_cycle = np.array([0.3,0.7]*25 + [0.3])

plt.figure(figsize=(fig_width, fig_height))
plt.plot(x, y_cycle, 'o-', color='green')
plt.ylim(0,1)
plt.xlabel("Iteración n", fontsize=label_fontsize)
plt.ylabel("x_n", fontsize=label_fontsize)
plt.title("Ciclo: oscilación periódica", fontsize=title_fontsize)
plt.xticks(fontsize=tick_fontsize)
plt.yticks(fontsize=tick_fontsize)
plt.grid(True)
plt.tight_layout()
plt.savefig(output_folder + "ciclo.png", dpi=150)
plt.close()

# --- 3️⃣ Caos determinista ---
r = 3.9
y_chaos = [0.1]
for i in range(50):
    y_chaos.append(r*y_chaos[-1]*(1-y_chaos[-1]))

plt.figure(figsize=(fig_width, fig_height))
plt.plot(range(len(y_chaos)), y_chaos, 'o-', color='red')
plt.ylim(0,1)
plt.xlabel("Iteración n", fontsize=label_fontsize)
plt.ylabel("x_n", fontsize=label_fontsize)
plt.title("Caos determinista", fontsize=title_fontsize)
plt.xticks(fontsize=tick_fontsize)
plt.yticks(fontsize=tick_fontsize)
plt.grid(True)
plt.tight_layout()
plt.savefig(output_folder + "caos.png", dpi=150)
plt.close()

print("¡Imágenes generadas con labels legibles en 'imagenes_intro/'!")
