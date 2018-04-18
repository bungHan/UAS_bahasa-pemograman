def b():
    print("\n*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*")
    nam = input ("\tMasukan Nama : ")
    nim = input ("\tMasukan NIM : ")
    num = input ("\tMasukan Semester sekarang : ")
    print("\n\t+++PILIHAN PEMBAYARAN+++") 
    print("\t1. Pembayaran SPP ")  
    print("\t2. Pembayaran UTS ")  
    print("\t3. Pembayaran UAS ")  
    print("\t4. Pembayaran SPP & UTS ")  
    print("\t5. Pembayaran SPP & UAS ")
    p = input("\n\tMAU PILIH YANG MANA (1/2/3/4/5)?: ")  
    if p == "1":
        spp()
    elif p == "2":
        uts()
    elif p == "3":
        uas()
    elif p == "4":
        spp_uts()  
    elif p == "5":
        spp_uas()
    else:
        exit
        tanya()
def spp():
    b = int(input("\n\tjumlah bulan yang di bayar : "))
    t = 500000 * b
    print("\t________________________________________")
    print("totalnya adalah Rp.500000 x ",b," = Rp. ",t)
    

def uas():
    mak = int(input("\n\tjumlah mata kuliah : "))
    byuas = 50000 * mak
    print("_____________________________________________")
    print("\ttotalnya adalah Rp.50000 x" ,mak,"  = Rp. ",byuas)

def uts():
    mat = int(input("\tjumlah mata kuliah : "))
    byuts = 50000 * mat
    print("_____________________________________________")
    print("\ttotal bayar uts = Rp.50000 x ",mat," = Rp. ",byuts)
    
def spp_uas():
    b = int(input("\n\tjumlah bulan yang di bayar : "))
    mak = int(input("\tjumlah mata kuliah : "))
    byuas = 50000 * mak
    tspp = 500000 * b
    t = byuas + tspp + 5000
    print("\tspp @ Rp.500000 x ",b," = Rp. ",tspp)
    print("\tuas @ Rp.50000  x ",mak," = Rp. ",byuas)
    print("\tbiaya tambahan untuk server Rp.5000 ")
    print("_____________________________________________")
    print("\ttotal bayar sejumlah  = Rp. ",t)
    
def spp_uts():
    b = int(input("\n\tjumlah bulan yang di bayar : "))
    mat = int(input("\tjumlah mata kuliah : "))
    byuts = 50000 * mat
    tspp = 500000 * b
    t = byuts + tspp + 5000
    print("\tspp @ Rp.500000 x ",b," = Rp. ",tspp)
    print("\tuts @ Rp.50000  x ",mat," = Rp. ",byuts)
    print("\tbiaya tambahan untuk server Rp.5000 ")
    print("_____________________________________________")
    print("\ttotal bayar sejumlah  = Rp. ",t)