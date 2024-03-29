# -*- coding: utf-8 -*-
"""SC61717_Rahel Cecilia Purba_Python Foundation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RufTbVlCXzp7WRyyJ5IZJLraJllgk2VV

#Tugas Python Foundation Kelompok Second Choice(2)

#Import data
"""

import pandas as pd

bmi_dataset = ('/content/Dataset_Kompi17_Assignment1.csv')

df = pd.read_csv(bmi_dataset)

df

"""# 1.1 Identifikasi dan jelaskan tipe data apa saja yang ada pada dataframe, ada berapa kolom dan baris, serta informasi apa saja yang terkandung dalam data tersebut?

Dalam data tersebut terdiri dari beberpa kolom yang berisiskan no. peserta, nama, jurusan, berat badan, dan tinggi badan. tipe data pada kolom no. peserta, berat badan, dan tinggi badan adalah integer sedangkan kolom nama dan jurusan memiliki tipe data string. jumlah baris pada data tersebut adalah 25 baris dan 5 kolom
"""

df.info()

"""# 1.2 Hitunglah BMI setiap siswa dengan rumus BMI."""

df['BMI'] = df.iloc[:, 3] / (df.iloc[:, 4] / 100) **2

df.iloc[:, [1, 5]]

"""# 1.3 Buatlah program untuk menghitung BMI!"""

berat_badan = int(input("Berat Badan :"))
tinggi_badan = int(input("Tinggi Badan :"))

if(berat_badan >0 and tinggi_badan >0):
  bmi = berat_badan / ((tinggi_badan/100)**2)
  print("BMI :", bmi)
  if bmi <18.5:
    print("Status : Underweight")
  if 18.5<= bmi <25 :
    print("Status : Normal")
  if 25 <= bmi <30 :
    print("Status : Overweight")
  if 30<= bmi < 35 :
    print("Status : Obesity")

"""# 1.4 Update dataframe df dengan menambahkan hasil perhitungan soal nomor 2, beri nama kolom BMI."""

df['BMI'] = df.iloc[:, 3] / (df.iloc[:, 4] / 100) **2

df

"""# 1.5 Buatlah status BMI untuk setiap siswa dari kategoti berikut, lalu simpan data statusnya dengan nama kolom status BMI."""

def status_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obesity'

# Menambahkan kolom baru untuk status BMI
df['Status BMI'] = df['BMI'].apply(status_bmi)
df

"""# 1.6

a. Buatlah variabel baru lalu urutkan data berdasarkan tinggi badan dari yang tertinggi ke rendah
"""

df_tinggi_desc = df.sort_values(by=df.columns[4], ascending=False)
df_tinggi_desc

"""b. Buat variabel baru lalu urutkan data berdasarkan nama dari Z-A"""

df_nama_desc = df.sort_values(by=df.columns[1], ascending=False)
df_nama_desc

"""# 1.7 Filter dataframe df berdasarkan :

a. Status BMI di luar normal
"""

non_normal = df[(df.iloc[:, 6] != 'Normal')]
non_normal

"""b. Tinggi badan > 169 cm dan berat badan > 60 kg"""

tinggi_berat = df[(df.iloc[:, 4] > 169) & (df.iloc[:, 3] > 60)]
tinggi_berat

"""c. Nama yang mengandung huruf "y"
"""

nama_y = df[df.iloc[:, 1].str.contains('y')]
nama_y

"""d. Siapa saja yang berat badannya kurang dari 60 kg?"""

kurang_berat = df[(df.iloc[:, 3] < 60)]
kurang_berat

"""# 1.8 Tambahkan nomor urut pada dataframe df sesuai jumlah siswa dan tempatkan kolom nomor baru tersebut di paling ujung kiri sebagai kolom pertama serta beri nama kolomnya "No."
"""

nomor = range(1, len(df) + 1)
df.insert(0, 'No.', nomor)
df

"""# 1.9 Cari nilai-nilai berikut :

a. Cari nilai terendah dan tertingginya
"""

print("Berat Badan Tertinggi:", df.iloc[:, 4].max())
print("Berat Badan Terendah:", df.iloc[:, 4].min())
print("Tinggi Badan Tertinggi:", df.iloc[:, 5].max())
print("Tinggi Badan Terendah:", df.iloc[:, 5].min())
print("Nilai BMI Tertinggi:", df.iloc[:, 6].max())
print("Nilai BMI Terendah:", df.iloc[:, 6].min())

"""b. Berapa nilai rata-rata tinggi badan siswa"""

print("Rata-rata Tinggi Badan Siswa:", df.iloc[:, 5].mean())

"""c. Berapa rata-rata berat badan siswa"""

print("Rata-rata Berat Badan Siswa:", df.iloc[:, 4].mean())

"""d. Ada berapa orang jumlah siswa yang tercatatpada dataframe df?"""

print("Jumlah Siswa Dalam DataFrame:", len(df))

"""e. 5 orang dengan nilai BMI tertinggi"""

df.nlargest(5,"BMI")

"""f. Ada berapa orang yang tergolong status underweight, normal, overweight, dan obesity"""

status_kategori = df.iloc[:, 7].value_counts()

print("Status BMI dan Jumlah Data:")
status_kategori

"""# 2.2


"""

modal_investasi = int(input('Modal Investasi : '))
tahun_investasi = int(input('Jangka Waktu Investasi (tahun) : '))
investasi = 0.25
if modal_investasi > 0 and modal_investasi <= 1000000000 and tahun_investasi > 0:
    for tahun in range(1, tahun_investasi + 1):
        investasi_tahun_ini = modal_investasi * ((1 + investasi) ** tahun)
        print("Tahun ke-", tahun, ", total investasi kamu", investasi_tahun_ini)
else :
  print("Input tidak valid, modal haruslah berada di antara 0 hingga 1 miliar dan tahun investasi harus lebih dari 0 tahun")