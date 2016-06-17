# Dosyanın Adı      : girisprotokolu.py
# Yaratıcı                               : Doğan Aydın
# Proje Başlangıç                        : 14 Haziran 2016
# Son Düzenleme     :
# Version                                : 1.5
# Modifikasyon      :

# Açıklama                    : Basit bir kayıt ve giriş uygulamasıdır


# 17 Haziran 2016 tarihinde test edildi
# time modülü aktarılıyor
import time

# döngü oluşturuluyor
while True:

	# gösterilecek metin basılıyor
    print(
    """

    Hoşgeldiniz...
    Kayıt Olmak için    (1)
    Giriş Yapmak için   (2)
    Hesap Makinesi için (3)
    Çıkış Yapmak için   (Q)
    
	"""
    )

    # kullanıcıdan cevap isteniyor
    cevap = input("Lütfen yapmak istediğiniz işlem numarasını girin: ")


    # eğer kullanıcı çıkmak isterse
    if cevap == "q" or cevap == "Q":
        break

    # eğer kullanıcı kayıt olmak isterse
    elif cevap == "1":
        time.sleep(1)
        kullaniciAdi    = input("Kullanıcı Adı Belirleyiniz       : ")
        parola          = input("Parola belirleyiniz              : ")
        parolaKontrol   = input("Lütfen Parolayı Tekrar giriniz   : ")
        isim            = input("İsminizi Giriniz                 : ")
        soyisim         = input("Soyisminizi giriniz              : ")


        # eğer kullanıcı istenilenleri girmezse
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

        # eğer kullanıcının parolası uygun ise
        elif len(parola) in range(3,16):
            pass
        else:
            print("Parola 3 ile 16 karakter arasında olmalıdır!")


        # kullanıcının parolası kontrol ediliyor
        if parolaKontrol == parola:
            # parola doğru ise
            print("\nKayıt Başarılı!")
            input("Devam etmek için 'Enter'e basın...")
            time.sleep(1)
        # parola doğru değil ise
        else:
            print("Parolalar Eşleşmiyor!")

    # eğer kullanıcı giriş yapmak isterse
    elif cevap == "2":
        time.sleep(1)

        # kullanıcının girdiğin bilgiler kontrol ediliyor
        try:

            girisAdi         = input("Kullanıcı Adı    : ")
            girisSifre       = input("Parola           : ")

            # eğer kullanıcının girdiği bilgiler uyuşuyorsa
            if girisAdi == kullaniciAdi and girisSifre == parola:
                time.sleep(2)
                print("\nGiriş Başarılı!")
                input("Devam etmek için 'Enter'e basın...")
                time.sleep(1)

            # eğer kullanıcın girdiği bilgiler uyuşmuyorsa
            else:
                time.sleep(1)
                print("Giriş Başarısız!")

        # girilen bilgilerde hata varsa
        except NameError:
            time.sleep(0.5)
            print("\nLütfen ilk önce kayıt olunuz!\n")
            input("Devam etmek için 'Enter'e basın...")


    # eğer kulllanıcı hesap makinesi isterse
    elif cevap == "3":
        time.sleep(1)
        try:

            if girisAdi == kullaniciAdi and girisSifre == parola:
                time.sleep(2)
                pass
            else:
                break
        except NameError:
            print("Lütfen ilk önce giriş yapınız!")

        # toplama fonksiyonu oluşturuluyor
        def toplama():

            # bilgiler kontrol ediliyor
            try:

                soru1 = int(input("1.Sayıyı girin: "))
                soru2 = int(input("2.Sayıyı girin: "))
                print("-"*17)
                print(soru1,"+",soru2,"=",soru1 + soru2)

            # hata varsa kullanıcıya bildiriliyor
            except ValueError:
                print("Lütfen sadece sayı girin!!")
            # fonksiyon sonlandırılıyor
            return

        # çıkarma fonksiyonu oluşturuluyor
        def cikarma():

            try:

                soru1 = int(input("1.Sayıyı girin: "))
                soru2 = int(input("2.Sayıyı girin: "))
                print("-"*17)
                print(soru1,"-",soru2,"=",soru1 - soru2)

            except ValueError:
                print("Lütfen sadece sayı girin!!")
            return

        # çarpma fonksiyonu oluşturuluyor
        def carpma():

            try:

                soru1 = int(input("1.Sayıyı girin: "))
                soru2 = int(input("2.Sayıyı girin: "))
                print("-"*17)
                print(soru1,"x",soru2,"=",soru1 * soru2)

            except ValueError:
                print("Lütfen sadece sayı girin!!")
            return

        # bölme fonksiyonu oluşturuluyor
        def bolme():

            try:

                soru1 = int(input("1.Sayıyı girin: "))
                soru2 = int(input("2.Sayıyı girin: "))
                print("-"*17)
                print(soru1,"/",soru2,"=",soru1 / soru2)

            except ValueError:
                print("Lütfen sadece sayı girin!!")
            except ZeroDivisionError:
                print("Bir sayıyı 0'a bölemezsin!")
            return

        while True:
        
            # işlem sıraları belitiliyor
            topla   = "\nToplama işelmi için             (1)"
            çıkarma = "\nÇıkarma işlemi için             (2)"
            çarpma  = "\nÇarpma işlemi için              (3)"
            bölme   = "\nBölme işlemi için               (4)"
            çıkış   = "\nHesap makinesinden çıkmak için  (Q)"

            # işlemler ekrana basılıyor
            print(topla)
            print(çıkarma)
            print(çarpma)
            print(bölme)
            print(çıkış)

            # hangi işlemin yapılmak istendiği soruluyor
            soru = input("\nHangi işlemi yapmak istiyorsunuz: ")

            if soru == "q" or soru == "Q":
                break
            elif soru == "1":
                toplama()
                time.sleep(1)
                input("Devam etmek için 'Enter'e basın...")
                time.sleep(1)
            elif soru == "2":
                cikarma()
                time.sleep(1)
                input("Devam etmek için 'Enter'e basın...")
                time.sleep(1)
            elif soru == "3":
                carpma()
                time.sleep(1)
                input("Devam etmek için 'Enter'e basın...")
                time.sleep(1)
            elif soru == "4":
                bolme()
                time.sleep(1)
                input("Devam etmek için 'Enter'e basın...")
                time.sleep(1)
