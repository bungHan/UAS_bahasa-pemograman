def c():
   def add(x, y):
       return x + y
    # fungsi pengurangan
   def subtract(x, y):
       return x - y
    # fungsi perkalian
   def multiply(x, y):
       return x * y
    # fungsi pembagian
   def divide(x, y):
       return x / y
    # menu operasi
   print("*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*")
   print("+-+-+-+-+-INI  KALKULATOR-+-+-+-+-+-+-+")
   print("*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*")
   print("""\t1.Penjumlahan")
   \t2.Pengurangan
   \t3.Perkalian
   \t4.Pembagian""")
    # Meminta input dari user
   p = input("MASUKAN PILIHAN ?(1/2/3/4): ")
   n1 = int(input("Masukkan bilangan pertama: "))
   n2 = int(input("Masukkan bilangan kedua: "))
   if p == "1":
      print("hasilnya adalah\t",n1,"+",n2,"=", add(n1,n2))
   elif p == "2":
      print("hasilnya adalah\t",n1,"-",n2,"=", subtract(n1,n2))
   elif p == "3":
      print("hasilnya adalah\t",n1,"x",n2,"=", multiply(n1,n2))
   elif p == "4":
      print("hasilnya adalah\t",n1,":",n2,"=", divide(n1,n2))
   else:
      print("Salah Input Gan")

   
   tanya = input("\n\tHitung Lagi (y/t)?: ")
   if tanya == "y" :
      c()
   elif tanya == "t" :
       exit
   else:
       print("\n\tsalah input gan....!!!")   
