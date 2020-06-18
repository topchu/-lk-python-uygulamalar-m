# Bankamatik Uygulaması

hesaplar = {
    '01': {
        'ad': 'İsmail Topçu',
        'hesapNo': '01',
        'bakiye': 3000,
        'parola': '1595'
    },
    '02': {
        'ad': 'Kamil Bulut',
        'hesapNo': "02",
        'bakiye': 4000,
        'parola': '1234'
    }
}

def deposit(hesap, miktar):
    hesap['bakiye'] += miktar
    print(f"Bakiyeniz: {hesap['bakiye']}")
    print("-"*50)

def whitdraw(hesap, miktar):
    if miktar <= hesap['bakiye']:
        hesap['bakiye'] -= miktar
        print(f"Bakiyeniz: {hesap['bakiye']}")
        print("-"*50)
    else:
        print("İşlem başarısız. (Yetersiz bakiye)")
        print("-"*50)

def bakiyeSorgula(hesap):
    print(f"Bakyeniz: {hesap['bakiye']}")
    print("-"*50)

print("""-Banka-
Kullanıcı girişi""")
girilenHesap = input("Hesap No: ")
girilenParola = input("Parola: ")

if girilenHesap == hesaplar['01']['hesapNo'] and girilenParola == hesaplar['01']['parola']:
    print("Giriş Başarılı.")
    print('-'*50)
    print("""Lütfen işlemi seçiniz.
1. Bakiye sorgulama
2. Para çekme
3. Para yatırma
4. Çıkış""")
    print("-"*50)
    while True:
        işlem = input("İşlem: ")
    
        if işlem == "3":
            miktar = int(input("Bakiyenize yatırmak istediğiniz miktar: "))       
            deposit(hesaplar['01'],miktar)
        elif işlem == "2":
            miktar = int(input("Bakiyenizden çekmek istediğiniz miktar: "))
            whitdraw(hesaplar['01'],miktar)
        elif işlem == "4":
            print("Çıkış yapıldı.")
            exit()
        else:
            bakiyeSorgula(hesaplar['01'])
    
        


elif girilenHesap == hesaplar['02']['hesapNo'] and girilenParola == hesaplar['02']['parola']:
    print("Giriş Başarılı.")
    print('-'*50)
    print("""Lütfen işlemi seçiniz.
1. Bakiye sorgulama
2. Para çekme
3. Para yatırma
4. Çıkış""")
    print("-"*50)
    while True:
        işlem = input("İşlem: ")
    
        if işlem == "3":
            miktar = int(input("Bakiyenize yatırmak istediğiniz miktar: "))       
            deposit(hesaplar['02'],miktar)
        elif işlem == "2":
            miktar = int(input("Bakiyenizden çekmek istediğiniz miktar: "))
            whitdraw(hesaplar['02'],miktar)
        elif işlem == "4":
            print("Çıkış yapıldı.")
            exit()
        else:
            bakiyeSorgula(hesaplar['02'])

else:
    print("Hesap no ya da parola yanlış girildi.")