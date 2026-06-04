import numpy as np
import matplotlib.pyplot as plt

# ==========================
# DATA SAMPEL
# ==========================

x = [
    7,6,6,5.5,5,5,6,4,7,6,
    4,7,5,7,4,8,6,5,5,7,
    6,5,6,6,6,5,5.5,5,4,7,
    5,5,6,7,7,6,8,4,5,2,
    7,7,3,7,6,6,6,6,6,5
]

y = [
    3,3,3,3,4,3,3,2,3,2,
    3,3,2,3,3,4,3,5,2,3,
    2,3,3,3,3,3,3,2,4,3,
    4,3,2,3,4,3,5,3,3,5,
    4,3,2,3,5,3,2,3,3,4
]

# ==========================
# REGRESI LINIER
# ==========================

slope, intercept = np.polyfit(x, y, 1)

# Korelasi dan determinasi
r = np.corrcoef(x, y)[0, 1]
r2 = r**2

# Titik garis regresi
x_line = np.linspace(min(x), max(x), 100)
y_line = intercept + slope * x_line

# ==========================
# OUTPUT
# ==========================

print("="*50)
print("HASIL ANALISIS REGRESI LINIER")
print("="*50)
print(f"Intercept (a) = {intercept:.4f}")
print(f"Slope (b)     = {slope:.4f}")
print(f"Persamaan     = Ŷ = {intercept:.4f} + {slope:.4f}X")
print(f"Korelasi (r)  = {r:.4f}")
print(f"Determinasi (R²) = {r2:.4f}")

# ==========================
# VISUALISASI
# ==========================

plt.figure(figsize=(10,6))

# Scatter plot
plt.scatter(
    x,
    y,
    s=80,
    alpha=0.8,
    color='royalblue',
    label='Data Sampel'
)

# Garis regresi
plt.plot(
    x_line,
    y_line,
    color='red',
    linewidth=2.5,
    label='Garis Regresi'
)

# Menampilkan persamaan
info = (
    f"Ŷ = {intercept:.4f} + {slope:.4f}X\n"
    f"r = {r:.4f}\n"
    f"R² = {r2:.4f}"
)

plt.text(
    2.2,
    4.5,
    info,
    fontsize=10,
    bbox=dict(facecolor='white')
)

plt.title(
    "Scatter Plot dan Garis Regresi\nDurasi Tidur vs Produktivitas Mahasiswa ITERA"
)

plt.xlabel("Durasi Tidur (Jam)")
plt.ylabel("Skor Produktivitas")

plt.grid(True)
plt.legend()

plt.savefig(
    "Scatter_Regresi_Tidur_Produktivitas.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()