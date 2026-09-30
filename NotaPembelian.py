#Program Membuat Nota Pembelian
#I.S.: pengguna memasukkan no. transaksi, tanggal dan ketiga data barang yang dibeli oleh seorang pelanggan
#F.S.: menampilkan nota pembelian

import subprocess
subprocess.run('cls', shell = True)

#badan program
#memasukkan nomor transaksi pembelian dan tanggal beli
no_transaksi = str(input('no. transaksi : '))
tanggal      = str(input('tanggal       : '))
print('------------------------------\n')

#memasukkan tiga data barang yang dibeli
print('<< DATA PEMBELIAN BARANG >>')
print('Data Barang Ke-1')
print('----------------')
kode_brg1     = str(input('Kode Barang : '))
nama_brg1     = str(input('Nama Barang : '))
jumlah_beli1  = int(input('Jumlah Beli : '))
harga_satuan1 = int(input('Harga Satuan : Rp. '))
#menghitung harga total barang kesatu
harga_total1 = jumlah_beli1 * harga_satuan1
#menampilkan harga total barang kesatu
print(f'Harga Total : Rp. {harga_total1}\n')

print('Data Barang Ke-2')
print('----------------')
kode_brg2     = str(input('Kode Barang : '))
nama_brg2     = str(input('Nama Barang : '))
jumlah_beli2  = int(input('Jumlah Beli : '))
harga_satuan2 = int(input('Harga Satuan : Rp. '))
#menghitung harga total barang kedua
harga_total2 = jumlah_beli2 * harga_satuan2
#menampilkan harga total barang kedua
print(f'Harga Total : Rp. {harga_total2}\n')

print('Data Barang Ke-3')
print('----------------')
kode_brg3     = str(input('Kode Barang : '))
nama_brg3     = str(input('Nama Barang : '))
jumlah_beli3  = int(input('Jumlah Beli : '))
harga_satuan3 = int(input('Harga Satuan : Rp. '))
#menghitung harga total barang ketiga
harga_total3 = jumlah_beli3 * harga_satuan3
#menampilkan harga total barang ketiga
print(f'Harga Total : Rp. {harga_total3}\n')

#menghitung total pembelian
total_pembelian = harga_total1 + harga_total2 + harga_total3
print(f'Total Pembelian : Rp. {total_pembelian:,}')