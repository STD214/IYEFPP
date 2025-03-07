from otomobil import Otomobil
from motosiklet import Motosiklet
from kiralama_sistemi import KiralamaSistemi

# Test nesneleri oluşturalım
otomobil1 = Otomobil("BMW", "320i", 2020, 1000, "Otomatik")
motosiklet1 = Motosiklet("Honda", "CBR", 2021, 500, 600)

# Kiralama sistemi oluşturalım
kiralama = KiralamaSistemi()

# Test edelim
print(otomobil1.bilgileri_goster())
print(otomobil1.yakit_tuketimi())
print(kiralama.arac_kirala(otomobil1, 3))

print("\n" + "="*50 + "\n")

print(motosiklet1.bilgileri_goster())
print(motosiklet1.yakit_tuketimi())
print(kiralama.arac_kirala(motosiklet1, 5)) 