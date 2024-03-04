from tabulate import tabulate

class Transaction:
    def __init__(self):
        self.items = []
        self.total = 0
        
    def add_item(self, item, quantity, price):
        self.items.append((item, quantity, price))
    
    def remove_item(self, item):
        for i, (item_name, _, _) in enumerate(self.items):
            if item_name == item:
                self.items.pop(i)
                return
            else:
                raise Exception("Barang tidak ada")
            
    
    def update_item(self, update_item_name, update_quantity, update_price):
        for i, (item_name, _, _) in enumerate(self.items):
            if item_name == update_item_name:
                self.items[i] = (update_item_name, update_quantity, update_price)
                return
            else:
                raise Exception("Barang tidak ada")
                
    def update_quantity(self, item_name, new_quantity):
        for i, (item_name, _, _) in enumerate(self.items):
            if name == item_name:
                self.items[i] = (name, new_quantity, self.items[i][2])
                return
        raise Exception("Barang tidak ada")
    
    def update_price(self, item_name, new_price):
        for i, (name, _, n) in enumerate(self.items):
            if name == item_name:
                self.items[i] = (name, self.items[i][1], new_price)
                return
        raise Exception("Barang tidak ada")
                
    def calculate_total(self):
        total_cost = 0
        for _, quantity, price in self.items:
            total_cost += quantity * price
        
        discount_info = ""
        if total_cost >= 500000:
            total_cost -= total_cost * 0.1
            discount_info = "Potongan Diskon 10%"

        elif total_cost >= 300000:
            total_cost -= total_cost * 0.08
            discount_info = "Potongan Diskon 8%"
            
            
        elif total_cost >= 200000:
            total_cost -= total_cost * 0.05
            discount_info = " Potongan Diskon 5%"
          
        
        self.total = total_cost
        return total_cost, discount_info

    
    def check(self):
        
        total_cost, discount_info = self.calculate_total()
        headers = ["No",  "Nama Item", "Jumlah Item", "Harga Item",]
        table_data = [(i+1, item[0], item[1], item[2]) for i, item in enumerate(self.items)]
        print(tabulate(table_data, headers=headers, tablefmt="github"))
        print("")
        print(f"Total belanja:                      Rp.{total_cost} ({discount_info})")
        print("-------------------------------")