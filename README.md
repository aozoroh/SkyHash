# SKY - Hash Cracker Tool v1.0

SKY-HashCracker adalah sebuah perkakas berbasis CLI (*Command-Line Interface*) yang dirancang khusus menggunakan bahasa pemrograman Python untuk melakukan pembongkaran kode rahasia (*brute-force hash decryption*) berjenis MD5. 

Alat ini bekerja secara cerdas dan efisien dengan mencocokkan nilai *hash* target terhadap ribuan kata sandi dari sebuah daftar kata (*wordlist*) secara akurat.

## ✨ Fitur Utama
- **Fast Brute-Force Encription**: Melakukan konversi teks massal menggunakan pustaka optimal berbasis mesin Python.
- **Robust CLI Arguments**: Dikendalikan sepenuhnya dari luar terminal memanfaatkan pustaka `argparse` sehingga tidak perlu mengubah isi kode program.
- **Cross-Platform Compatibility**: Dilengkapi dengan fitur pembersihan otomatis karakter enter bawaan Windows (`\r`) sehingga berkas *wordlist* dari sistem operasi apa pun (Windows, Linux, Mac) dapat terbaca dengan lancar.
- **Interactive UI Colors**: Visualisasi terminal yang estetik memanfaatkan kombinasi warna dan ketebalan teks dari pustaka `colorama`.
- **Graceful Interruption handling**: Mengantisipasi pembatalan darurat pengguna (`Ctrl + C`) secara halus tanpa memicu eror sistem *crash*.

## 🛠️ Daftar Pustaka (Dependencies) & Instalasi

Pastikan komputer Anda sudah terinstal Python. Pasang pustaka pihak ketiga yang diperlukan dengan menjalankan perintah berikut di terminal Anda:

```bash
pip install colorama
```

*Catatan: Modul `argparse`, `hashlib`, dan `sys` yang digunakan di dalam kode adalah pustaka bawaan standar Python, sehingga tidak memerlukan instalasi tambahan.*

## 🚀 Cara Penggunaan

1. Sediakan sebuah berkas teks daftar kata sandi (misalnya diberi nama `wordlist.txt`) di dalam folder yang sama dengan skrip. Contoh isi file:
   ```text
   password123
   skynet
   admin
   hacker
   ```
2. Jalankan skrip melalui terminal atau command prompt dengan memasukkan kode *hash* target dan lokasi berkas *wordlist*:

```bash
python index.py [KODE_HASH_TARGET] -w [NAMA_FILE_WORDLIST]
```

### 🎯 Contoh Pengujian Berhasil:
Jika ingin menebak kata di balik kode hash milik kata `hacker` (`d6a6bc0db10694a2d90e3a69648f3a03`), ketik perintah berikut:
```bash
python index.py d6a6bc0db10694a2d90e3a69648f3a03 -w wordlist.txt
```

**Output Terminal:**
```text
[*] Memulai brute-force hash: d6a6bc0db10694a2d90e3a69648f3a03...
[+] KATA SANDI DITEMUKAN: hacker
```

## 📝 Catatan Edukasi
Alat ini dibangun murni untuk tujuan pembelajaran, edukasi, dan pengujian keamanan internal yang sah (*Authorized Penetration Testing*). Segala bentuk penyalahgunaan alat ini di luar aktivitas yang legal adalah tanggung jawab pengguna masing-masing.

---

## 💙 Penutup & Dukungan
Terima kasih banyak telah mencoba dan menggunakan alat **SKY-HashCracker** ini! Proyek ini menjadi salah satu bukti perjalanan saya dalam mendalami dunia pemrograman Python dan keamanan siber.

Jika Anda menyukai proyek ini, silakan berikan dukungan dengan mengeklik tombol **Star (⭐)** di pojok kanan atas repositori ini. Tetap semangat belajar dan mari terus melangkah lebih jauh! 🚀🔥

*Happy Coding & Stay Safe!* 🌤️💻✨