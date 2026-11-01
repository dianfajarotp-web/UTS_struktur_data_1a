import time
import random

class ProdukNode:
    """Node untuk Custom Linked List"""
    def __init__(self, id_produk, nama, harga):
        self.id_produk = id_produk
        self.nama = nama
        self.harga = harga
        self.next = None

class CustomLinkedList:
    """Implementasi Custom Linked List untuk Eksperimen"""
    def __init__(self):
        self.head = None

    def insert(self, id_produk, nama, harga):
        new_node = ProdukNode(id_produk, nama, harga)
        new_node.next = self.head
        self.head = new_node

    def search(self, target_id):
        curr = self.head
        while curr:
            if curr.id_produk == target_id:
                return curr
            curr = curr.next
        return None

    def delete(self, target_id):
        curr = self.head
        prev = None
        while curr:
            if curr.id_produk == target_id:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False


def jalankan_benchmark():
    print("="*70)
    print(f"{'SIMULASI PENGUKURAN WAKTU EKSEKUSI (BENCHMARK)':^70}")
    print("="*70)
    
    # Jumlah data uji coba (misal: 10.000 data produk)
    n_data = 10000
    id_cari = f"P{n_data // 2:05d}" # ID yang dicari berada di tengah/akhir
    
    # 1. PERSIAPAN DATA (DUMMY DATA)
    list_data_mentah = [(f"P{i:05d}", f"Produk ke-{i}", random.randint(10000, 1000000)) for i in range(n_data)]
    
    # --- A. HASH TABLE (Python dict) ---
    print(f"\n[1] Menguji Struktur Data: HASH TABLE (Python dict)")
    hash_table = {}
    
    # Ukur Waktu Insert Hash Table
    start_time = time.perf_counter()
    for id_p, nama, harga in list_data_mentah:
        hash_table[id_p] = {"nama": nama, "harga": harga}
    end_time = time.perf_counter()
    waktu_insert_dict = (end_time - start_time) * 1000 # dalam milidetik
    print(f"    - Waktu Insert {n_data} data: {waktu_insert_dict:.4f} ms (Kompleksitas O(1))")
    
    # Ukur Waktu Search Hash Table
    start_time = time.perf_counter()
    _ = hash_table.get(id_cari)
    end_time = time.perf_counter()
    waktu_search_dict = (end_time - start_time) * 1000
    print(f"    - Waktu Search 1 data : {waktu_search_dict:.6f} ms (Kompleksitas O(1))")

    # Ukur Waktu Delete Hash Table
    start_time = time.perf_counter()
    hash_table.pop(id_cari, None)
    end_time = time.perf_counter()
    waktu_delete_dict = (end_time - start_time) * 1000
    print(f"    - Waktu Delete 1 data : {waktu_delete_dict:.6f} ms (Kompleksitas O(1))")


    # --- B. ARRAY-BASED LIST (Python list) ---
    print(f"\n[2] Menguji Struktur Data: ARRAY-BASED LIST (Python list)")
    array_list = []
    
    # Ukur Waktu Insert List (append di akhir)
    start_time = time.perf_counter()
    for id_p, nama, harga in list_data_mentah:
        array_list.append((id_p, nama, harga))
    end_time = time.perf_counter()
    waktu_insert_list = (end_time - start_time) * 1000
    print(f"    - Waktu Insert {n_data} data: {waktu_insert_list:.4f} ms (Kompleksitas O(1) amortized)")
    
    # Ukur Waktu Search List (Linear Search)
    start_time = time.perf_counter()
    hasil_cari_list = None
    for item in array_list:
        if item[0] == id_cari:
            hasil_cari_list = item
            break
    end_time = time.perf_counter()
    waktu_search_list = (end_time - start_time) * 1000
    print(f"    - Waktu Search 1 data : {waktu_search_list:.4f} ms (Kompleksitas O(N))")

    # Ukur Waktu Delete List
    start_time = time.perf_counter()
    for i, item in enumerate(array_list):
        if item[0] == id_cari:
            array_list.pop(i)
            break
    end_time = time.perf_counter()
    waktu_delete_list = (end_time - start_time) * 1000
    print(f"    - Waktu Delete 1 data : {waktu_delete_list:.4f} ms (Kompleksitas O(N))")


    # --- C. CUSTOM LINKED LIST ---
    print(f"\n[3] Menguji Struktur Data: CUSTOM LINKED LIST")
    linked_list = CustomLinkedList()
    
    # Ukur Waktu Insert Linked List (sisip di depan / head insertion)
    start_time = time.perf_counter()
    for id_p, nama, harga in list_data_mentah:
        linked_list.insert(id_p, nama, harga)
    end_time = time.perf_counter()
    waktu_insert_ll = (end_time - start_time) * 1000
    print(f"    - Waktu Insert {n_data} data: {waktu_insert_ll:.4f} ms (Kompleksitas O(1))")
    
    # Ukur Waktu Search Linked List
    start_time = time.perf_counter()
    _ = linked_list.search(id_cari)
    end_time = time.perf_counter()
    waktu_search_ll = (end_time - start_time) * 1000
    print(f"    - Waktu Search 1 data : {waktu_search_ll:.4f} ms (Kompleksitas O(N))")

    # Ukur Waktu Delete Linked List
    start_time = time.perf_counter()
    linked_list.delete(id_cari)
    end_time = time.perf_counter()
    waktu_delete_ll = (end_time - start_time) * 1000
    print(f"    - Waktu Delete 1 data : {waktu_delete_ll:.4f} ms (Kompleksitas O(N))")

    print("\n" + "="*70)
    print("Eksperimen selesai! Gunakan angka perbandingan di atas untuk mengisi Tabel 4 & 5.")
    print("="*70)

if __name__ == "__main__":
    jalankan_benchmark()