bulan=int(input("\nSila masukkan bulan : "))

if bulan in (1,2,4,5,7,8,10,11):
    
    if bulan in (1,2):
        print("\nHaribulan yang anda masukkan adalah musim sejuk. ")

    elif bulan in (4,5):
        print("\nHaribulan yang anda masukkan adalah musim bunga. ")

    elif bulan in (7,8):
        print("\nHaribulan yang anda masukkan adalah musim panas. ")

    else: 
        print("\nHaribulan yang anda masukkan adalah musim luruh. ")

elif bulan in (3,6,9,12):

    hari = int(input("\nSila masukkan hari : "))

    if bulan == 12:

        if hari <= 20 and hari >= 1 :
            print("\nHaribulan yang anda masukkan adalah musim luruh. ")

        elif hari >= 21 and hari <= 31 : 
            print("\nHaribulan yang anda masukkan adalah musim sejuk. ")

        else: 
            print("\nHaribulan yang anda masukkan tidak berkenaan. ")

    elif bulan == 3: 

        if hari <= 19 and hari >= 1 :
            print("\nHaribulan yang anda masukkan adalah musim sejuk. ")

        elif hari >= 20 and hari <= 31 :
            print("\nHaribulan yang anda masukkan adalah musim bunga. ")

        else:
            print("\nHaribulan yang anda masukkan tidak berkenaan. ")

    elif bulan == 6:

        if hari <= 20 and hari >= 1 : 
            print("\nHaribulan yang anda masukkan adalah musim bunga. ")

        elif hari >= 21 and hari <= 30 : 
            print("\nHaribulan yang anda masukkan adalah musim panas. ")

        else: 
            print("\nHaribulan yang anda masukkan tidak berkenaan. ")

    else: 

        if hari <= 21 and hari >= 1 :
            print("\nHaribulan yang anda masukkan adalah musim panas. ")

        elif hari >=22 and hari <= 30 :
            print("\nHaribulan yang anda masukkan adalah musim luruh. ")

        else: 
            print("\nHaribulan yang anda masukkan tidak berkenaan. ")

else: 

    print("\nHaribulan yang anda masukkan tidak berkenaan. ")


# sejuk starts on 12/21                1 - 3 sejuk
# bunga starts on 3/20                 4 - 6 bunga
# panas starts on 6/21                 7 - 9 panas
# luruh starts on 9/22                 10-12 luruh

