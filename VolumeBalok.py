#Program Menghitung Volume Balok
#I.S.: Pengguna memasukan panjang, lebar dan tinggi balon dalam satuan inci
#F.s.: Menampilkan volume balok dalam satuan sentimeter kubik

import subprocess
subprocess.run('cls', shell = True)

#badan program
#memasukan panjang, lebar dan tinggi
panjang = int(input('Masukan Panjang Balok = '))
lebar   = int(input('Masukan Lebar Balok   = '))
tinggi  = int(input('Masukan Tinggi Balok  = '))

#menghitung volume balok
volume_balok = panjang * lebar * tinggi * 2.54 ** 3

#menampilkan hasil perhitungan
print(f'Volume Balok      = {volume_balok:.2f} cm3')