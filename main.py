from tabulate import tabulate
from FuncTransaction import Transaction

def main():
    var = Transaction()
    welcome = input("Selamat datang di Toko A, masukkan nama Anda: ").capitalize()

    while True:
        print("\nPilih menu dibawah ini: ")
        print("1. Tambah Barang")
        print("2. Hapus barang atau Transaksi")
        print("3. Perbarui Barang")
        print("4. Keranjang Anda")
        print("5. Pembayaran")
        print("6. Keluar\n")

        choice = input("Masukkan pilihan Anda: ")

        if choice == "1":
            try:
                item = str(input("Masukkan nama barang: ")).strip().capitalize()  
                quantity = int(input("Masukkan jumlah barang: "))
                price = float(input("Masukkan harga barang: "))
                var.add_item(item, quantity, price)
                print("\nBerhasil menambahkan barang dalam keranjang Anda!")
            except ValueError as e:
                print(e)
                    
        elif choice == "2":
            while True:
                print("\n Pilihlah menu dibawah in: ")
                print("1. Hapus barang")
                print("2. Hapus transaksi")
                print("3. Keluar\n")
                remove_choice = input("Masukan pilihan anda: ")
                if remove_choice == "1":
                    try:
                        item = input("Masukkan nama barang: ").capitalize()
                        var.remove_item(item)
                        print("\nBarang telah berhasil dihapus!")
                    except Exception as e:
                        print(e)
                elif remove_choice == "2":
                    var.reset_transaction()
                    print("\n Transaksi telah berhasil dihapus!")

                elif remove_choice == "3":
                    break

                else:
                    print("Pilihan tidak ada!")

        elif choice == "3":
            while True:
                print("\nPerbarui: ")
                print("1. Nama Barang")
                print("2. Jumlah Barang")
                print("3. Harga Barang")
                print("4. Keluar")

                update_choice = input("\nMasukkan pilihan Anda: ")

                if update_choice == "1":  
                    try:
                        old_item = str(input("Masukkan nama barang yang ingin dirubah: ")).strip().capitalize()
                        new_item = str(input("Masukkan nama barang yang baru: ")).strip().capitalize()
                        var.update_item_name(old_item, new_item)

                        quantity = int(input("Masukkan jumlah barang baru: "))
                        price = float(input("Masukkan harga barang baru: ")) 

                        if new_item in var.items:
                            if quantity != var.items[new_item][0]:
                                var.update_quantity(new_item, quantity)

                            if price != var.items[new_item][1]:
                                var.update_price(new_item, price)

                        print("\nData barang berhasil diupdate!")      

                    except Exception as e:
                        print(e)

                elif update_choice == "2":
                    try:
                        item = input("Masukkan nama barang yang ingin diubah jumlahnya: ").strip().capitalize()
                        quantity = int(input("Masukkan jumlah barang baru: "))
                        var.update_quantity(item, quantity)
                        print("\nJumlah barang berhasil diubah!")
                    except Exception as e:
                        print(e)

                elif update_choice == "3":
                    try:
                        item = input("Masukkan nama barang yang ingin diubah harganya: ").strip().capitalize()
                        price = float(input("Masukkan harga barang baru: ")) 
                        var.update_price(item, price)
                        print("\nHarga barang berhasil diubah!")
                    except Exception as e:
                        print(e)

                elif update_choice == "4":
                    break

                else:
                    print("Pilihan tidak ada!.")

        elif choice == "4":
            print(f"\n--------------- Keranjang Anda, {welcome} ------------------")
            total_cost, discount_info = var.calculate_total()
            print(f"\nSelamat {welcome} Anda Mendapatkan {discount_info}!!!")
            print("")
            var.check()

        elif choice == "5":
            print("\nKonfirmasi pembelian Anda")
            final_confirm = input("'Y' Melanjutkan Pembayaran, 'N' Membatalkann Pembelian: ").capitalize()
            if final_confirm == "Y":
                print(f"\nTerima kasih sudah berbelanja di Toko Kami, {welcome}!")
                print("\n-------------- Struk Pembelian Anda ---------------")
                var.check()
                break
            else:
                print("\nPembelian dibatalkan!")
                break

        elif choice == "6":
            print("\nTerima kasih, sampai jumpa lagi!")
            break

        else:
            print("\nPilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
