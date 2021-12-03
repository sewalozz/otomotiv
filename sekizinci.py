# OBJECT ORIENTED PROGRAMMING
# NESNE TABANLI PROGRAMLAMA

# a = 8;
# print(a.bit_length())
# print(type(a))

# araba = ["renk","motor","marka","model","segment" ,"yil"]
# araba = {"renk":"kırmızı","motor":2000,"marka":"fiat",
# "model":"doblo","segment":"ticari" ,"yil":2011}

# print( type(araba) )
import math
class araba():
    renk = "kırmızı"
    motor = None
    marka = "fiat";
    model = segment = yil = None
    # metod
    def vergi_hesapla(self):
        if self.motor < 2000 :
            return self.motor*1.2
        else :
            return self.motor * 2.4
    #constructor
    def __init__(self,motor) :
        self.motor = motor
        # print("Nesne oluşturuldu.")
    # destructor
    def __del__(self) :
        pass
        # print("Silindi!")

    

# print("henüz a nesnesi yok")
# a = araba()
# a.renk = "Mavi"
# print("a nesnesi oluşturuldu.")
# del a
# print("Silindikten sonra.")
# print( type(a) , a.renk )

arabam = araba(1200)
arabam.renk = "Mavi"
# arabam.motor = 1200
arabam.marka = "Renault"
arabam.model = "Clio"
arabam.yil = 2018
arabam.segment = "Hususi"

# print( "Markası: {}, Modeli: {}".format( arabam.marka , arabam.model  ) )

class kamyon (araba) :
    tonaj = None # NULL null

class tir (kamyon) :
    romork = None

km = kamyon(5700)
# print(km.renk)

tr = tir(12_000)
# tr.motor = 10_000
tr.tekerlek = 15
# print(tr.renk,tr.tekerlek )

#print(tr.vergi_hesapla(), km.vergi_hesapla() )

# motor_bilgisi = int ( input ("Motor hacmini giriniz.\n"))

# x = araba(motor_bilgisi)

# print("Ödemeniz gereken vergi:{}".format(x.vergi_hesapla()))






