# Tarik-Data-Dari-OLX-Indonesia
 Berikut adalah script baik dari selenium ataupun request untuk mengambil data dari OLX.
 
 Sepertinya dari pihak OLX hanya memberikan data sebanyak 500 iklan (25 page). Setelah melakukan scroll sebanyak 25x, tombol untuk memuat kembali menjadi tidak ada. Meskipun jumlah iklan melebihi 500.

 Metode yang disarankan untuk mengambil data dari OLX adalah menggunakan metode request terhadap API milik OLX.
 Keuntungan:
 - Lebih cepat dan lebih mudah.
 - Data lebih banyak yang bisa didapat.
 Kelemahan:
 - Sulit untuk menemukan link ke semua iklan. Namun, kita dapat mengakses foto dan deskripsi besarnya tanpa perlu membuka iklan tersebut.

 Keuntungan menggunakan selenium:
 - Bisa mendapatkan link ke setiap iklan. Link yang dimaksud adalah link yang tertanam di javascript setiap kotak iklan.
 Kelemahan:
 - Data yang didapat sebenarnya jauh lebih sedikit dibandingkan request dan jauh lebih berat.
 - Metode lain yang dapat digunakan adalah menggabungkan selenium dengan scrapy.
