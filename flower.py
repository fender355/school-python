print('''
Selamat Datang ke Kedai Bunga Tangan! 

A: Ros 
B: Tulip 
C: Dahlia 
''')

bunga=input("Sila masukkan pilihan bunga anda (A/B/C) : ")

if bunga.upper() in 'A':
    harga_bunga=150
elif bunga.upper() in 'B':
    harga_bunga=180
elif bunga.upper() in 'C':
    harga_bunga=210
else: 
    harga_bunga=0

print('''
Berapakah jarak dari rumah anda ke kedai?

A: 60 km dan ke atas 
B: 30 - 59 km
C: 8 - 29 km
D: 7 km dan ke bawah
''')

jarak=input("Sila masukkan pilihan anda (A/B/C/D): ")

if jarak.upper() in 'A':
    caj=50

elif jarak.upper() in 'B':
    caj=30

elif jarak.upper() in 'C':
    caj=15

elif jarak.upper() in 'D': 
    caj=0

else: 
    caj=1000

if harga_bunga == 0 or caj==1000:
    print("\nPilihan yang anda masukkan tidak berkenaan. Sila cuba lagi. ")

else: 
    print(f'''
Terima kasih!
Harga bunga tangan: RM {harga_bunga}
Caj penghantaran: RM {caj}
    ''')