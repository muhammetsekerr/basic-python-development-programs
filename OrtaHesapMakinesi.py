print("""Hesap Makinesi
      [1] Toplama İşlemi
      [2] Çıkarma İşlemi
      [3] Çarpma İşlemi
      [4] Bölme İşlemi
      [5] Üs alma
      [6] Mod Alma
      """)

giris = input("Yapmak istediğiniz seçiniz:")

if giris == "1":
    x = input("İşlem yapacağınız ilk sayıyı giriniz: ")
    x = float(x)
    y = input("İşlem yapacağınız ikinici sayıyı giriniz: ")
    y = float(y)

    print("İşlem sonucunuz: ", x+y)

if giris == "2":
    x = input("İşlem yapacağınız ilk sayıyı giriniz: ")
    x = float(x)
    y = input("İşlem yapacağınız ikinici sayıyı giriniz: ")
    y = float(y)

    print("İşlem sonucunuz: ", x-y)

if giris == "3":
    x = input("İşlem yapacağınız ilk sayıyı giriniz: ")
    x = float(x)
    y = input("İşlem yapacağınız ikinici sayıyı giriniz: ")
    y = float(y)

    print("İşlem sonucunuz: ", x*y)

if giris == "4":
    x = input("İşlem yapacağınız ilk sayıyı giriniz: ")
    x = float(x)
    y = input("İşlem yapacağınız ikinici sayıyı giriniz: ")
    y = float(y)

    print("İşlem sonucunuz: ", x/y)

if giris == "5":
    x = input("İşlem yapacağınız ilk sayıyı giriniz: ")
    x = float(x)
    y = input("İşlem yapacağınız ikinici sayıyı giriniz: ")
    y = float(y)

    print("İşlem sonucunuz: ", x**y)

if giris == "6":
    x = input("İşlem yapacağınız ilk sayıyı giriniz: ")
    x = float(x)
    y = input("İşlem yapacağınız ikinici sayıyı giriniz: ")
    y = float(y)

    print("İşlem sonucunuz: ", x%y)
    