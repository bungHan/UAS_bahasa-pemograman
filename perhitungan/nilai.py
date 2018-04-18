def n():
   from texttable import Texttable
   print("=======================================")
   x = Texttable ()
   j = "y"  
   ni = []   #pertama kita buat list kosong untuk menampung masukan
   no = 0
   na = []
   n_t = []
   n_u = []
   n_us = []
   while j == "y": #untuk melakukan pengulangan
        na.append(input("Nama         :"))  #nama variabel ditambahkan .append untuk menambahkan nilai masukan ke dalam list
        ni.append(input("NIM          :"))
        n_t.append(input("Nilai Tugas  :"))
        n_u.append(input("Nilai UTS    :"))
        n_us.append(input("Nilai UAS    :"))
        j = input("Tambah data (y/t)?")
        no += 1 
   for i in range(no):      
       t = int(n_t[i])          
       ut = int(n_u[i])         
       u = int(n_us[i])
       ak = t*30/100 + ut*35/100 + u*35/100  
       x.add_rows([['No','Nama','NIM','Tugas','UTS','UAS','Akhir'],[i+1,na[i],ni[i],n_t[i],n_u[i],n_us[i],ak]]) #menambahkan tabel                                                                                                                                                                                                                                                                                                                                            
   print (x.draw()) #menampilkan tabel
