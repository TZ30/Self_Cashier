from tabulate import tabulate
from FuncTransaction import Transaction

def main():
    var = Transaction()

    welcome = input("Selamat datang di Toko A, masukan nama anda: ").capitalize()

    while True:
        print("")
        print("Pilih menu dibawah ini: ")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Perbarui Barang")
        print("4. Keranjang Anda")
        print("5. Pembayaran")
        print("6. Keluar")
        print("")
        
        choice = input("Masukan pilihan anda: ")
        if choice == "1":
            while True:
                try:
                    item = input("Masukan nama barang: ").strip().capitalize()  
                    if not item.isalpha():
                        print("")
                        raise ValueError("Pastikan nama barang menggunakan huruf")
                    quantity = int(input("Masukan jumlah barang: "))
                    price = float(input("Masukan harga barang: "))
                    var.add_item(item, quantity, price)
                    print("")
                    print("Berhasil menambahkan barang dalam keranjang anda!")
                    break
                except ValueError:
                    print("Pastikan nama barang diisi dengan benar dan jumlah serta harga barang menggunakan angka!")
                    
        elif choice == "2":
            try:
                item = str(input("Masukan nama barang: ")).capitalize()
                var.remove_item(item)
                print("")
                print("Barang telah berhasil dihapus!")
            except Exception as e:
                print("")
                print(e)
                
        elif choice == "3":
            print("Perbarui: ")
            print('1. Nama Barang')
            print('2. Jumlah Barang')
            print('3. Harga Barang')
            print('4. Keluar')
            print("")
            
            while True:
                choice_2 = input("Masukan pilihan anda: ")
                if choice_2 == "1":  
                    try:
                        item = input("Masukkan nama barang: ").strip().capitalize()
                        if not item.isalpha():
                            print("")
                            raise ValueError("Pastikan nama barang menggunakan huruf!")
                        quantity = int(input("Masukkan jumlah barang: "))
                        price = float(input("Masukkan harga barang: "))
                        var.update_item(item, quantity, price)
                        print("Data barang berhasil diupdate!")
                        break
                    except Exception as e:
                        print("")
                        print(e)
                        
                elif choice_2 == "2":
                    try:
                        quantity = int(input("Masukan jumlah barang kembali: "))
                        var.update_quantity(item, quantity)
                        print("")
                        print("Jumlah barang berhasil diganti!")
                        
                    except Exception as e:
                        print("")
                        print(e)
                        break
                        
                elif choice_2 == "3":
                    try:
                        price = float(input("Masukan harga barang kembali: ")) 
                        var.update_price(item, price)
                        print("")
                        print("Harga barang berhasil diganti!")
                        
                    except Exception as e:
                        print("")
                        print(e)
                        break
                        
                elif choice_2 == "4":
                    break
                    
                else:
                    raise Exception("Opsi yang tersedia hanya 1,2,3,4")
                    
                            
        elif choice == "4":
            total_cost, discount_info = var.calculate_total()
            print("")
            print(f"--------------- Keranjang Ada {welcome} ------------------")
            print("")
            print(f"Selamat {welcome} Anda Mendapatkan {discount_info}!!!")
            print("")
            var.check()
        
        elif choice == "5":
            print("")
            print("Konfirmasi pembelajaan anda")
            final_confirm = input("'Y' Melanjutkan Pembayaran, 'N' Membatalkann Pembelian-: ").capitalize()
            
            if final_confirm == "Y":
                print("")
                print (f"Terimakasih Sudah Berbelanja di Toko Kami")
                print ("-------------- Struk Anda ---------------")
                var.check()
                break
            else:
                print("")
                print("Telah berhasil membatalkan pembelian!")
                break
                
        else:
            break

if __name__ == "__main__":
    main()
