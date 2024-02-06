# Implementation_ETL

# DATA
Data diambil dari sumber 'https://storage.googleapis.com/dqlab-dataset/dqthon-participants.csv'

# kode pos
kode pos diambil dari alamat peserta (kolom address) yang berada pada bagian paling akhir

# city
kolom baru bernama city didapat dari kolom address. Diasumsikan kota merupakan sekumpulan karakter yang terdapat setelah nomor jalan diikuti dengan \n (newline character) atau dalam bahasa lainnya yaitu enter.

# github_profile 
kolom baru github_profile yang merupakan link profil github dari peserta.
profil github mereka merupakan gabungan dari first_name dan last_name yang sudah di-lowercase. 

# Phone number
Jika awalan nomor HP berupa angka 62 atau +62 yang merupakan kode telepon Indonesia, maka diterjemahkan ke 0.
Tidak ada tanda baca seperti kurung buka, kurung tutup, strip⟶ ()-
Tidak ada spasi pada nomor HP nama kolom untuk menyimpan hasil cleansing pada nomor HP yaitu cleaned_phone_number

# team name
nama tim merupakan gabungan nilai dari kolom first_name, last_name, country dan institute.

# email
Format email:
xxyy@aa.bb.[ac/com].[cc]

Keterangan:
xx -> nama depan (first_name) dalam lowercase
yy -> nama belakang (last_name) dalam lowercase
aa -> nama institusi

Untuk nilai bb, dan cc mengikuti nilai dari aa. Aturannya:
- Jika institusi nya merupakan Universitas, maka
  bb -> gabungan dari huruf pertama pada setiap kata dari nama Universitas dalam lowercase
  Kemudian, diikuti dengan .ac yang menandakan akademi/institusi belajar dan diikuti dengan pattern cc
- Jika institusi bukan merupakan Universitas, maka
  bb -> gabungan dari huruf pertama pada setiap kata dari nama Universitas dalam lowercase
  Kemudian, diikuti dengan .com. Perlu diketahui bahwa pattern cc tidak berlaku pada kondisi ini

cc -> merupakan negara asal peserta, adapun aturannya:
- Jika banyaknya kata pada negara tersebut lebih dari 1 maka ambil singkatan dari negara tersebut dalam lowercase
- Namun, jika banyaknya kata hanya 1 maka ambil 3 huruf terdepan dari negara tersebut dalam lowercase
Contoh:
Nama depan: Citra
Nama belakang: Nurdiyanti
Institusi: UD Prakasa Mandasari
Negara: Georgia
Maka,Email nya: citranurdiyanti@upm.geo


Nama depan: Aris
Nama belakang: Setiawan
Institusi: Universitas Diponegoro
Negara: Korea Utara
Maka, Email nya: arissetiawan@ud.ac.ku

  # tanggal lahir
format YYYY-MM-DD dengan keterangan:

YYYY: 4 digit yang menandakan tahun
MM: 2 digit yang menandakan bulan
DD: 2 digit yang menandakan tanggal