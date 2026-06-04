import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f

# Derajat bebas
df1 = 24
df2 = 24

# Nilai F dari laporan
f_hitung = 1.5793
f_kiri = 0.4227
f_kanan = 2.2324

# Data x
x = np.linspace(0, 5, 1000)

# PDF Distribusi F
y = f.pdf(x, df1, df2)

plt.figure(figsize=(10,6))

# Kurva F
plt.plot(
    x,
    y,
    color='darkgreen',
    linewidth=3,
    label='Distribusi F'
)

# Area penerimaan H0
plt.fill_between(
    x,
    y,
    where=(x >= f_kiri) & (x <= f_kanan),
    color='lightgreen',
    alpha=0.5,
    label='Daerah Penerimaan H₀'
)

# Batas kiri
plt.axvline(
    f_kiri,
    color='red',
    linestyle='--',
    linewidth=2,
    label=f'Batas kiri = {f_kiri}'
)

# Batas kanan
plt.axvline(
    f_kanan,
    color='red',
    linestyle='--',
    linewidth=2,
    label=f'Batas kanan = {f_kanan}'
)

# F hitung
plt.axvline(
    f_hitung,
    color='blue',
    linewidth=2,
    label=f'Fhitung = {f_hitung}'
)

plt.title("Distribusi F untuk Uji Perbandingan Variansi")
plt.xlabel("Nilai F")
plt.ylabel("Kepadatan Probabilitas")

plt.grid(True, alpha=0.3)
plt.legend()

plt.savefig(
    "Distribusi_F.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()