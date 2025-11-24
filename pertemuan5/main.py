from abc import ABC, abstractmethod

class LibraryItem(ABC):
    """
    Abstract Base Class yang merepresentasikan item di perpustakaan.
    Class ini tidak bisa diinstansiasi secara langsung.
    """
    def __init__(self, title, item_id):
        self._title = title          # Protected attribute
        self.__item_id = item_id     # Private attribute (Encapsulation)
    @property
    def item_id(self):
        """Getter untuk mengakses private attribute __item_id"""
        return self.__item_id

    @property
    def title(self):
        """Getter untuk mengakses protected attribute _title"""
        return self._title

    @abstractmethod
    def get_details(self):
        """
        Abstract method yang WAJIB diimplementasikan oleh subclass.
        Ini adalah bentuk persiapan untuk Polymorphism.
        """
        pass

# SUBCLASS 1: Book
class Book(LibraryItem):
    """Class Buku yang mewarisi LibraryItem"""
    def __init__(self, title, item_id, author, isbn):
        super().__init__(title, item_id)
        self.author = author
        self.isbn = isbn

    def get_details(self):
        """Implementasi method abstract khusus untuk Buku"""
        return f"[Buku] {self.title} oleh {self.author} (ISBN: {self.isbn})"

# SUBCLASS 2: Magazine
class Magazine(LibraryItem):
    """Class Majalah yang mewarisi LibraryItem"""
    def __init__(self, title, item_id, issue, publisher):
        super().__init__(title, item_id)
        self.issue = issue
        self.publisher = publisher

    def get_details(self):
        """Implementasi method abstract khusus untuk Majalah"""
        return f"[Majalah] {self.title} Edisi: {self.issue} - Penerbit: {self.publisher}"

# CLASS MANAGER: Library
class Library:
    """Class untuk mengelola koleksi item perpustakaan"""
    def __init__(self):
        self._collection = [] # Encapsulation: List item bersifat protected

    def add_item(self, item: LibraryItem):
        """Menambahkan item ke dalam koleksi"""
        self._collection.append(item)
        print(f"Berhasil menambahkan: {item.title}")

    def show_items(self):
        """Menampilkan semua item yang tersedia"""
        print("\n=== Daftar Koleksi Perpustakaan ===")
        if not self._collection:
            print("Koleksi kosong.")
        else:
            for item in self._collection:
                # Polymorphism: Method get_details() menyesuaikan tipe objeknya
                print(f"ID: {item.item_id} | {item.get_details()}")

    def search_item(self, keyword):
        """Mencari item berdasarkan judul atau ID"""
        print(f"\n=== Hasil Pencarian: '{keyword}' ===")
        found = False
        for item in self._collection:
            # Mencari berdasarkan ID atau Judul 
            if keyword.lower() in item.title.lower() or keyword == str(item.item_id):
                print(f"Ditemukan: {item.get_details()}")
                found = True
        
        if not found:
            print("Item tidak ditemukan.")

# MAIN PROGRAM
if __name__ == "__main__":
    my_library = Library()

    # Membuat Objek Buku dan Majalah
    buku1 = Book("Belajar Python OOP", 101, "Guido van Rossum", "978-3-16-148410-0")
    buku2 = Book("Laskar Pelangi", 102, "Andrea Hirata", "978-979-3062-79-2")
    majalah1 = Magazine("National Geographic", 201, "Januari 2025", "NatGeo Society")

    # Menambahkan ke Perpustakaan
    my_library.add_item(buku1)
    my_library.add_item(buku2)
    my_library.add_item(majalah1)

    # Menampilkan Semua Item
    my_library.show_items()

    # Mencari Item
    my_library.search_item("Python") # Cari berdasarkan judul
    my_library.search_item("201")    # Cari berdasarkan ID