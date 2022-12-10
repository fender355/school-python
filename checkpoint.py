print("*** Atur cara untuk menyemak bilangan hari dalam bulan yang dipilih ***")

bulan=input("Masukkan bulan (Januari-Disember) : ")

if bulan.lower() in ("januari","mac", "mei", "julai", "ogos", "oktober", "disember"): 
    print("Jumlah hari dalam bulan", bulan.title(), "ialah 31 hari. ")

elif bulan.lower() in ("februari"):
    print("Jumlah hari dalam bulan", bulan.title(), "ialah 28 atau 29 hari. ")

elif bulan.lower() in ("april", "jun", "september", "november"): 
    print("Jumlah hari dalam bulan", bulan.title(), "ialah 30 hari. ")

else:
    print("Bulan yang anda masukkan tidak berkenaan. ")