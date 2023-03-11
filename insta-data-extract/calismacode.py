from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

URL = ("https://www.instagram.com/")

def veri_cek(kullanici_adi):
    son_url = URL + kullanici_adi

    request = Request(son_url,headers={'User-Agent':'Mozilla/5.0'})
    html_veri = urlopen(request).read()

    soup = BeautifulSoup(html_veri, 'html.parser')

    veri = soup.find("meta", property='og:description').attrs['content']

    veri.split("-")[0]

    veri = veri.split(" ")

    print("Takipci sayısı: "+veri[0])
    print("Takip Edilen: "+veri[2])
    print("Gönderi Sayısı: "+veri[4])


kullanici_adi = input("Kullanıcı adı giriniz: ")
veri_cek(kullanici_adi)