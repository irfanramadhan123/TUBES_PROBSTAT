import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

df = 49

x = np.linspace(20, 90, 1000)

y = chi2.pdf(x, df)

chi_left = chi2.ppf(0.025, df)
chi_right = chi2.ppf(0.975, df)

plt.figure(figsize=(10,6))

plt.plot(
    x,
    y,
    color='darkorange',
    linewidth=3,
    label="Distribusi Chi-Square"
)

plt.fill_between(
    x,
    y,
    where=(x >= chi_left) & (x <= chi_right),
    color='gold',
    alpha=0.4,
    label="Daerah Kepercayaan 95%"
)

plt.axvline(
    chi_left,
    color='red',
    linestyle='--',
    linewidth=2,
    label=f'χ² kiri = {chi_left:.2f}'
)

plt.axvline(
    chi_right,
    color='red',
    linestyle='--',
    linewidth=2,
    label=f'χ² kanan = {chi_right:.2f}'
)

plt.title("Distribusi Chi-Square untuk Interval Kepercayaan 95%")
plt.xlabel("Nilai χ²")
plt.ylabel("Kepadatan Probabilitas")

plt.grid(True, alpha=0.3)
plt.legend()

plt.savefig(
    "Chi_Square_95.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()