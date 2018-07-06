# -*- coding: utf-8 -*-
import os
import sys
import platform
from xlpy import *

def main_menu():
    clear()
    print(
        "\n############################################################"
        "\n     Tembak Paket XL"
        "\n     Mod By     : Gebang Kiidiw"
        "\n     Contact Me : gebangkiidiw@gmail.com"
        "\n     Blog       : www.gebangkiidiw.com"
        "\n     Youtube    : Gebang Kiidiw"
        "\n     Instagram  : @Bang_Joss24"
        "\n     Thanks To  : Alberto Anggi"
        "\n############################################################" +
        "\nSilahkan pilih menu Anda :"
        "\n[1] Paket Pembelian" + 
        "\n[2] Req OTP Code"  +
        "\n[0] Keluar"
    )
    choice = str(input(" >> "))
    exec_menu(choice)
    return

def exec_menu(choice):
    clear()
    if(choice == ''):
        menu_actions['main']()
    else:
        try:
            menu_actions[choice]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main']()
    return

def menu_1():
    print("===Paket Pembelian Menu=== WWW.GEBANGKIIDIW.COM")
    msisdn = str(input("Masukan Nomer Anda >> "))
    passwd = str(input("Masukan OTP >> "))
    print(
        "Daftar Paket XL Service ID:"
        "\n[1] Xtra Combo 10GB(Rp. 59.900) - 8211183" +
        "\n[2] XtraKuota 30GB (Rp. 10.000) - 8110577" +
        "\n-----------------------------------------"
        )
    serviceid = str(input("Masukan Service ID Di Atas >> "))
    xl = XL(msisdn)
    r = xl.loginWithPassword(passwd)
    if(r != False):
        print(xl.purchasePackage(serviceid)['message'])
    else:
        print("Login failed try again")
    decision = str(input("Ingin Mengulangi Prosesnya Masukan [Y] Kembali ke Menu Utama [N]? >> "))
    menu_actions['main']() if(decision in ['N','n']) else menu_actions['1']()
    return
        
def menu_2():
    clear()
    print("Request OTP Code - WWW.GEBANGKIIDIW.COM")
    msisdn = str(input("Masukan Nomer Anda >> "))
    xl = XL(msisdn)
    print(xl.reqPassword()['message'])
    decision = str(input("Ingin Mengulangi Prosesnya Masukan [Y] Kembali ke Menu Utama [N]? >> "))
    menu_actions['main']() if(decision in ['N','n']) else menu_actions['2']()
    return

def exit():
    sys.exit()

def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "0" : exit
}


if __name__ == "__main__":
    main_menu()
