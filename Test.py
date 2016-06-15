"""

##########################
#    Giriş Protokolü     #
#    Sürüm numarası 1.0  #
#    Python 3.4.4        #
##########################

"""

import time

while True:

    print(
    """

    Hoşgeldiniz...
    Kayıt Olmak için   (1)
    Giriş Yapmak için  (2)
    Çıkış Yapmak için  (Q)

    """
    )

    cevap = input("Lütfen yapmak istediğiniz işlem numarasını girin: ")

    if cevap == "q" or cevap == "Q":
        break

    elif cevap == "1":
        kullaniciAdi    = input("Kullanıcı Adı Belirleyiniz       : ")
        parola          = input("Parola belirleyiniz              : ")
        parolaKontrol   = input("Lütfen Parolayı Tekrar giriniz   : ")
        isim            = input("İsminizi Giriniz                 : ")
        soyisim         = input("Soyisminizi giriniz              : ")

        if not kullaniciAdi:
            print("Kullanıcı Adı Bölümü Boş Bırakılamaz!")
            break
        elif not parola:
            print("Parola Bölümü Boş Bırakılamaz!")
            break
        elif not parolaKontrol:
            print("Parola Kontrol Bölümü Boş Bırakılamaz!")
            break
        elif not isim:
            print("İsim Bölümü Boş Bırakılamaz!")
            break
        elif not soyisim:
            print("Soyisim Bölümü Boş Bırakılamaz!")
            break

        elif len(parola) in range(3,16):
            pass
        else:
            print("Parola 3 ile 16 karakter arasında olmalıdır!")

        if parolaKontrol == parola:
            pass
        print("Parolalar Eşleşmiyor!")
        break