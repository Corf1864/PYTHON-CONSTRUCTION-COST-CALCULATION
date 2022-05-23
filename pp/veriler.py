import sqlite3
    
veritabani=sqlite3.connect("insaat.db")
imlec=veritabani.cursor()




sorgu1="select * from bolgeler" #burdan itibaren üc satır fonksiyon dışında yukarıdaydı unutursan hata verirse
imlec.execute(sorgu1)
satirlar=imlec.fetchall() 


def bolgeleryazdir():
    
    for i in satirlar:
        print(i[1],"===",i[2])
        
dizi=[]  
def malzemefiyat():
    sorgu2="select * from materials"
    imlec.execute(sorgu2)
    
    for i in imlec.fetchall():
        dizi.append([i[1],i[2]])
    return dizi
       
def makinalar():
    veritabani=sqlite3.connect("insaat.db")
    imlec=veritabani.cursor()
    sorgu="select * from makinalar"
    imlec.execute(sorgu)
    return imlec.fetchall()
    

def malzeme_esg(v):
    
    if v==1:
        print("Malzeme adını yazdıktan sonra alt çizgiden sonra birimini yazınız\n Örnek kablo_5metre veya kum_m^3\n")
        while True:
            
            mtname=input("Yeni malzeme adı giriniz\n")
            mtprice=input("Malzemenin Fiyatını Giriniz\n")
            imlec.execute("insert into materials (material_name,price) values(?,?)",[mtname,mtprice])
            karar=input("Başka Ekleyecek misiniz? evet:hayir\n")
            if karar=="hayir" or karar=="hayır":
                break
            elif karar=="evet":
                continue 
           
    elif v==2:
        x=input("Sistemde Kayitli Malzemenin Tam Adını Giriniz\n")
        imlec.execute("delete from materials where material_name=? ",[x])
  
    elif v==3:
        urunad=input("Güncellemek Istediğiniz Ürünün Adının Giriniz\n")
        t=imlec.execute("select count(id) from materials where material_name=?",[urunad])
        
        if t.fetchall()[0][0]>=1:
            yenifiyat=input("Yeni Fiyat Giriniz\n")
            imlec.execute("update  materials set price=? where material_name=?",[yenifiyat,urunad])
            
        else:
            print("Böyle Bir Kayit Bulunamadı\n")
    veritabani.commit()    
    
def makina_esg(v):
    
    if v==1:
        makina_ad=input("Makina Adını Giriniz\n")
        makina_saatlik=input("Makina Saatlik Ücreti Giriniz\n")
        imlec.execute("insert into makinalar (makina_adi,saatlik_ucret) values(?,?)",[makina_ad,makina_saatlik])
        
    elif v==2:
        m_Ad=input("Sistemde Kayitli Makinanın Tam Adını Giriniz\n")
        imlec.execute("delete from makinalar where makina_adi=? ",[m_Ad])    
        
        
    elif v==3:
        makina_ad=input("Güncellemek İstediginiz Makinenin Adını Giriniz\n")
        t=imlec.execute("select count(id) from makinalar where makina_adi=?",[makina_ad])
        if (t.fetchall()[0][0]>=1):
            yeni_fiyat=input("Seçilen Makinenin Saatlik Ücretini Giriniz\n")
            imlec.execute("update makinalar set saatlik_ucret=? where makina_adi=?",[yeni_fiyat,makina_ad])
            
        else:
            print("Girilen isimde bir sonuç bulunamadı\n")
    
    veritabani.commit()    

def personel():
    yeni=imlec.execute("select unvan,saatlik_ucret from personel")
    veritabani.commit()
    return yeni.fetchall()



veritabani.commit()

