print ("=====GEBYAR DISKON===== \n=====MASUKKAN JUMLAH BARANG YANG DIPESAN=====")
KA = int(input("KIPAS ANGIN DISKON 10%  Rp 25.000,00    : "))
SP = int(input("SEPEDA DISKON 55%       Rp 6.000,00     : "))
HR = int(input("HELM ROSSI DISKON 77%   Rp 8.000,00     : ")) 

KAD = ((KA*25000)/100)*10
SPD = ((SP*6000)/100)*55
HRD = ((HR*8000)/100)*77
TOTAL = HRD+SPD+KAD
print ("=====TOTAL=====")
print ("TOTAL KIPAS ANGIN    : Rp ",KAD)
print ("TOTAL SEPEDA SUPER   : Rp ",SPD)
print ("TOTAL HELM ROSSI     : Rp ",HRD)
print ("Jumlah total diskon yang didapat adalah Rp ",TOTAL)
