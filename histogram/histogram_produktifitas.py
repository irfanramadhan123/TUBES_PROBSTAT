import matplotlib.pyplot as plt

produktivitas = [
3,3,3,3,4,3,3,2,3,2,
3,3,2,3,3,4,3,5,2,3,
2,3,3,3,3,3,3,2,4,3,
4,3,2,3,4,3,5,3,3,5,
4,3,2,3,5,3,2,3,3,4
]

plt.figure(figsize=(8,5))

plt.hist(
    produktivitas,
    bins=[1.5,2.5,3.5,4.5,5.5],
    edgecolor="black"
)

plt.title("Histogram Produktivitas Mahasiswa ITERA")
plt.xlabel("Skor Produktivitas")
plt.ylabel("Frekuensi")

plt.grid(True)

plt.savefig(
    "Histogram_Produktivitas.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()