import matplotlib.pyplot as plt

durasi_tidur = [
7,6,6,5.5,5,5,6,4,7,6,
4,7,5,7,4,8,6,5,5,7,
6,5,6,6,6,5,5.5,5,4,7,
5,5,6,7,7,6,8,4,5,2,
7,7,3,7,6,6,6,6,6,5
]

plt.figure(figsize=(8,5))

plt.hist(
    durasi_tidur,
    bins=7,
    edgecolor='black'
)

plt.title("Histogram Durasi Tidur Mahasiswa ITERA")
plt.xlabel("Durasi Tidur (Jam)")
plt.ylabel("Frekuensi")

plt.grid(True)

plt.savefig(
    "Histogram_Tidur.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()