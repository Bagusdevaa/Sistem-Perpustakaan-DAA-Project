import os
import datetime
import pandas as pd
import datetime
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def kembali():
    print("\n")
    input("Tekan tombol apa saja untuk kembali...")
    clear_screen()

def pop_line(file, no_line):
    with open(file, 'r') as fp:
        lines = fp.readlines()
    with open(file, 'w') as fp:
        for number, line in enumerate(lines):
            if number not in [no_line-1]:
                fp.write(line)
pop_line("peminjam.txt",1)
def pop(file): # Fungsi untuk remove line pertama pada file txt
    with open(file, 'r+') as f: 
        firstLine = f.readline() # baca line pertama
        data = f.read() # baca sisanya
        f.seek(0) # kursor jadi paling atas
        f.write(data) # tulis data lagi
        f.truncate() # set ukuran file ke ukuran skrg
        return firstLine
   
def getDate(): # untuk tanggal
    now=datetime.now
    return str(now().date())

def getTime(): # untuk jam
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def create_account(): #buat akun
    f = open("peminjam.txt","a")
    f2 = open("account.txt","r")
    f2 = f2.readline()
    if f2 == "" or f2 =="\n":
        un = input("Username: ")
        with open("account.txt", 'a') as file:
            file.write(un+',')
        pw = input("password: ")
        with open("account.txt", 'a') as file:
            file.write(pw+'\n\n')
        print("Akun berhasil dibuat!")
    else:
        un = input("Username: ")
        with open("account.txt", 'a') as file:
            file.write(un+',')
        pw = input("password: ")
        with open("account.txt", 'a') as file:
            file.write(pw+'\n\n')
        print("Akun berhasil dibuat!")
        f.write("\n")

def login(): #login akun
    global username
    username = input("Username: ")
    password = input("password: ")
    file = open('account.txt','r')
    file = file.readlines()
    new_list_file = []
    for i in file:
        new_list_file.append(i.replace("\n",""))
    if (username + ','+password) in new_list_file:
            print("Login sukses!")              
    else: 
        print("Username atau password salah!")
        login()

def tambah_pinjaman(judul): # Untuk menambahkan data pinjaman
    file = open("peminjam.txt", "a")
    file.write(username+","+judul+","+str(getDate())+","+"Meminjam" +","+"7"+"|")
    file.close()

def booking(judul):
    file = open("peminjam.txt", "a")
    file.write(username+","+judul+","+str(getDate())+","+"Booking" +","+"-"+"|")
    file.close()

def show_data_user():
    file = open("data_user.txt", "r")
    file = file.readline()
    file_to_list = file.replace("\n","")
    file_to_list = file_to_list.split(",")
    print("Nama lengkap      : ",file_to_list[0])
    print("Tempat/tgl lahir  : ",file_to_list[1])
    print("Jenis kelamin     : ",file_to_list[2])
    print("E-mail            : ",file_to_list[3])
    print("No telepon        : ",file_to_list[4])


### MAIN MENU FUNCTION
def cari_buku(): # Cari buku, melihat daftar buku, dan pinjam/booking
    df = pd.read_excel("C:/Users/hp/OneDrive/Documents/Belajar Pemrograman/Project DAA/Data.xlsx")
    df2 = list(df["Judul"])
    file = open("peminjam.txt","a")
    print("Daftar buku:\n"+"="*150)
    print(df)
    print("="*150)
    print("\n1. Cari Buku\n2. Booking/pinjam Buku")
    pil = int(input("Pilihan: "))
    if pil == 1:
        input_buku = input("Masukkan judul buku yang lengkap: ")
        if input_buku in df2:
            indeks = df2.index(input_buku)
            print(df.iloc[[indeks]])
        else:
            print("Buku dengan judul seperti itu tidak ada!")
    else:
        print("Masukkan nomor buku yang ingin dipinjam: ")
        title = int(input("-> "))
        print("Data buku: ")
        new_df = df.iloc[title-1]
        print(new_df)
        if new_df["Status"] == "Available":
            print("Buku berstatus available, apakah ingin meminjam buku ini? 1=y|0=n")
            pil = int(input("-> "))
            if pil == 1:
                tambah_pinjaman(df["Judul"].iloc[title-1])
                print("Order telah dimasukkan ke dalam menu data peminjaman!")
            else:
                cari_buku()
        else: # Status terpinjam atau rusak
            print("Stok buku kosong, apakah ingin booking buku dan menunggu ? 1=y|0=n")
            pil1 = int(input("-> "))
            if pil1 == 1:
                booking(df["Judul"].iloc[title])
            else:
                cari_buku()
    backup()

def backup():
    file = open("peminjam.txt", "r+")
    file = file.readline()
    file = file.split("|")
    file.pop(-1)

    with open("backup_peminjam.txt", "r+") as backup: 
        for i in file:
            backup.write(i + "\n")
        backup.close()

def data_peminjaman():
    backup = open("backup_peminjam.txt","r+")
    backup = backup.readlines()
    new = []
    for i in backup: # Memasukkan database ke list new (jadi 2 dimensi)
        x = i.replace("\n","")
        new.append(x.split(","))
    new_lagi = [] 
    for i in range(len(new[0])): # Mengurutkan perkategori ke dalam new_lagi
        for j in range(len(new)):
            new_lagi.append(new[j][i])
            
    nomor = [x for x in range(1,len(new)+1)] # Untuk nomor tabel
    ind = len(new)
    df = pd.DataFrame({"No":nomor[0:len(nomor)],"Username":new_lagi[0:ind],"Judul buku":new_lagi[ind:ind*2],
                    "Tanggal pinjam":new_lagi[ind*2:ind*3],"Status":new_lagi[ind*3:ind*4],"Tenggat":new_lagi[ind*4:ind*5]})
    print(df.to_string(index=False))

    print("\n\n1. Kembalikan Buku? 1=y|0=n")
    pil = int(input("-> "))
    if pil == 1:
        print("Ketik no buku yang ingin dikembalikan!")
        pil1 = int(input("-> "))
        try:
            global to_pengembalian
            if new[pil1-1][3] == "Meminjam":
                to_pengembalian = backup[pil1-1]
                to_pengembalian = to_pengembalian.split(",")
                to_pengembalian[3] = "Dikembalikan"
                to_pengembalian[2] = str(getDate())+"/"+str(getTime())
                if new[pil1-1][4] == "0":
                    to_pengembalian[4] = "Rp15.000"
                else:
                    to_pengembalian[4] = "Rp0"
                to_pengembalian = ",".join(to_pengembalian)
                f = open("pengembalian.txt", "a")
                f.write(to_pengembalian+"|")
                print("Data Buku:")
                print(df.iloc[pil1-1])
                pop_line("backup_peminjam.txt", pil1)
                print("\nSukses mengembalikan Buku! Cek riwayat pada Data Pengembalian!")
            else:
                print("Buku berstatus booking!")
        except Exception as e: print(e) 


def data_pengembalian():
    file = open("pengembalian.txt", "r+")
    file = file.readline()
    file = file.split("|")
    file.pop(-1)
    new = [] 
    for i in file: # Memasukkan database ke list new (jadi 2 dimensi)
        x = i.replace("\n","")
        new.append(x.split(","))

    try:
        new_lagi = [] 
        for i in range(len(new[0])): # Mengurutkan perkategori ke dalam new_lagi
            for j in range(len(new)):
                new_lagi.append(new[j][i])
                
        nomor = [x for x in range(1,len(new)+1)] # Untuk nomor tabel
        ind = len(new)
        df = pd.DataFrame({"No":nomor[0:len(nomor)],"Username":new_lagi[0:ind],"Judul buku":new_lagi[ind:ind*2],
                        "Tanggal pengembalian":new_lagi[ind*2:ind*3],"Status":new_lagi[ind*3:ind*4],"Denda":new_lagi[ind*4:ind*5]})
        print(df.to_string(index=False))
    except:
        print("Ada error di database cuy :(")


def data_user():
    file = open("data_user.txt", "r+")
    add_file = open("data_user.txt", "a")
    file = file.readline()
    print("1. Lihat profil saya\n2. Update profil")
    pil = int(input("pilihan: "))
    if pil == 1:
        if file == "\n" or file == "":
            print("Anda belum mengisi data user, update data terlebih dahulu!")
            kembali()
            data_user()
        else:
            show_data_user()
    else:
        pop("data_user.txt")
        print("\nLengkapi data di bawah!")
        nama = input("Nama lengkap      : ")
        tgl = input("Tempat/tgl lahir  : ")
        sex = input("Jenis kelamin     : ")
        email = input("E-mail            : ")
        telp = input("No telepon        : ")
        add_file.write(nama+","+tgl+","+sex+","+email+","+telp+"\n")
        print("\nUpdate profil berhasil!!")
        kembali()