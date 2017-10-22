import requests,re,sys

def temaTespit(site):
    şablon = 'wp-content/themes/(.*?)/style.css'
    kaynak = requests.get(site).text
    temaİsmi = re.findall(şablon,kaynak)
    return temaİsmi[0]

def temaBilgi(site):
    siteKaynak = requests.get(site+"/wp-content/themes/"+temaTespit(site)+"/style.css").text
    temaİsmi = re.findall("Theme Name: (.*?)\n", siteKaynak)
    temaLink = re.findall("Theme URI: (.*?)\n", siteKaynak)
    temaSahip = re.findall("Author: (.*?)\n",siteKaynak)
    temaVersiyon = re.findall("Version: (.*?)\n", siteKaynak)
    temaLicense = re.findall("License: (.*?)\n", siteKaynak)
    bilgiler = "TEMA İSMİ: {}\nTEMA LİNK: {}\nTEMA SAHİBİ: {}\nTEMA VERSİYON: {}\nTEMA LİSANS: {}\n".format(temaİsmi[0],temaLink[0],temaSahip[0],temaVersiyon[0],temaLicense[0])
    return bilgiler
 

print(temaBilgi(sys.argv[1]))


