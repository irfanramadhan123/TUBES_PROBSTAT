import numpy as np
import matplotlib.pyplot as plt

# Data dari laporan
mean = 3.12
s = 0.799
n = 50

# Standard Error
se = s / np.sqrt(n)

# Interval Kepercayaan 95%
lower = 2.8929
upper = 3.3471

# Kurva normal
x = np.linspace(mean - 4*se, mean + 4*se, 1000)

y = (1 / (se * np.sqrt(2 * np.pi))) * np.exp(
    -((x - mean) ** 2) / (2 * se ** 2)
)

plt.figure(figsize=(10,6))

plt.plot(x, y, linewidth=2, label="Distribusi Normal")

plt.fill_between(
    x,
    y,
    where=(x >= lower) & (x <= upper),
    alpha=0.3,
    label="Interval Kepercayaan 95%"
)

plt.axvline(
    lower,
    color='red',
    linestyle='--',
    label=f'Batas bawah = {lower}'
)

plt.axvline(
    mean,
    color='green',
    label=f'Mean = {mean}'
)

plt.axvline(
    upper,
    color='red',
    linestyle='--',
    label=f'Batas atas = {upper}'
)

plt.title("Grafik Distribusi Normal untuk Interval Kepercayaan 95%")
plt.xlabel("Nilai Rata-rata Produktivitas")
plt.ylabel("Kepadatan Probabilitas")

plt.grid(True)
plt.legend()

plt.savefig(
    "Distribusi_Normal_95.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()