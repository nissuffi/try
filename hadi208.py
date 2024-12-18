def main():
    
    print ("Selamt Datang") 
    while True:
        print("1. registration")
        print("2. Login")
        print("3. pinjam buku")
        print("4. keluar")
        
        pilih = input("\nPilih nombor dari 1 hingga 4: ")
        
        if pilih == '1':
            with open ("pelajar.dat",'r') as file:
                name=input("sila masukkan nama anda:")
                password=input("sila masukkan password anda:")
                print("anda berjaya registration",'\n')
            
        elif pilih == '2':
            with open ("pelajar,dat", 'r') as file:
                nama = input ("sila masukkan nama anda:")
                password = input("sila masukkan password anda:")
                print ("anda berjaya login",'\n')
                break 
                print ("username or password anda salah.",'\n')
            
        elif pilih == '3':
            with open ("Buku.dat", 'r') as file:
                Tajuk=input("sila masukkan Tajuk buku:")
                ISBN=input("masukkan ISBN buku:")
                print('Pelajar telah memilih buku:', Tajuk)
                print('ISBN:', ISBN)
                print ("anda sudah berjaya meminjam buku")
    
        elif pilih == '4':
            print("keluar")
            break
        else:
            print("Sila pilih nombor 1 hingga 4 sahaja.", '\n')


           
    print("Selamat datang")
    username = input("Sila masukkan username: ")
    password = input("Sila masukkan password: ")
    with open ("pekerja.dat",'r') as file:
        if not authenticate(username, password):
            print("Sila cuba lagi.")
            return
        
        while True:
            print("\nPilihan:")
            print("1. Buku Baru")
            print("2. Kemas kini Buku")
            print("3. Padam Buku")
            print("4. Semak Senarai Buku")
            print("5. Keluar")
        
            pilih = input("\nPilih nombor dari 1 hingga 5: ")
            if pilih == '1':
                Buku_baru()
            elif pilih == '2':
                Kemas_kini_Buku()
            elif pilih == '3':
                Padam_Buku()
            elif pilih == '4':
                Semak_senarai_buku()
            elif pilih == '5':
                break
            else:
                print("Sila pilih nombor 1 hingga 5 sahaja.")
                
def authenticate(username, password):
    with open("pekerja.dat", 'r') as file:
        for line in file:
            if username == username and password == password:
                return True
    return False

def Buku_baru():
    with open ("Bukuinfo.dat", 'w') as file:
        Tajuk = input("Sila masukkan Tajuk: ")
        author = input("Sila masukkan nama author: ")
        ISBN = input("Sila masukkan ISBN buku: ")
        publisher = input("Sila masukkan publisher: ")
        place = input("Sila masukkan place buku: ")
        year = input("Sila masukkan Year buku: ")

        file = open("Bukuinfo.dat", 'a')
        file.write(f"Tajuk: {Tajuk}\n")
        file.write(f"author: {author}\n")
        file.write(f"ISBN: {ISBN}\n")
        file.write(f"publisher: {publisher}\n")
        file.write(f"place: {place}\n")
        file.write(f"year: {year}\n")
        file.write("\n")

        file.close()
        print("Tambah buku dalam sistem berjaya.", '\n')

def Kemas_kini_Buku():
    with open ("Bukuinfo.dat", 'r') as file:
        Bukuinfo = Baca_Bukuinfo()
        Tajuk = input("Sila masukkan nama buku: ")
        found = False
    
        for i in range(len(Bukuinfo)):
            Buku = Bukuinfo[i]
            if Buku[0] == Tajuk:
                print("Sila isi maklumat yang tertera:")
                Bukuinfo[i] = [
                    Tajuk,
                    input(f"Author [{Buku[1]}]: ") or Buku[1],
                    input(f"ISBN [{Buku[2]}]: ") or Buku[2],
                    input(f"Publisher [{Buku[3]}]: ") or Buku[3],
                    input(f"Place [{Buku[4]}]: ") or Buku[4],
                    input(f"Year [{Buku[5]}]: ") or Buku[5]
                ]
                Tulis_Bukuinfo(Bukuinfo)
                print("Buku berjaya dikemaskini.", '\n')
                found = True
                break
    
        if not found:
            print("Buku tidak wujud dalam sistem.", '\n')

def Padam_Buku():
    with open ("Bukuinfo.dat") as file:
        Bukuinfo = Baca_Bukuinfo()
        Tajuk = input("Sila masukkan nama buku: ")
        found = False
    
        for i in range(len(Bukuinfo)):
            Buku = Bukuinfo[i]
            if Buku[0] == Tajuk:
                found = True
                del Bukuinfo[i]  
                Tulis_Bukuinfo(Bukuinfo)  
                print("Buku berjaya dipadamkan.")
                break  
    
        if not found:
            print("Buku tidak wujud dalam sistem.")

def Semak_senarai_buku():
    with open ("Bukuinfo.dat",'r') as file:
        Bukuinfo = Baca_Bukuinfo()
        if Bukuinfo:
            print("Senarai Buku:")
            for Buku in Bukuinfo:
                print(f"Tajuk: {Buku[0]}")
                print(f"Author: {Buku[1]}")
                print(f"ISBN: {Buku[2]}")
                print(f"Publisher: {Buku[3]}")
                print(f"Place: {Buku[4]}")
                print(f"Year: {Buku[5]}")
                print()
        else:
            print("Tiada buku dalam senarai.")

def Baca_Bukuinfo():
    Bukuinfo = []
    with open("Bukuinfo.dat", 'r') as file:
        for line in file:
            info = line.strip().split(': ')
            if len(info) == 2:
                Bukuinfo.append([info[0], info[1]])
            else:
                print(f"Ignoring line: {line.strip()}")

    return Bukuinfo

def Tulis_Bukuinfo(Bukuinfo):
    with open("Bukuinfo.dat", 'w') as file:
        for Buku in Bukuinfo:
            file.write(f"{Buku[0]}: {Buku[1]}\n")


if __name__ == "__main__":
    main()




