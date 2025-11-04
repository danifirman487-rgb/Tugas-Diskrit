import itertools

# Definisi fungsi implikasi
def implies(p, q):
    return (not p) or q

# Header tabel
print(f"{'p':<5}{'q':<5}{'p and q':<10}{'p or q':<10}{'¬p':<5}{'p → q':<8}")

# Iterasi semua kombinasi p dan q (True/False)
for p, q in itertools.product([True, False], repeat=2):
    print(f"{str(p):<5}{str(q):<5}{str(p and q):<10}{str(p or q):<10}{str(not p):<5}{str(implies(p, q)):<8}")

# Fungsi untuk mengecek apakah bilangan ganjil
def is_odd(n):
    return n % 2 == 1

# Pembuktian dengan kontradiksi
def proof_by_contradiction():
    for n in range(1, 10):
        if is_odd(n**2) and not is_odd(n):
            print(f"Kontradiksi ditemukan pada n={n}!")
            return False
    print("Tidak ada kontradiksi ditemukan -> pernyataan benar: jika n² ganjil maka n ganjil.")
    return True

# Panggil fungsi pembuktian
proof_by_contradiction()