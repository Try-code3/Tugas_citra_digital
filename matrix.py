Tugas 1 Pengolahan Citra Digital
# Perkalian Matriks Array 3 Dimensi

A = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

B = [
    [
        [9, 10],
        [11, 12]
    ],
    [
        [13, 14],
        [15, 16]
    ]
]

# Menyimpan hasil
C = []

# Perkalian setiap matriks
for k in range(len(A)):
    hasil = []

    for i in range(len(A[k])):
        baris = []

        for j in range(len(B[k][0])):
            jumlah = 0

            for x in range(len(B[k])):
                jumlah += A[k][i][x] * B[k][x][j]

            baris.append(jumlah)

        hasil.append(baris)

    C.append(hasil)

# Menampilkan hasil
print("Hasil Perkalian Matriks:")

for k in range(len(C)):
    print(f"\nMatriks {k + 1}:")
    for baris in C[k]:
        print(baris)
