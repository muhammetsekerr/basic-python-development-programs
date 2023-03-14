print('Hesap Makinesine Hoşgeldiniz')

birinciSayi = int(input('Bir sayı giriniz:'))
islem = input('Yapmak istediğiniz işlemi giriniz:')
ikinciSayi= int(input('Bir sayı giriniz:'))

if(islem == '+'):
    print(birinciSayi + ikinciSayi)
if(islem == '-'):
    print(birinciSayi - ikinciSayi)
if(islem == '*'):
    print(birinciSayi * ikinciSayi)
if(islem == '/'):
    print(birinciSayi / ikinciSayi)
