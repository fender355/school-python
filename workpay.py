masih = True

while masih == True: 
    jam = float(input("Nyatakan bilangan jam anda bekerja lebih masa: "))
    
    bayar=6.5*jam

    print(f'Jumlah bayaran yang diperolehi untuk {jam} jam bekerja ialah RM {bayar}.')

    guna = int(input("\nAdakah anda masih ingin menggunakan atur cara ini? (1. Ya atau 2. Tidak): "))

    if guna==1:
        masih
    else:
        break
    
print("Terima kasih kerana telah menggunakan atur cara ini. ")
    