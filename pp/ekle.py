import sqlite3
veritabani=sqlite3.connect("insaat.db")
imlec=veritabani.cursor()


makina_ad=input("Makina Adını Giriniz\n")
makina_saatlik=input("Makina Saatlik Ücreti Giriniz\n")
imlec.execute("insert into makine (makine_ad,saatlik_fiyat) values(?,?)",[makina_ad,makina_saatlik])


"""
sorgu=create table  makinalar(id INTEGER PRIMARY KEY AUTOINCREMENT,
                             makina_adi,
                             saatlik_ucret
                             )

"""


veritabani.commit()
