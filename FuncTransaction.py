from tabulate import tabulate

class Transaction:
    
    """Inisialisasi transaksi dengan dictionary kosong untuk menyimpan barang dan total biaya.
    Attribute: self.items (Dictoonary kosong) & self.total (set 0) """
   
    def __init__(self):
        self.items = {}
        self.total = 0
        
    def add_item(self, item, quantity, price):
        
        """Fungsi untuk menambah item kedalam self.items
            Attribute: item, quantity, price. """                                   
        
        if item in self.items:
            self.items[item][0] += quantity
        else:
            self.items[item] = [quantity, price]
    
    def remove_item(self, item):

        """Fungsi untuk menghapus item pada self.items
        Attribute: item.
        Exception: Barang tidak ada (jika input barang oleh user tidak ada pada self.items)"""
        
        if item in self.items:
            del self.items[item]
        else:
            raise Exception("Barang tidak ada")
            
    def update_item_name(self, old_item, new_item):

        """Fungsi untuk memperbaru item pada self.items dengan menggunakan 
        method .pop untuk mengganti item yang ada dalam keranjang.  
        Old_item, memanggil item lama untuk diganti dengan nama item baru (new_item)
        Attribute: old_item, new_item.
        Exception: Barang tidak ada (jika input barang oleh user tidak ada pada self.items)"""
        
        if old_item in self.items:
            self.items[new_item] = self.items.pop(old_item)
        else:
            raise Exception("Barang tidak ada")
    
    def update_quantity(self, item_name, new_quantity):
        
        """Fungsi untuk memperbarui jumlah barang (new_quantity) pada self.items dengan cara mengisi ulang Val[0] .
        Attribute: item_name, new_quantitiy.
        Exception: Barang tidak ada (jika input barang oleh user tidak ada pada self.items)"""
        
        if item_name in self.items:
            self.items[item_name][0] = new_quantity
        else:
            raise Exception("Barang tidak ada")
    
    def update_price(self, item_name, new_price):

     """Fungsi untuk memperbarui harga barang (new_price) pada self.items dengan cara mengisi ulang Val[1] .
        Attribute: item_name, new_price.
        Exception: Barang tidak ada (jika input barang oleh user tidak ada pada self.items)"""
        
        if item_name in self.items:
            self.items[item_name][1] = new_price
        else:
            raise Exception("Barang tidak ada")
                
    def calculate_total(self):

        """Fungsi untuk menghitung jumlah total belanja beserta diskon dengan ketentuannya. 
        Menggunakan return untuk mengembalikan nilai setelah penggunaan. memangil self.total sebagai total_cost
        Attribute: self."""
        
        total_cost = sum(quantity * price for quantity, price in self.items.values())
        
        discount_info = ""
        if total_cost >= 500000:
            total_cost *= 0.9
            discount_info = "Potongan Diskon 10%"
        elif total_cost >= 300000:
            total_cost *= 0.92
            discount_info = "Potongan Diskon 8%"
        elif total_cost >= 200000:
            total_cost *= 0.95
            discount_info = "Potongan Diskon 5%"
        
        self.total = total_cost
        return total_cost, discount_info
    
    def reset_transaction(self):

        """Fungsi untul menghapus seluru item pada self.items dengan method .clear()"""
        
        self.items.clear()
    
    def check(self):

        """Fungsi check menampilkan barang dengan format tabulate (Headers & Table) yang berisikan item_name, quantity & price.
        Memanggil variable total_cost & discount_info pada fungsi self.calculate_total() untuk ditampilkan pada "Total Belanja".
        Attribute: self."""
        
        total_cost, discount_info = self.calculate_total()
        headers = ["No",  "Nama Item", "Jumlah Item", "Harga Item"]
        table_data = [(i+1, item, info[0], info[1]) for i, (item, info) in enumerate(self.items.items())]
        print(tabulate(table_data, headers=headers, tablefmt="github"))
        print("")
        print(f"Total belanja:                      Rp.{total_cost} ({discount_info})")
        print("-------------------------------")
