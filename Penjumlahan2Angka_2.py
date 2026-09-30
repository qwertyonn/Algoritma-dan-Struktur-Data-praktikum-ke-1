#Program Penjumlahan Dua Buah Angka
#I.S.: diberikan harga ke dalam variabel angka1 = 5 dan angka2 = 2
#F.s.: menampilkan hasil penjumlahan
import subprocess
subprocess.run('cls', shell = True)

#badan program
#memasukan dua angka secara langsung
angka1 = int(input('Masukan Angka Ke-1 = '))
angka2 = int(input('Masukan Angka Ke-2 = '))

#menjumlahkan dua angka
hasil = angka1 + angka2

#menampilkan hasil penjumlahan
print(f'Hasil Penjumlahan = {angka1} + {angka2}')
print(f'                  = {hasil}')