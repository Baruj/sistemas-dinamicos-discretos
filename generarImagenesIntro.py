import numpy as np
import matplotlib.pyplot as plt
import os

# Carpeta donde guardar las imágenes
output_folder = "./imagenes_intro/"
os.makedirs(output_folder, exist_ok=True)

# --- 1️⃣ Estabilidad ---
x = np.arange(0, 50+1)
y_stable = np.ones_like(x) * 0.6  # valor estable constante

plt.figure(figsize=(6,4))
plt.plot(x, y_stable, 'o-', color='blue', label='x_n')
plt.ylim(0,1)
plt.xlabel("Iteración n", fontsize=12)
plt.ylabel("x_n", fontsize=12)
plt.title("Estabilidad: convergencia a un valor fijo", fontsize=14)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "estabilidad.png"), dpi=150)
plt.close()

# --- 2️⃣ Ciclo periódico ---
y_cycle = np.array([0.3,0.7]*25 + [0.3])  # ciclo de periodo 2

plt.figure(figsize=(6,4))
plt.plot(x, y_cycle, 'o-', color='green', label='x_n')
plt.ylim(0,1)
plt.xlabel("Iteración n", fontsize=12)
plt.ylabel("x_n", fontsize=12)
plt.title("Ciclo: oscilación periódica", fontsize=14)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "ciclo.png"), dpi=150)
plt.close()

# --- 3️⃣ Caos determinista ---
r = 3.9
y_chaos = [0.1]
for i in range(50):
    y_chaos.append(r*y_chaos[-1]*(1-y_chaos[-1]))

plt.figure(figsize=(6,4))
plt.plot(range(len(y_chaos)), y_chaos, 'o-', color='red', label='x_n')
plt.ylim(0,1)
plt.xlabel("Iteración n", fontsize=12)
plt.ylabel("x_n", fontsize=12)
plt.title("Caos determinista", fontsize=14)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "caos.png"), dpi=150)
plt.close()

print("¡Imágenes generadas con éxito en la carpeta 'imagenes_intro/'!")
