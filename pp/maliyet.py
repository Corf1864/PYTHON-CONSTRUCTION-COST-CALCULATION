import veriler


x=0
plaka=0
metrekare=0
genelmaliyet={}

malzemeler=[]


#bunlara ek olarak işçilik araç kullanımı masrafları mühendislik ücretleri eklenecek 
#görsel olarak rastgele mimari tasarım yapılacak 
#malzemelere ekleme yapılacak 

def malzemehesap():
    
   kayit=[]
   toplam_malzeme=0
   # print(veriler.malzemefiyat()) #veritabanından malzeme fiyatlarını çekiyorum
   malzemeler=veriler.malzemefiyat()
   
 
   for i in malzemeler:
       
       x=int(input(f"{i[0]}:\n"))
       kayit.append(x)
       toplam_malzeme+= x* int(i[1])
      
      
       
   genelmaliyet.setdefault("malzememaliyet",toplam_malzeme)  


#şimdilik tek katmış gibi hesap yapılıyor ilerleyen zamanlarda kat sistemi eklenebilir

def personelmaliyehesap():
    personel={}
    
    karar="yes"
    dizi=["mimar","muhendis","usta"]
    
    
    
    print("Lütfen Aşağıdaki Bilgileri Boşlık Bırakarak Doldurunuz. Yoksa Bilgileri 0 giriniz\n\n")

    for i in range(len(dizi)):
        degisken1={}
        bos=input(f"{dizi[i]}// Çalışan Sayısı:Saatlik Ücreti:Kaç Gün Çalışacak\n")

        degisken1.setdefault("calisansayisi:",bos.split(" ")[0])
        degisken1.setdefault("saatlikucret:",bos.split(" ")[1])
        degisken1.setdefault("kacgun:",bos.split(" ")[2])

        personel.setdefault(dizi[i],degisken1)
        
    sayac=0
    
    #diziye ekstra meslek gurubu eklemek icin while yazıldı
    while karar=="yes":
        karar=input("Sisteme Başka Alanda Çalışan Peronel Eklemek İstiyor musunuz?\n yes:no ")
        if karar=="yes":
            dizi.append(input("Meslek Grubunu giriniz: "))
            sayac+=1
            
        elif karar=="no":
            break

    for j in range(sayac):
        degisken2={}
        bos=input(f"{dizi[len(dizi)-sayac +j]}// Çalışan Sayısı:Saatlik Ücreti:Kaç Gün Çalışacak\n")

        degisken2.setdefault("calisansayisi:",bos.split(" ")[0])
        degisken2.setdefault("saatlikucret:",bos.split(" ")[1])
        degisken2.setdefault("kacgun:",bos.split(" ")[2])

        personel.setdefault(dizi[len(dizi)-sayac +j],degisken2)

    
    #////////////////////////////////////////////////////////////// buraya kadar  veri girişiydi
    #burdan sonra hesap

    toplampersonelmasraf=0

    for k in personel:
        
        toplampersonelmasraf+=(int(personel[k]["saatlikucret:"]) * int(personel[k]["kacgun:"]) *int(personel[k]["calisansayisi:"]))*8
    print(toplampersonelmasraf)

    genelmaliyet.setdefault("personelmaliyeti",toplampersonelmasraf)
    

def makinamaliyet():
    
    makinatoplampara=0
    
    print("Aşağıdaki Makinaların Çalışma Süresini Giriniz. \n")
    
    makinalist=veriler.makinalar()
    for i in range(len(makinalist)):
        
        u=int(input(f"{makinalist[i][1]}="))
        
        makinatoplampara+=u*int(makinalist[i][2])
    
    genelmaliyet.setdefault("makinemaliyet",makinatoplampara)
    
    
def maliyetgenelhesap():
    
      
    genelmaliyet.setdefault("projeadi",input("Projenizin Adını Giriniz\n"))
    
    plaka=int(input("nerede yapilacak plaka kodunu giriniz\n"))
    metrekare=int(input("arazi ham metrekare giriniz\n"))

    
    arsamaliyet=int(veriler.satirlar[plaka-1][2])* metrekare
    
    print("lütfen aşağıdaki malzemelerin gerektiği ölçüde giriniz\n")
    
    malzemehesap()
    
    personelmaliyehesap()
    
    makinamaliyet()
    
    
    genelmaliyet.setdefault("ruhsatmaliyet",input("Ruhsat Masraflarını Giriniz\n"))
    genelmaliyet.setdefault("diger",input("Diğer Giderleri Ekle\n"))
    genelmaliyet.setdefault("arsamaliyet",arsamaliyet)
    
    marj=int(input("Yüzde Kaç Kar Oranı Girmek İstersin?\n"))
    
    class kayit():
        projeAdi=""
        personelMaliyet=0
        malzemeMaliyet=0
        makineMaliyet=0
        arsaMaliyet=0
        ruhsatMaliyet=0
        diger=0
        satisfiyati=0
        
        def __init__(self):
            import sqlite3
            veritabani=sqlite3.connect("insaat.db")
            im=veritabani.cursor()
            
            
            self.projeAdi=genelmaliyet["projeadi"]
            self.malzemeMaliyet=int(genelmaliyet["malzememaliyet"])
            self.makineMaliyet=int(genelmaliyet["makinemaliyet"])
            self.personelMaliyet=int(genelmaliyet["personelmaliyeti"])    
            self.arsaMaliyet=int(genelmaliyet["arsamaliyet"])
            self.ruhsatMaliyet=int(genelmaliyet["ruhsatmaliyet"])
            self.diger=int(genelmaliyet["diger"])
            
            
            
            toplam=int(self.malzemeMaliyet+self.makineMaliyet+self.personelMaliyet+self.arsaMaliyet+self.ruhsatMaliyet+self.diger)
            self.satisfiyati=int(((toplam*marj)/100) +toplam)
            genelmaliyet.setdefault("toplam",self.satisfiyati)
            
            im.execute("insert into projekayit (projeadi,malzememaliyet,makinamaliyet,personelmaliyet,arsamaliyet,ruhsatmaliyet,diger,satisfiyati) values(?,?,?,?,?,?,?,?)",
                       [self.projeAdi,self.malzemeMaliyet,self.makineMaliyet,self.personelMaliyet,self.arsaMaliyet,self.ruhsatMaliyet,self.diger,self.satisfiyati])
            veritabani.commit()
            
            print("*" *70,"\n")
            print("Proje Adı:",self.projeAdi,"\n")
            print("Proje Arsa Maliyet:",self.arsaMaliyet,"\n")
            print("Proje Malzeme Maliyet:",self.malzemeMaliyet,"\n")
            print("Proje Makina Maliyet:",self.makineMaliyet,"\n")
            print("Proje Personel Maliyet:",self.personelMaliyet,"\n")
            print("Proje Ruhsat Maliyet:",self.ruhsatMaliyet,"\n")
            print("Proje Diger Maliyet:",self.diger,"\n")
            print("Proje Satış Fiyatı:",self.satisfiyati,"\n")
            print("*" *70)
            
            
            
    kayit()
    
    
    
    
    
    

