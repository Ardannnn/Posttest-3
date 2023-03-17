import os
os.system('cls')

class Lagu:
    def __init__(self, title):
        self.data = title
        self.lagu = None

    #Get Berfungsi Buat Getter untuk Atribut, Disebut get_title dsb
    def get_title(self):
        return self.data
    
    def set_title(self, title):
        self.data = str(title.title())

    def get_next_song(self):
        return self.lagu

    def set_next_song(self, next_title):
        self.lagu = next_title

    # Data Musik
    def _str_(self):
        return str(self.data)

    # Menampilkan Urutan Lagu
    def _repr_(self):
        return f"{self.data} -> {self.lagu}"

class Playlist:
    def __init__(self):
        self.head = None

    # Buat METHOD add_Musik Membuat Objek lagu dan Menambahkan Ke Daftar Putar. Metode ini Memiliki 1 Parameter Yaitu TITLE
    def add_song(self, title):
        Lagu_baru = Lagu(title)
        Lagu_baru.set_title(title)
        Lagu_baru.set_next_song(self.head)
        self.head = Lagu_baru

    # Buat METHOD find_song yang Mencari Apakah lagu Keluar dari Playlist dan Mengembalikan indeksnya. Method ini mempunyai Parameter juga yaitu TITLE 
    def find_song(self, title):
        song = self.head
        index = 0
        if self.length() is None:
            return -1
        else:
            while song:
                if song.get_title() == title:
                    return index
                else:
                    index += 1
                    song = song.get_next_song()
            return -1

  #Buat Method remove_song Yang Menghapus lagu dari Playlist. Method ini Mempunyai Parameter TITLE, yaitu lagu yang harus di Hapus 
    def remove_song(self, title):
        song = self.head

        if song == None:
            return print('Tidak Ada Lagu Didalam Playlist. Harap Menambahkan Terlebih Dahulu.')
        elif song.get_title() == title: 
            self.head = song.get_next_song()
            return print(f'Lagu {title} berhasil dihapus dari Playlist')
        else: 
            song = song.get_next_song()

    # Method length, Mengembalikan jumlah lagu Dalam Playlist 
    def length(self):
        index = 0
        song = self.head

        while song != None:
            index += 1
            song = song.get_next_song()
        return index


    # Method Print_songs,Mencetak Playlist Bernomor di Playlist
    # Contoh:
    # 1. Judul Lagu  1
    # 2. Judul Lagu 2
    # 3. Judul Lagu 3

    def print_songs(self):
        index = 1
        song = self.head
        if song == None:
            print(f"==========================================================")
            print(f"Tidak Ada Musik Didalam Playlist. Silahkan Tambahkan Musik")
            print(f"==========================================================")
            return None
        while song:
            print(f"{index}. {song.get_title()}")
            index += 1
            song = song.get_next_song()

    def print_linkedlist(self):
        if self.head is None:
            print("Tidak Ada Lagu Didalam Playlist.")
            
        else:
            n = self.head
            while n is not None:
                print(n._repr_(), end=" ---> ")
                n = n._repr_()

playlist = Playlist()
while True:
    # Pilihan menu awal
    print('''
    I=====================================I
    I    * * * Spotify Playlist * * *     I
    I=====================================I
    Pilihan :
    1: Menambahkan Musik Kedalam Playlist
    2: Lihat isi Playlist
    3: Menghapus Musik Dari Playlist
    4: Mencari Musik Didalam Playlist
    5: Melihat Jumlah Musik Dalam Playlist
    6: Keluar
    =====================================
    ''')

    # Pilihan inputan user
    Pilihan = int(input('Silahkan masukkan pilihan anda : '))
    print()


    # Pilihan 1: Untuk Menambahkan Lagu Pada Playlist
    if Pilihan == 1:
        pilihan2 = input('Judul Lagu yang ingin ditambahkan : ')
        playlist.add_song(pilihan2)
        
    # Pilihan 2: Untuk melihat playlist
    elif Pilihan == 2:
        playlist.print_songs()

    # Pilihan 3: Untuk Menghapus Lagu Pada Playlist
    elif Pilihan == 3:
        pilihan3 = input('Judul Lagu yang ingin dihapus :  ')
        print(playlist.remove_song(pilihan3))

    # Pilihan 4: Untuk Mencari lagu Pada Playlist
    elif Pilihan == 4:
        pilihan4 = input('Judul Lagu yang ingin dicari :  ')
        index = playlist.find_song(pilihan4)
        if index == -1:
            print(f"Judul Lagu {pilihan4} Tidak Ada Didalam Playlist.")
        else:
            print(f"Judul Lagu {pilihan4} Berada Pada Nomor {index+1}")

    # Pilihan 5: Untuk Melihat Urutan Playlist
    elif Pilihan == 5:
        print(f"Terdapat {playlist.length()} Judul Lagu Dalam Playlist.")

    # Pilihan 6: Untuk Keluar  
    elif Pilihan == 6:
        print(f"Berhasil keluar.")
        break

    # Else jika pilihan tidak sesuai 
    else:
        print('Pilihan Tidak Valid Silahkan Masukkan Pilihan Dengan Benar!!!.\n')