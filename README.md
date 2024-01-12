## Eksploiter Apache HTTP Server Request Smuggling

### Deskripsi
Program ini mengeksploitasi kerentanan HTTP Request Smuggling pada Apache HTTP Server versi 2.4.0 hingga 2.4.55. Kerentanan muncul dari konfigurasi yang salah pada mod_proxy saat dikombinasikan dengan RewriteRule atau ProxyPassMatch, menyebabkan potensi serangan Request Smuggling. Ini dapat mengakibatkan melewati kontrol akses pada server proxy, memproksi URL yang tidak dimaksudkan ke server asal, dan racun cache. Pengguna disarankan untuk memperbarui setidaknya ke versi 2.4.56 dari Apache HTTP Server.

### Cara Kerja
Bayangkan server sebagai penjaga pintu dan konfigurasi yang salah sebagai celah dalam sistem keamanannya. Program ini memanfaatkan celah-celah ini untuk menipu penjaga pintu agar menangani permintaan secara tidak benar, berpotensi memungkinkan akses tanpa izin atau menyebabkan masalah keamanan lainnya.

### Cara Menjalankan
1. Pastikan Anda memiliki Python terinstal.
2. Unduh program.
3. Buka terminal dan arahkan ke direktori program.
4. Jalankan program dengan perintah `python http-request-smuggling.py`.

### Tujuan
Program ini dibuat untuk tujuan pendidikan guna menunjukkan potensi risiko keamanan pada versi Apache HTTP Server yang salah konfigurasi. Gunakan dengan bijak dan hanya pada sistem yang Anda miliki izinnya.

### Penulis
ifulxploit  
Email: ifulxploit@gmail.com

**Catatan: Program ini hanya untuk tujuan pendidikan. Harap gunakan dengan etika dan tanggung jawab.**

---
