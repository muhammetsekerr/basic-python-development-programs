print("ATM uygulamasına hoşgeldiniz.")

k_adi = "123"
sifre = "456"


kul_adi = input("Kullanıcı Adınızı Giriniz:")
kul_sifre = input("Şifrenizi Giriniz:")

if((k_adi != kul_adi) & (sifre == kul_sifre )):
    print("Kullanıcı adınız hatalı girilmiştir.")

if((k_adi == kul_adi) & (sifre != kul_sifre )):
    print("Şifreniz hatalı girilmiştir.")

if((k_adi != kul_adi) & (sifre != kul_sifre )):
    print("Kullanıcı adınız ve şifreniz hatalı girilmiştir.")

if((k_adi == kul_adi) & (sifre == kul_sifre )):
    
    print("Kullanıcı adı ve şifreniz doğru, hoşgeldiniz")
    print("""  
                0- Çıkış
                1- Bakiye Sorgulama
                2- Para çekme
                3- Para yatırma 
                """)
    bakiye = 12500
    while True:
        
        islem = input("Yapmak istediğiniz işlemi giriniz:")
        
        if(islem == '0'):
            print("Hesabınızdan çıktınız.")
            break
        if(islem == '1'):
           print("Bakiyeniz: {}" .format(bakiye) )
        elif(islem=='2'):
            p_cekme = int(input("Çekmek istediğiniz tutarı giriniz:"))
            print("Para çekme işleminiz gerçekleştirilmiştir: {} TL" .format(p_cekme))
            bakiye -= p_cekme
            print('Kalan bakiyeniz: {}'  .format(bakiye))
        elif(islem == '3'):
            p_yatirma = int(input("Yatırmak istediğiniz tutarı giriniz:"))
            print("{} TL yatırma işleminiz gerçekleştirilmiştir." .format(p_yatirma))
            bakiye +=p_yatirma
            print("Yeni bakiyeniz {} TL'dir." .format(bakiye))