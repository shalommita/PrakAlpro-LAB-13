# Shalommita P ---- 71200640

# Soal
# Buat fungsi rekursif Python yang menghitung angka dengan membagi angka dengan pembaginya
# Angka yang kita tentukan akan dibagi dengan angka dari 1 ke angka itu sendiri
# dan di akhir fungsi akan mengembalikan angka itu sendiri

def pembagian(angka,pembagi):
    if angka%pembagi==0:
        print(pembagi)
    elif angka==pembagi:
        return angka
    return pembagian(angka,pembagi+1)

print(pembagian(63,1))
