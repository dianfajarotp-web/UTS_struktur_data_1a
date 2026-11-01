class Produk:
    """Kelas untuk merepresentasikan entitas data produk e-commerce."""
    def __init__(self, id_produk: str, nama_produk: str, kategori: str, harga: float, stok: int):
        self.id_produk = id_produk
        self.nama_produk = nama_produk
        self.kategori = kategori
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return f"ID: {self.id_produk} | Nama: {self.nama_produk} | Kategori: {self.kategori} | Harga: Rp{self.harga:,.2f} | Stok: {self.stok} unit"


class InventarisEcommerce:
    """
    Sistem Manajemen Inventaris menggunakan Hash Table (Python dict) 
    sebagai struktur data utama terpilih dengan kompleksitas O(1).
    """
    def __init__(self):
        # Menggunakan dictionary: key = id_produk, value = objek Produk
        self.data_inventaris = {}

    def insert_produk(self, produk: Produk) -> bool:
        """Menambahkan produk baru (Insert - O(1))"""
        if produk.id_produk in self.data_inventaris:
            print(f"[!] Gagal: Produk dengan ID '{produk.id_produk}' sudah terdaftar.")
            return False
        self.data_inventaris[produk.id_produk] = produk
        print(f"[Sukses] Produk '{produk.nama_produk}' berhasil ditambahkan ke inventaris.")
        return True

    def search_produk(self, id_produk: str) -> Produk:
        """Mencari detail produk berdasarkan ID Produk (Search - O(1))"""
        # Akses langsung melalui key dictionary berkecepatan konstan O(1)
        return self.data_inventaris.get(id_produk, None)

    def delete_produk(self, id_produk: str) -> bool:
        """Menghapus produk dari peredaran pasar (Delete - O(1))"""
        if id_produk in self.data_inventaris:
            produk_dihapus = self.data_inventaris.pop(id_produk)
            print(f"[Sukses] Produk '{produk_dihapus.nama_produk}' (ID: {id_produk}) berhasil dihapus dari sistem.")
            return True
        print(f"[!] Gagal: Produk dengan ID '{id_produk}' tidak ditemukan di sistem.")
        return False

    def tampilkan_semua(self):
        """Menampilkan seluruh daftar inventaris produk"""
        if not self.data_inventaris:
            print("\n[!] Inventaris produk saat ini masih kosong.")
            return
        print("\n" + "="*80)
        print(f"{'DAFTAR INVENTARIS PRODUK E-COMMERCE (HASH TABLE)':^80}")
        print("="*80)
        for produk in self.data_inventaris.values():
            print(produk)
        print("="*80)


# Program Utama berbasis Command Line Interface (CLI)
def main():
    inventaris = InventarisEcommerce()
    
    # Data awal simulasi produk
    inventaris.insert_produk(Produk("P001", "Laptop Gaming ASUS", "Elektronik", 15000000, 25))
    inventaris.insert_produk(Produk("P002", "Smartphone Samsung", "Elektronik", 4500000, 50))
    inventaris.insert_produk(Produk("P003", "Sepatu Sneakers Pria", "Fashion", 350000, 100))

    while True:
        print("\n--- SISTEM MANAJEMEN INVENTARIS E-COMMERCE (UTAMA) ---")
        print("1. Tambah Produk Baru (Insert)")
        print("2. Cari Detail Produk Berdasarkan ID (Search)")
        print("3. Hapus Produk (Delete)")
        print("4. Tampilkan Seluruh Produk")
        print("5. Keluar Program")
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == '1':
            print("\n--- TAMBAH PRODUK BARU ---")
            id_p = input("Masukkan ID Produk (contoh P004): ").strip()
            nama = input("Masukkan Nama Produk: ").strip()
            kat = input("Masukkan Kategori: ").strip()
            try:
                harga = float(input("Masukkan Harga (Rp): "))
                stok = int(input("Masukkan Jumlah Stok: "))
                produk_baru = Produk(id_p, nama, kat, harga, stok)
                inventaris.insert_produk(produk_baru)
            except ValueError:
                print("[!] Error: Harga dan Stok harus berupa angka valid.")
                
        elif pilihan == '2':
            print("\n--- CARI DETAIL PRODUK ---")
            id_Cari = input("Masukkan ID Produk yang dicari: ").strip()
            hasil = inventaris.search_produk(id_Cari)
            if hasil:
                print(f"[Ditemukan] -> {hasil}")
            else:
                print(f"[!] Produk dengan ID '{id_Cari}' tidak ditemukan.")
                
        elif pilihan == '3':
            print("\n--- HAPUS PRODUK ---")
            id_Hapus = input("Masukkan ID Produk yang ditarik dari pasar: ").strip()
            inventaris.delete_produk(id_Hapus)
            
        elif pilihan == '4':
            inventaris.tampilkan_semua()
            
        elif pilihan == '5':
            print("\nTerima kasih telah menggunakan Sistem Manajemen Inventaris E-Commerce!")
            break
        else:
            print("[!] Pilihan tidak valid. Silakan masukkan angka 1 sampai 5.")

if __name__ == "__main__":
    main()