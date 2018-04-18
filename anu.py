import getpass
from perhitungan.nilai import n
from perhitungan.bayar import b
from perhitungan.calculator import c
print("""
echo " /$$   /$$  /$$$$$$  /$$$$$$$  /$$   /$$  /$$$$$$ ";
echo "| $$  | $$ /$$__  $$| $$__  $$| $$  | $$ /$$__  $$";
echo "| $$  | $$| $$  \ $$| $$  \ $$| $$  | $$| $$  \__/";
echo "| $$$$$$$$| $$$$$$$$| $$$$$$$/| $$  | $$|  $$$$$$ ";
echo "| $$__  $$| $$__  $$| $$__  $$| $$  | $$ \____  $$";
echo "| $$  | $$| $$  | $$| $$  \ $$| $$  | $$ /$$  \ $$";
echo "| $$  | $$| $$  | $$| $$  | $$|  $$$$$$/|  $$$$$$/";
echo "|__/  |__/|__/  |__/|__/  |__/ \______/  \______/ ";
echo " /$$        /$$$$$$   /$$$$$$  /$$$$$$ /$$   /$$  ";
echo "| $$       /$$__  $$ /$$__  $$|_  $$_/| $$$ | $$  ";
echo "| $$      | $$  \ $$| $$  \__/  | $$  | $$$$| $$  ";
echo "| $$      | $$  | $$| $$ /$$$$  | $$  | $$ $$ $$  ";
echo "| $$      | $$  | $$| $$|_  $$  | $$  | $$  $$$$  ";
echo "| $$      | $$  | $$| $$  \ $$  | $$  | $$\  $$$  ";
echo "| $$$$$$$$|  $$$$$$/|  $$$$$$/ /$$$$$$| $$ \  $$  ";
echo "|________/ \______/  \______/ |______/|__/  \__/  ";
echo "                                                  ";
echo "                                                  ";
echo "                                                  ";

\t\tUNTUK BISA MEMAKAI APLIKASI INI 
\t\t     SILAHKAN LOGIN DULU !
""")
def menu():
    print("""
    *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*""")
    print("\n\tPILIHAN :")
    print("""\t\t  1.PENILAIAN MAHASISWA
    \t\t  2.PEMBAYARAN MAHASISWA
    \t\t  3.KALKULATOR
    \n    #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#""")

    pilih = input ("\tPILIH MANA (1/2/3)?: ")
    if pilih == "1" :
        n()
    elif pilih == "2" :
        b()
    elif pilih == "3" :
        c()
    else :
         exit
    t()

def t():
    t = input("\nKEMBALI KE MENU AWAL (y/t)?: ")
    if t == "y" :
        menu()
    elif t == "t" :
       exit
    else:
       print("\n\tSALAH INPUT GAN....!!!")

        
user = input ("Username: ")
sandi = getpass.getpass()
if sandi == "3" and user == "h":
   print("""

    =========================================
    =+-+-+-+-+ANDA BERHASIL LOGIN+-+-+-+-+-+=
    *****************************************""")
   menu()

else:
   print("Username atau Password Anda Salah")

