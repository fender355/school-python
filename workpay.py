masih = True

while masih == True: 
    jam = float(input("\nNyatakan bilangan jam anda bekerja lebih masa: "))
    
    bayar = 6.5 * jam

    print(f'\nJumlah bayaran yang diperolehi untuk {jam} jam bekerja ialah RM {bayar}.')

    guna = int(input("\nAdakah anda masih ingin menggunakan atur cara ini? (1. Ya atau 2. Tidak): "))

    if guna == 1:
        masih
    else:
        masih = False
        print("\nTerima kasih kerana telah menggunakan atur cara ini. ")
        break
    

    