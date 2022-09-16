# Konversi Suhu
from random import choices
from re import A
from secrets import choice
print ("Ini Adalah Pengkonversi Suhu!!")
celcius = float(input("Masukkan Suhu : "))
print ("Pilih Kode Operasi : (c , f , r , k )")
choice= input()

# Ini Suhu Celcius
if choice== "c":
    print("Suhu Celcius",celcius)

elif choice == "f" :
    print ("Suhu Farenhait: ",celcius * (9/5) + (32 )) 

elif choice == "r" :
   print ("Suhu Reamur : ",celcius * (4/5))

elif choice == "k" :
    print ( "Suhu Kelvin : ",celcius + (273))

print ("Teima Kasih Telah Menggunakan Program Ini!")

