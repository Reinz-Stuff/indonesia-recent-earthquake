import requests
from bs4 import BeautifulSoup

description = 'to get the latest earthquake in Indonesia from BMGK.go.id'


def ektraksi_data():
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        page = soup.find('span', {'class': 'waktu'})
        page = page.text.split(', ')
        tanggal = page[0]
        waktu = page[1]

        page = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        page = page.findChildren('li')

        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in page:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak menemukan data gempa terkini')
        return
    print("Gempa terakhir berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"koordinat: ls= {result['koordinat']['ls']} bt= {result['koordinat']['bt']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"{result['dirasakan']}")


if __name__ == "__main__":
    print('Deskripsi package', description)
    result = ektraksi_data()
    tampilkan_data(result)

#add tags