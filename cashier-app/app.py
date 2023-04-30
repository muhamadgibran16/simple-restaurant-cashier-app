from datetime import datetime 

print("\n============================================================")
print("             WELCOME TO JAPANESE FOOD RESTAURANT")
print("                        Tokyo, Japan")
print("============================================================")
print("                        DAFTAR MENU")
print("------------------------------------------------------------")
# Make a menu list 
print("""Makanan :\t\t\tMinuman :
------------------------\t----------------------------
1. Sushi    : Rp. 40.000\t1. Green Tea    : Rp. 15.000
2. Onigiri  : Rp. 30.000\t2. Milk Tea     : Rp. 15.000
3. Ramen    : Rp. 50.000\t4. Cappucino    : Rp. 17.000
4. Sup Miso : Rp. 35.000\t4. Red Velvet   : Rp. 15.000
5. Takoyaki : Rp. 25.000\t5. Coca Cola    : Rp. 12.000
""")
print("============================================================")
print("\n\n-------------------------------------------")

tanggal = datetime.now()
waktu   = datetime.strftime(tanggal,"%d-%B-%Y \t  %H:%M:%S")
print("Date       : ", waktu)
order   = input("Order ID   :  ")

# Food List Variable 
makan        = []
total_makan  = []
jumlah_makan = []
harga_makan  = []
# Drink List Variable 
minum        = []
total_minum  = []
jumlah_minum = []
harga_minum  = []

# Main Menu Choice at the Cashier
def main_menu() :
    print("-------------------------------------------")
    print("""Menu Utama :
        1. Input Pesanan Makanan
        2. Input Pesanan Minuman
        3. Cetak Struk Pembelian   
        4. Keluar
        """)
    print("-------------------------------------------")
    
    pilih = input("Pilih Menu : ")
    
    # Menu Option
    if pilih == "1" :
        daftar_makanan()
    elif pilih == "2" :
        daftar_minuman()
    elif pilih == "3" :
        cetak()
    elif pilih == "4" :
        exit()
    else :
        print("Pilihan yang anda masukan salah!")
        main_menu()
        
# Create a Food Menu Display
def daftar_makanan() :
    print("-------------------------------------------")
    print("""Menu Makanan :
        1. Sushi        : Rp. 40.000
        2. Onigiri      : Rp. 30.000
        3. Ramen        : Rp. 50.000
        4. Sup Miso     : Rp. 35.000
        5. Takoyaki     : Rp. 25.000
        """)
    print("-------------------------------------------")
    # Input Order
    kode  = int(input("Masukkan Kode Makanan   : "))
    porsi = int(input("Masukkan Jumlah Pesanan : "))

    # Branching to Determine Food List Code
    if kode == 1 :
        makan.append("Sushi     ")
        harga = 40000
        harga_makan.append(harga)
        jumlah_makan.append(porsi)
        total_makan.append(harga * porsi)
        opsi()
    elif kode == 2 :
        makan.append("Onigiri   ")
        harga = 30000
        harga_makan.append(harga)
        jumlah_makan.append(porsi)
        total_makan.append(harga * porsi)
        opsi()
    elif kode == 3 :
        makan.append("Ramen     ")
        harga = 50000
        harga_makan.append(harga)
        jumlah_makan.append(porsi)
        total_makan.append(harga * porsi)
        opsi()
    elif kode == 4 :
        makan.append("Sup Miso  ")
        harga = 35000
        harga_makan.append(harga)
        jumlah_makan.append(porsi)
        total_makan.append(harga * porsi)
        opsi()
    elif kode == 5 :
        makan.append("Takoyaki  ")
        harga = 25000
        harga_makan.append(harga)
        jumlah_makan.append(porsi)
        total_makan.append(harga * porsi)
        opsi()
    else :
        print("Kode yang anda masukan salah")
        daftar_makanan()
    return
        
# Loop Function for Food List
def opsi() :
    print("-------------------------------------------")
    pilih = input("Input Makanan Lagi ? [y/n]\n")
    if pilih == "y" or pilih == "Y":
        daftar_makanan()
    elif pilih == "n" or pilih == "N":
        main_menu()
    else :
        print("Pilihan yang anda masukan salah!")
        opsi()


# Create a Drink Menu Display
def daftar_minuman() :
    print("-------------------------------------------")
    print("""Menu Minuman :
        1. Green Tea    : Rp. 15.000
        2. Milk Tea     : Rp. 15.000
        3. Cappucino    : Rp. 17.000
        4. Red Velvet   : Rp. 15.000
        5. Coca Cola    : Rp. 12.000
        """)
    print("-------------------------------------------")
    # Input Order
    kode  = int(input("Masukkan Kode Minuman   : "))
    gelas = int(input("Masukkan Jumlah Pesanan : "))

    # Branching to Determine Drink List Code
    if kode == 1 :
        minum.append("Green Tea ")
        harga = 15000 
        harga_minum.append(harga)
        jumlah_minum.append(gelas)
        total_minum.append(harga * gelas)
        option()
    elif kode == 2 :
        minum.append("Milk Tea  ")
        harga = 15000
        harga_minum.append(harga)
        jumlah_minum.append(gelas)
        total_minum.append(harga * gelas)
        option()
    elif kode == 3 :
        minum.append("Cappucino ")
        harga = 17000 
        harga_minum.append(harga)
        jumlah_minum.append(gelas)
        total_minum.append(harga * gelas)
        option()
    elif kode == 4 :
        minum.append("Red Velvet")
        harga = 15000 
        harga_minum.append(harga)
        jumlah_minum.append(gelas)
        total_minum.append(harga * gelas)
        option()
    elif kode == 5 :
        minum.append("Coca Cola ")
        harga = 12000
        harga_minum.append(harga)
        jumlah_minum.append(gelas)
        total_minum.append(harga * gelas)
        option()
    else :
        print("Kode yang anda masukan salah")
        daftar_minuman()
    return

# Loop Function for Drink List
def option() :
    print("-------------------------------------------")
    pilih = input("Input Minuman Lagi ? [y/n]\n")
    if pilih == "y" or pilih == "Y":
        daftar_minuman()
    elif pilih == "n" or pilih == "N":
        main_menu()
    else :
        print("Pilihan yang anda masukan salah!")
        option()
        
# Function to Print Output Display
def cetak() :
    print("-------------------------------------------\n\n\n")
    print("===========================================")
    print("         JAPANASE FOOD RESTAURANT          ")
    print("                Tokyo, Japan               ")
    print("===========================================")
    print("Date       : ", waktu)
    print("Order ID   : ", order)
    print("-------------------------------------------")
    print("Order\t\tHarga\tJumlah\t     Total")
    print("-------------------------------------------")
    
    # Food Order List
    for x in range(len(makan)):
        print(f"{makan[x]}\t{harga_makan[x]}\t  {jumlah_makan[x]}\tRp.  {total_makan[x]}")
    # Drink Order List
    for y in range(len(minum)):
        print(f"{minum[y]}\t{harga_minum[y]}\t  {jumlah_minum[y]}\tRp.  {total_minum[y]}")
        
    total = total_makan + total_minum
    print("-------------------------------------------")
    print("SubTotal                      : Rp. ", sum(total))   
    print("Bayar                         : Rp. ", end=" ")     
    bayar = int(input())
    kembalian = bayar - (sum(total))
    print("-------------------------------------------")
    print("Kembalian                     : Rp. ", kembalian)
    print("===========================================")
    print("               Terima Kasih         ")
    print("    Telah mengunjungi Restaurant Kami!!!")
    print("===========================================\n")
    
    
# Main Program
if __name__ == "__main__" :
    main_menu()