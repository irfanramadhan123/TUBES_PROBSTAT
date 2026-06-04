import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Derajat bebas
df = 49

# Nilai x untuk kurva Chi-Square
x = np.linspace(20, 90, 1000)

# PDF Chi-Square
y = chi2.pdf(x, df)

# Nilai kritis untuk CI 90%
chi_left = chi2.ppf(0.05, df)
chi_right = chi2.ppf(0.95, df)

plt.figure(figsize=(10,6))

# Kurva Chi-Square
plt.plot(
    x,
    y,
    color='darkorange',
    linewidth=3,
    label="Distribusi Chi-Square"
)

# Area kepercayaan 90%
plt.fill_between(
    x,
    y,
    where=(x >= chi_left) & (x <= chi_right),
    color='gold',
    alpha=0.4,
    label="Daerah Kepercayaan 90%"
)

# Garis batas kiri
plt.axvline(
    chi_left,
    color='red',
    linestyle='--',
    linewidth=2,
    label=f'χ² kiri = {chi_left:.2f}'
)

# Garis batas kanan
plt.axvline(
    chi_right,
    color='red',
    linestyle='--',
    linewidth=2,
    label=f'χ² kanan = {chi_right:.2f}'
)

plt.title("Distribusi Chi-Square untuk Interval Kepercayaan 90%")
plt.xlabel("Nilai χ²")
plt.ylabel("Kepadatan Probabilitas")

plt.grid(True, alpha=0.3)
plt.legend()

plt.savefig(
    "Chi_Square_90.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()