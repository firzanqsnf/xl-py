# -*- coding: utf-8 -*-
import os
import sys
import platform
from xlpy import *

def main_menu():
    clear()
    print(
        "   ==========================================" +
        "   = TEMBAK PAKET XL - WWW.GEBANGKIIDIW.COM =" +
        "   ==========================================" +
        "\nSilakan pilih menu yang ingin Anda bintangi:"
        "\n[1] Paket Pembelian" + 
        "\n[2] Req OTP"  +
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
    print("===Paket Pembelian Menu")
    msisdn = str(input("Masukan MSISDN >> "))
    passwd = str(input("Masukan OTP >> "))
    print(
        "List of Internet package Service ID:"
        "\n[4] Xtra Combo 10GB(Rp. 59.900) - 8211183" +
        "\n[5] XtraKuota 30GB (Rp. 10.000) - 8110577" +
        "\n-----------------------------------------"
        )
    serviceid = str(input("Input your Service ID >> "))
    xl = XL(msisdn)
    r = xl.loginWithPassword(passwd)
    if(r != False):
        print(xl.purchasePackage(serviceid)['message'])
    else:
        print("Login failed try again")
    decision = str(input("Want to repeat the process [Y/N]? >> "))
    menu_actions['main']() if(decision in ['N','n']) else menu_actions['1']()
    return
        
def menu_2():
    clear()
    print(".::Password Menu::.")
    msisdn = str(input("Input your MSISDN >> "))
    xl = XL(msisdn)
    print(xl.reqPassword()['message'])
    decision = str(input("Want to repeat the process [Y/N]? >> "))
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
