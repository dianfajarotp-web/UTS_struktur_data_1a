# Proyek 1a - Sistem Manajemen Inventaris Produk E-Commerce

Repositori ini berisi kode program Python untuk memenuhi tugas Proyek 1 (Skenario Studi Kasus 1) pada mata kuliah Struktur Data, Program Studi Teknik Informatika, Fakultas Sains dan Teknologi, UIN Sultan Syarif Kasim Riau.

## Identitas Mahasiswa
* **Nama:** Dian Fajar[cite: 1]
* **NIM:** [Isi NIM Anda]
* **Program Studi:** Teknik Informatika

## Deskripsi Program
Program ini dikembangkan untuk membangun purwarupa "Sistem Manajemen Inventaris Produk" bagi perusahaan e-commerce berskala besar. Program ini mengimplementasikan struktur data **Hash Table** (Python `dict`) sebagai pilihan utama karena memiliki kecepatan akses konstan rata-rata **$O(1)$** untuk menangani jutaan data produk.

Repositori ini dibagi menjadi dua modul utama:
1. **`inventaris_cli.py`**: Program utama berbasis *Command Line Interface* (CLI) murni menggunakan struktur data *Hash Table* (`dict`) untuk mencakup fungsi penyisipan (`insert`), pencarian (`search`), penghapusan (`delete`), dan tampilan inventaris.
2. **`pengukuran_kompleksitas.py`**: Modul eksperimen simulasi dan *benchmark* waktu eksekusi (`time`) untuk membandingkan performa operasi antara **Hash Table** (`dict`), **Array-based List** (`list`), dan **Custom Linked List** guna menjawab tabel perbandingan kompleksitas.

## Cara Menjalankan Program
Pastikan Python sudah terinstal di komputer Anda, lalu jalankan perintah berikut di terminal:

### 1. Menjalankan Sistem Inventaris CLI Utama
```bash
python inventaris_cli.py