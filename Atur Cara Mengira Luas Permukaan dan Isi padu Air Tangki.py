# Pengisytiharaan nama atur cara
print("~ Atur Cara Pengiraan Luas Permukaan & Isi padu Air Tangki ~") 

# INPUT: Meminta ukuran jejari daripada pengguna 
j = float(input("\nMasukkan ukuran jejari air tangki: "))

# INPUT: Meminta ukuran ketinggian daripada pengguna
t = float(input("Masukkan ukuran ketinggian air tangki: ")) 

# PROSES: Pengiraan luas permukaan air tangki
# Formula: 2πjt + 2πj²
luas = (2*3.142*j*t) + (2*3.142*j*j)

# PROSES: Pengiraan isi padu air tangki
# Formula: πj²t 
isipadu = 3.142*j*j*t 

# Paparan hasil pengiraan 
print("\nUkuran air tangki anda adalah yang berikut. ")

# OUTPUT: Paparan luas permukaan air tangki
# Dibundarkan ke dua tempat titik perpuluhan
print("Luas permukaan: ",round(luas, 2),"m²")

# OUTPUT: Paparan isi padu air tangki 
# Dibundarkan ke dua tempat titik perpuluhan 
print("Isi padu: ",round(isipadu, 2),"cm³")

from time import sleep 
name=input("      ") 
print("Hello "+name) 
sleep(5) #this window won't close for 5 seconds, enough to see the greeting 
