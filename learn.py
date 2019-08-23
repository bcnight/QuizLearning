#!/usr/bin/python
#Author:Alwan Putra & Gunawan Cipta
#VERSI 3.7
#MAU RECODE?TAU DIRI
#hargailah sang pencipta :v
#gataungoding.id


R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue

from getpass import getpass
import time
import os

users = {
    "root": {
        "password": "kocak",
        "group": []
    }
}


#---------------------------------------------------------------#
point = 0

form_jawaban_benar = ("Jawaban Benar, Kamu mendapatkan 20 Point")
#---------------------------------------------------------------#

# DI BAWAH INI ADALAH SOAL UNTUK MAPEL REKAYASA PERANGKAT LUNAK 
# V.3 

def soal1_rpl():
    time.sleep(1)
    correct_answer = "a"
    print('-'*40)
    print("1. sekumpulan program yang dibangun untuk melayani program lain adalah ...")
    print("  a. Perangkat Lunak System")
    print("  b. Perangkat Lunak Bisnis")
    print("  c. Perangkat Lunak Teknik dan Ilmu Pengetahuan")
    print("  d. Perangkat Lunak yang Dilekatkan")
    print("  e. Perangkat keras")
    jawaban1 = str(input("Jawaban => "))

    global point
    global form_jawaban_benar
    if jawaban1 == correct_answer:
        time.sleep(1)
        print('-'*30)
        print(form_jawaban_benar)
        point += 20
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)

def soal2_rpl():
    time.sleep(1)
    correct_answer = "b"
    print('-'*30)
    print("2. seluruh perintah yang digunakan untuk memproses informasi ...")
    print("  a. Aplikasi")
    print("  b. Perangkat Lunak")
    print("  c. Desain")
    print("  d. Analisa")
    print("  e. MBAH GOOGLE")
    jawaban1 = str(input("Jawaban => "))

    global point
    global form_jawaban_benar
    if jawaban1 == correct_answer:
        time.sleep(1)
        print('-'*30)
        print(form_jawaban_benar)
        point += 20
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)

def soal3_rpl():
    time.sleep(1)
    correct_answer = "a"
    print('-'*30)
    print("3. Perangkat lunak mempuantai dua hal pokok adalah . . .")
    print("  a. Konsep dasar rekayasa perangkat lunak")
    print("  b. Proses dan metode perangkat lunak")
    print("  c. Evaluasi perkembangan software")
    print("  d. Karakteristik dan atribut perangkat lunak")
    print("  e. MBAH GOOGLE")
    jawaban1 = str(input("Jawaban => "))

    global point
    global form_jawaban_benar
    if jawaban1 == correct_answer:
        time.sleep(1)
        print('-'*30)
        print(form_jawaban_benar)
        point += 20
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)

def soal4_rpl():
    time.sleep(1)
    correct_answer = "c"
    print('-'*30)
    print("4. YouTube di buat dengan bahasa ?")
    print("  a. Inggris")
    print("  b. Belanda")
    print("  c. Python")
    print("  d. Java")
    print("  e. MBAH YOUTUBE")
    jawaban1 = str(input("Jawaban => "))

    global point
    global form_jawaban_benar
    if jawaban1 == correct_answer:
        time.sleep(1)
        print('-'*30)
        print(form_jawaban_benar)
        point += 20
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)

def soal5_rpl():
    time.sleep(1)
    correct_answer = "d"
    print('-'*30)
    print("5. Game kebanyakan dibuat dengan bahasa ? ")
    print("  a. Bahasa Jawa")
    print("  b. Bahasa Cina")
    print("  c. Bash")
    print("  d. C++")
    print("  e. Tanya Google")
    jawaban1 = str(input("Jawaban => "))

    global point
    global form_jawaban_benar
    if jawaban1 == correct_answer:
        time.sleep(1)
        print('-'*30)
        print(form_jawaban_benar)
        point += 20
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)

def perkumpulan_soal_rpl():
    soal1_rpl()
    soal2_rpl()
    soal3_rpl()
    soal4_rpl()
    soal5_rpl()

#------------------------------------------------------------------------#

# DI BAWAH INI ADALAH SOAL UNTUK MATA PELAJARAN TEKNIK KOMPUTER JARINGAN
# V.3

def soal1_tkj():
    time.sleep(1)
    correct_answer = "b"
    print('-'*30)
    print("1. Subnet Mask yang dapat digunakan pada IP kelas B adalah . . .")
    print("  a. 255.0.0.0")
    print("  b. 255.255.0.0")
    print("  c. 255.255.255.248")
    print("  d. 255.255.255.0")
    print("  e. 000.0000.0000.00000")
    jawaban1 = str(input("Jawaban => "))

    global point
    global form_jawaban_benar
    if jawaban1 == correct_answer:
        time.sleep(1)
        print('-'*30)
        print(form_jawaban_benar)
        point += 20
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def soal2_tkj():
    time.sleep(1)
    correct_answer = "a"
    print('-'*30)
    print("2. Alat yang berfungsi untuk menghubungkan 2 jaringan dengan segmen yang berbeda adalah ...")
    print("  a. Router")
    print("  b. Switch")
    print("  c. Hub")
    print("  d. Access Point")
    print("  e. LAN")
    jawaban1 = str(input("Jawaban => "))

    global point
    global form_jawaban_benar
    if jawaban1 == correct_answer:
        time.sleep(1)
        print('-'*30)
        print(form_jawaban_benar)
        point += 20
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)

def soal3_tkj():
    time.sleep(1)
    correct_answer = "d"
    print('-'*30)
    print("3. Subnet Mask yang dapat digunakan pada IP kelas C adalah . . .")
    print("  a. 255.0.0.0")
    print("  b. 255.255.0.0")
    print("  c. 255.255.255.248")
    print("  d. 255.255.255.0")
    print("  e. 000.0000.0000.00000")
    jawaban1 = str(input("Jawaban => "))

    global point
    global form_jawaban_benar
    if jawaban1 == correct_answer:
        time.sleep(1)
        print('-'*30)
        print(form_jawaban_benar)
        point += 20
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)

def soal4_tkj():
    time.sleep(1)
    correct_answer = "e"
    print('-'*30)
    print("4. Salah satu tipe jaringan komputer yang umum dijumpai adalah....")
    print("  a. Star")
    print("  b. Bus")
    print("  c. WAN")
    print("  d. Wireless")
    print("  e. Client Server")
    jawaban1 = str(input("Jawaban => "))

    global point
    global form_jawaban_benar
    if jawaban1 == correct_answer:
        time.sleep(1)
        print('-'*30)
        print(form_jawaban_benar)
        point += 20
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)

def soal5_tkj():
    time.sleep(1)
    correct_answer = "e"
    print('-'*30)
    print("5. Berikut ini jenis topologi jaringan komputer, kecuali ...")
    print("  a. Star")
    print("  b. Bus")
    print("  c. Ring")
    print("  d. Mesh")
    print("  e. Three")
    jawaban1 = str(input("Jawaban => "))

    global point
    global form_jawaban_benar
    if jawaban1 == correct_answer:
        time.sleep(1)
        print('-'*30)
        print(form_jawaban_benar)
        point += 20
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)

def perkumpulan_soal_tkj():
    soal1_tkj()
    soal2_tkj()
    soal3_tkj()
    soal4_tkj()
    soal5_tkj()

#---------------------------------------------------------------#

# DI BAWAH INI ADALAH SOAL UNTUK MAPEL MULTIMEDIA
# V.3

def soal1_mm():
    time.sleep(1)
    correct_answer = "b"
    print('-'*30)
    print("1. Multimedia adalah kombinasi dari..")
    print("  a. User, grafis, BIOS, dan suara")
    print("  b. Teks, grafis, seni, suara, animasi, dan video")
    print("  c. Suara, animasi, blog, banner, dan CMOS")
    print("  d. Natrium klorida, NaCl, H2O dan video")
    print("  e. elemen air dan api okwokw")
    jawaban1 = str(input("Jawaban => "))

    global point
    global form_jawaban_benar
    if jawaban1 == correct_answer:
        time.sleep(1)
        print('-'*30)
        print(form_jawaban_benar)
        point += 20
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def soal2_mm():
    time.sleep(1)
    correct_answer = "c"
    print('-'*30)
    print("2. Presentasi Multimedia dapat meliputi...")
    print("  a. Judul multimedia")
    print("  b. Piranti authoring")
    print("  c. Non linier interaktif dan pasif")
    print("  d. Atta Halilintar")
    print("  e. Film dan cetak ")
    jawaban1 = str(input("Jawaban => "))

    global point
    global form_jawaban_benar
    if jawaban1 == correct_answer:
        time.sleep(1)
        print('-'*30)
        print(form_jawaban_benar)
        point += 20
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)

def soal3_mm():
    time.sleep(1)
    correct_answer = "c"
    print('-'*30)
    print("3. Sebuah struktur Multimedia dimana pengguna bernavigasi sesuai urutan dari 1 ")
    print("   frame atau bite informasi ke yang lainnya disebut.......")
    print("  a. Bentuk non linier")
    print("  b. Bentuk vector")
    print("  c. Bentuk Aljabar")
    print("  d. Bentuk Linier")
    print("  e. Bentuk Algoritma")
    jawaban1 = str(input("Jawaban => "))

    global point
    global form_jawaban_benar
    if jawaban1 == correct_answer:
        time.sleep(1)
        print('-'*30)
        print(form_jawaban_benar)
        point += 20
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)

def soal4_mm():
    time.sleep(1)
    correct_answer = "a"
    print('-'*30)
    print("4. Proyek Multimedia ketika dipublikasikan disebut.....")
    print("  a. Judul multimedia")
    print("  b. Kalimat Multimedia")
    print("  c. Susunan Multimedia")
    print("  d. Uraian Multimedia")
    print("  e. Abang Tampan ")
    jawaban1 = str(input("Jawaban => "))

    global point
    global form_jawaban_benar
    if jawaban1 == correct_answer:
        time.sleep(1)
        print('-'*30)
        print(form_jawaban_benar)
        point += 20
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)

def soal5_mm():
    time.sleep(1)
    correct_answer = "a"
    print('-'*30)
    print("5. Multimedia mampu..., kecuali:")
    print("  a. Mengubah Cara Berpakaian")
    print("  b. Mengubah Cara Belanja")
    print("  c. Mengubah Tempat Bekerja")
    print("  d. Atta Halilintar")
    print("  e. Membuat Youtuber")
    jawaban1 = str(input("Jawaban => "))

    global point
    global form_jawaban_benar
    if jawaban1 == correct_answer:
        time.sleep(1)
        print('-'*30)
        print(form_jawaban_benar)
        point += 20
    else:
        time.sleep(1)
        print("Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)

def perkumpulan_soal_mm():
    soal1_mm()
    soal2_mm()
    soal3_mm()
    soal4_mm()
    soal5_mm()

def kumpulan_soal_tkj():
    perkumpulan_soal_tkj()
    total_point();
    daftar_mapel();

def kumpulan_soal_rpl():
    perkumpulan_soal_rpl();
    total_point();
    daftar_mapel();

def kumpulan_soal_mm():
    perkumpulan_soal_mm()
    total_point();
    daftar_mapel();
#---------------------------------------------------------------# 
def load():
    os.system ('clear')
    print("mOhon tunggu......[\]")
    time.sleep (0.1)
    os.system ('clear')
    print("moHon tunggu......[|]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohOn tunggu......[/]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohoN tunggu......[-]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon Tunggu......[\]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tUnggu......[|]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tuNggu......[/]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tunGgu......[-]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tungGu......[\]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tunggU......[|]")
    time.sleep (0.1)
    os.system ('clear')
    print("Mohon tunggu......[-]")
    time.sleep (0.1)
    os.system ('clear')
    print("mOhon tunggu......[\]")
    time.sleep (0.1)
    os.system ('clear')
    print("moHon tunggu......[|]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohOn tunggu......[/]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohoN tunggu......[-]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon Tunggu......[\]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tUnggu......[|]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tuNggu......[/]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tunGgu......[-]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tungGu......[\]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tunggU......[|]")
    time.sleep (0.1)
    os.system ('clear')
    print("Mohon tunggu......[-]")
    time.sleep (0.1)
    os.system ('clear')
    print("mOhon tunggu......[\]")
    time.sleep (0.1)
    os.system ('clear')
    print("moHon tunggu......[|]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohOn tunggu......[/]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohoN tunggu......[-]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon Tunggu......[\]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tUnggu......[|]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tuNggu......[/]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tunGgu......[-]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tungGu......[\]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tunggU......[|]")
    time.sleep (0.1)
    os.system ('clear')
    print("Mohon tunggu......[-]")
    time.sleep (0.1)
    os.system ('clear')
    print("mOhon tunggu......[\]")
    time.sleep (0.1)
    os.system ('clear')
    print("moHon tunggu......[|]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohOn tunggu......[/]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohoN tunggu......[-]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon Tunggu......[\]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tUnggu......[|]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tuNggu......[/]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tunGgu......[-]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tungGu......[\]")
    time.sleep (0.1)
    os.system ('clear')
    print("mohon tunggU......[|]")
    time.sleep (0.1)
    os.system('clear')
#-----------------------------------------------#
def back_mapel():
    back = input("mau kembali/exit? [y/n]:")
    if back == 'y':
        daftar_mapel()
    elif back == 'n':
        exit()
    else:
        print('yang bener inputnya ')

def back_home():
    back = input("mau kembali/exit? [y/n]:")
    if back == 'y':
        session()
    elif back == 'n':
        exit()
    else:
        print('yang bener inputnya ')


def total_point():
    global point
    print("Total Point Kamu Adalah: ", point)

    if point >= 75:
        print("Selamat Anda Lulus!")

    elif point is 60:
        print("Anda Remed")

    elif point is 40:
        print("Anda Tidak Lulus")
    
    elif point is 20:
        print("Anda Tidak Lulus")
        
    else:
        print("Anda harus belajar lebih giat")

#---------------------------------------------------------------#

def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
            time.sleep(2)
            print("Login sukses.akan diarahkan ke halaman selanjutnya")
            time.sleep(2)
            return True
    return False

def login():
    os.system('clear')
    time.sleep(1)
    print("LOGIN")
    print ("-"*31)
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("username ga bole kosong")
        else:
            break
    while True:
        password = getpass("Password: ")
        if not len(password) > 0:
            print("password ga boleh kosong")
        else:
            break

    if loginauth(username, password):
        return session()
    else:
        print("Invalid username or password,buat akun dlu kalo blm buat")


def daftar():
    time.sleep(1)
    print ("-"*31)
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("username ga bole kosong ya.")
            continue
        else:
            break
    while True:
        password = getpass("New password: ")
        if not len(password) > 0:
            print("password ga bole kosong ya.")
            continue
        else:
            break

    load()
        
    users[username] = {}
    users[username]["password"] = password
    users[username]["group"] = "user"
    time.sleep(1)
    print("akun sukses dibuat.")
    back = input("mau login/exit? [y/n]:")
    if back == 'y':
        login()
    elif back == 'n':
        exit()
    else:
        print('input yg bener')
#------------------------------------#
def list_kkm():
    time.sleep(1)
    os.system('clear')
    print('++++++++++++++++++++++++++++')
    print("+ Nama Mapel   |    KKM    +")
    print('++++++++++++++++++++++++++++')
    print("+ Produktif RPL|   (80)    +")
    print("+ Matematika   |   (75)    +")
    print('+ PKN          |   (75)    +')
    print('++++++++++++++++++++++++++++')

    back_home()

def list_guru():
    time.sleep(1)
    print("+++++++++++++++++++++++++++++++++++++++")
    print('+ Nama Guru   |   Mata Pelajaran      +')
    print('+++++++++++++++++++++++++++++++++++++++')
    print("+pak rizki    |  (Produktif RPL)      +")
    print('+pak siswanto |  (Produktif Pemodelan)+')
    print('+++++++++++++++++++++++++++++++++++++++')

    back_home()

def daftar_mapel():
    time.sleep(1)
    print ("-"*50)
    print ("Pilih Mapel: [1.]RPL | [2.]TKJ | [3.] MM | [4.] EXIT")
    while True:
        input_user = input(" => ")
        if input_user == "1":
            kumpulan_soal_rpl()

        elif input_user == "2":
            kumpulan_soal_tkj()

        elif input_user == "3":
            kumpulan_soal_mm()  
        
        elif input_user == '4':
            exit()

        else:
            print(input_user + "\nyg bener inputnya yaaa")

def session():
    os.system('clear')
    time.sleep(1)
    print(" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(" +                      ~Welcome to System Learning~                    +")
    print(" +Options : [1.]Daftar Mapel | [2.]list guru | [3.]list kkm | [q.]Logout+")
    print(' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    while True:
        input_user = input(" => ")
        if input_user == "1":
            daftar_mapel()

        elif input_user == "2":
            list_guru()

        elif input_user == "3":
            list_kkm()

        elif input_user == "q":
            exit()            

        else:
            print(input_user + "\nyg bener inputnya yaaaa")
 #---------------------------------------------------------------#           
def menu():
    time.sleep(1)
    os.system('clear')
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+                    ~System Learning~                   +")
    print("+              ~sebelum login daftar dlu ya~             +")
    print("+       Options: [1.].LOGIN | [2.].DAFTAR | [9].EXIT     +")
    print("+                https://www.gataungoding.id/            +")
    print("+                       Version 3.7                      +")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    start = 0

    while start != 10:

        input_user = str(input('pilih angka => '))

        if input_user == "1":
            login()

        elif input_user == "2":
            daftar()

        elif input_user == "9":
            exit()

        else:
            print(input_user + "\nyg bener inputnya yaaaa")


menu() 
