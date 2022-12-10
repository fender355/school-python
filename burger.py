print('''
Selamat Datang!

A: Makan dalam Restoran
B: Bawa Pulang
''')

makan=input("Sila masukkan pilihan anda (A/B): ")
harga=8.5

print('''
==Inti Tambahan==
\nA: Telur (sebiji) - RM 1.00
B: Daging/Ayam (sekeping) - RM 2.00
C: Keju (sekeping) - RM 1.50
D: Tamat (tunjukkan harga)
''')

tambahan=input("Sila masukkan pilihan inti tambahan anda (A/B/C/AB/AC/BC/ABC/D) : ")

if tambahan.upper() not in ("D"):

    if tambahan.upper() in ("A"):
        harga=harga+1.0

    elif tambahan.upper() in ("B"):
        harga=harga+2.0

    elif tambahan.upper() in ("C"):
        harga=harga+1.5

    elif tambahan.upper() in ("AB"):
        harga=harga+3.0
    
    elif tambahan.upper() in ("BC"):
        harga=harga+3.5
    
    elif tambahan.upper() in ("AC"):
        harga=harga+2.5
    
    elif tambahan.upper() in ("ABC"):
        harga=harga+4.5

    else:
        harga=harga+6000
else:
    harga=harga


if makan.upper() in ("A"):
    harga=harga

elif makan.upper() in ("B"): 
    harga=harga+0.2

else: 
    harga=harga+1000


if harga>=1000:
    print("Pilihan yang anda masukkan tidak berkenaan. ")

elif harga>=6000:
    print("Pilihan inti tambahan yang dimasukkan tidak berkenaan. ")

else:
    print("\nTerima kasih! Harga yang anda perlu bayar adalah RM", harga)