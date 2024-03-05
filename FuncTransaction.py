from tabulate import tabulate

class Transaction:
    def __init__(self):
        self.items = {}
        self.total = 0
        
    def add_item(self, item, quantity, price):
        if item in self.items:
            self.items[item][0] += quantity
        else:
            self.items[item] = [quantity, price]
    
    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            raise Exception("Barang tidak ada")
            
    def update_item_name(self, old_item, new_item):
        if old_item in self.items:
            self.items[new_item] = self.items.pop(old_item)
        else:
            raise Exception("Barang tidak ada")
    
    def update_quantity(self, item_name, new_quantity):
        if item_name in self.items:
            self.items[item_name][0] = new_quantity
        else:
            raise Exception("Barang tidak ada")
    
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name][1] = new_price
        else:
            raise Exception("Barang tidak ada")
                
    def calculate_total(self):
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
    
    def check(self):
        total_cost, discount_info = self.calculate_total()
        headers = ["No",  "Nama Item", "Jumlah Item", "Harga Item"]
        table_data = [(i+1, item, info[0], info[1]) for i, (item, info) in enumerate(self.items.items())]
        print(tabulate(table_data, headers=headers, tablefmt="github"))
        print("")
        print(f"Total belanja:                      Rp.{total_cost} ({discount_info})")
        print("-------------------------------")
