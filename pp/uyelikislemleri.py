import sqlite3

veritabani=sqlite3.connect("insaat.db")
imlec=veritabani.cursor()


def uyekayit():

    sirket_ad=input("Şirket adı giriniz\n")
    sirket_tel=input("Şirket telefon giriniz\n")
    sirket_email=input("Şirket e mail adresini giriniz\n")
    sirket_faks=input("Şirket faks numarasini giriniz\n")
    sirket_personel_sayisi=input("Şirket personel sayisini giriniz\n")
    sirket_adres=input("Şirket adresini giriniz\n")
    sirket_pass=input("Lütfen bir şifre belirleyiniz\n")
    
    
    imlec.execute("""insert into uyelik(company_name,company_phone,company_email,company_fax,company_adress,company_staffcount,company_password)
            values(?,?,?,?,?,?,?)""",[sirket_ad,sirket_tel,sirket_email,sirket_faks,sirket_personel_sayisi,sirket_adres,sirket_pass])
    veritabani.commit()
    
    

def uyegiris():
    
    email=input("Lütfen sistemdeki e-mail adresini giriniz\n")
    sifre=input("Lütfen şifrenizi giriniz\n")
    
    imlec.execute("select company_email,company_password from uyelik")
    loglist=imlec.fetchall()
    veritabani.commit()
  
    
    for k in loglist:
       if k[0]==email and k[1]==sifre:
           return 1
       
    
       

veritabani.commit()