import veriler
import maliyet,uyelikislemleri
giriskontrol=0

while True:
    giris=int(input("Üyelik Al:0\nÜye Girişi:1\nÇıkış:2\n"))
    if giris==0:
        uyelikislemleri.uyekayit()
    
    elif giris==1:
        giriskontrol=uyelikislemleri.uyegiris()
        
        if giriskontrol==1:
            break
    
       

if giriskontrol==1:
  
    while True:
        print("Insaat Maliyet-Fiyat Hesaplama\n")
        print("Yapmak Istediginiz Islemi seciniz\n")
    
        
        secim=int(input("""
        1:bölgelere göre arazi fiyatlarını incele
        2:Malzeme Fiyatlarini Incele
        3:Maliyet Hesabini Cikar
        4:Makina Saatlik Fiyatlarını Güncelle ya da Yeni Makina Ekle
        5:Malzeme Ekle/Sil/Güncelle
        6:Personel Ekle/Sil/Güncelle
        13:Çıkış Yap\n"""))   
       
        
        
                        
        if secim==1:#arazi fiyatlarÄ±nÄ± listeler
            veriler.bolgeleryazdir()
                
        
        elif secim==2:
            print("malzeme fiyatri\n")
            malzemeler=veriler.malzemefiyat()
            for i in malzemeler:
                print(i)
            
                
        elif secim==3:
            maliyet.maliyetgenelhesap()
        
        elif secim==4:
            makinakarar=int(input("Makina Ekle:1\n Makina Sil:2\n Fiyat Güncelle:3\n"))
            if makinakarar==1:
                veriler.makina_esg(1)
            elif makinakarar==2:
                veriler.makina_esg(2)
            elif makinakarar==3:
                veriler.makina_esg(3)
            
            
        elif secim==5:
            print("Projenizde Kullanılacak Malzemeler ve Fiyatları\n")
            for k in veriler.malzemefiyat():
                print(k)    
            esg=int(input(" Ekleme:1\n Silme:2\n Güncelle:3\n"))
            if esg==1:
                veriler.malzeme_esg(1)
            elif esg==2:
                veriler.malzeme_esg(2)
            elif esg==3:
                veriler.malzeme_esg(3)    
           
        elif secim==13:
            break

#sözlüge proje adı maliyetleri yazdırdım onları veritabanina kaydedicem ve class eklemem gerekiyor
    
            
            
                    
   
            
    
   
        
    
  
 

