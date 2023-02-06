import proces
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def kembali():
    print("\n")
    input("Tekan tombol apa saja untuk kembali...")
    clear_screen()

def main():
    flag = True
    while flag:
        print("~~~~~~~ PERPUSTAKAAN UNUD ~~~~~~~")
        print("1. Masuk")
        print("2. Buat akun")
        pilihan = int(input("Pilihan: "))
        if pilihan == 1:
            os.system("cls")
            f = open("account.txt", "r")
            f = f.readline()
            if f == "" or f == "\n":
                
                print("Belum ada akun! Silahkan buat akun")
                kembali()
            else:
                print("Masukkan akun")
                proces.login()
                flag = False
                kembali()
        elif pilihan == 2:
            os.system("cls")
            proces.create_account()
            kembali()
    main_menu()
    
def main_menu():  
    os.system("cls")
    print("~~~~~~~ PERPUSTAKAAN UNUD ~~~~~~~")
    print("Menu:")
    print("1. Cari Buku")
    print("2. Data Peminjaman")
    print("3. Data Pengembalian")
    print("4. Data User")
    print("5. Keluar")
    pil = int(input("Pilihan: "))
    if pil == 1:
        proces.cari_buku()
        kembali()
        main_menu()
    elif pil == 2:
        f = open("backup_peminjam.txt", "r")
        f = f.readline()
        print(f)
        if f == "" or f =="\n":
            print("KOSONG!!")
            kembali()
            main_menu()
        else:
            proces.data_peminjaman()
            kembali()
            main_menu()
    elif pil == 3:
        f = open("pengembalian.txt", "r")
        f = f.readline()
        print(f)
        if f == "" or f =="\n":
            print("KOSONG!!")
            kembali()
            main_menu()
        else:
            proces.data_pengembalian()
            kembali()
            main_menu()
    elif pil == 4:
        proces.data_user()
        kembali()
        main_menu()
    elif pil == 5:
        exit()
    else: print("Tidak ada pilihan di di luar 1 - 5!!")

main()