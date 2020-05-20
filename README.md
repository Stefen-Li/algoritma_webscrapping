# Pergerakan Kurs JPY Tahun 2019
Pada analisa kali ini, kita akan mengamati pergerakan kurs JPY selama tahun 2019 untuk menentukan apakah JPY merupakan mata uang asing yang baik sebagai alat investasi.

## Pengumpulan Data
Pengumpulan data dapat dilakukan dalam beberapa tahap berikut:
- Menentukan situs yang akan diambil datanya, dan kali ini kita mengambil dari https://monexnews.com/
- Mengambil cuplikan kode html-nya
- Merapikan kode html menggunakan package BeautifulSoup
- Seleksi bagian yang akan kita ambil dengan menggunakan method find() dan find_all()
- Menggunakan looping untuk method find_all untuk mendapatkan semua data yang ada
- Karena data tanggal yang diperoleh berbentuk "31\xa0Desember\xa02019", maka kita dapat menghapus "\xa0" tersebut dengan menggunakan fungsi replace().

## Pengolahan Data
Pengolahan data dapat dilakukan dalam beberapa tahap berikut:
- Masukkan data-data yang sudah diperoleh ke dalam sebuah DataFrame yang terdiri dari Series Tanggal, KursJual, dan KursBeli
- Karena pd.to_dateime tidak dapat membaca tanggal dalam Bahasa Indonesia, maka kita perlu mengubah nilai dalam Series Tanggal kedalam Bahasa Inggris terlebih dahulu menggunakan fungsi replace()
- Mengganti tipe data masing-masing Series sesuai dengan nilainya
- Mengevaluasi pergerakan kurs JPY dengan mengamati rata-rata bulanan dari harga kurs jual dan kurs beli
- Membuat sebuah grafik yang menggambarkan pergerakan kurs JPY untuk memudahkan kita dalam membacanya.

## Kesimpulan
Apabila kita amati grafik pergerakan kurs JPY, nilai kurs jual dan kurs beli cenderung turun dalam kurun waktu 1 tahun. Jika kita membeli Yen pada bulan Januari 2019 dan menjualnya kembali pada bulan Desember 2019, maka akan kita dapati nilai tukarnya menurun sehingga kita mengalami kerugian. Dengan demikian, berdasarkan analisa kita terhadap pergerakan kurs JPY tahun 2019 dapat disimpulkan bahwa uang Yen tidak bisa kita gunakan sebagai alat investasi.
