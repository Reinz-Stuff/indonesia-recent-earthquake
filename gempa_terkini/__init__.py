import requests
from bs4 import BeautifulSoup

"""
OOP            <->     Procedural

obeject(class)
Methode         =      Fungsi
Field/Attribute =      variable
"""


class GempaTerkini:
    def __init__(self, url):
        self.description = 'to get the latest earthquake in Indonesia from BMGK.go.id'
        self.result = None
        self.url = url

    def ektraksi_data(self):
        try:
            content = requests.get(self.url)
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
            self.result = hasil
        else:
            return None

    def tampilkan_data(self):
        if self.result is None:
            print('Tidak menemukan data gempa terkini')
            return
        print("Gempa terakhir berdasarkan BMKG")
        print(f"Tanggal {self.result['tanggal']}")
        print(f"waktu {self.result['waktu']}")
        print(f"Magnitudo {self.result['magnitudo']}")
        print(f"Kedalaman {self.result['kedalaman']}")
        print(f"koordinat: ls= {self.result['koordinat']['ls']} bt= {self.result['koordinat']['bt']}")
        print(f"Lokasi {self.result['lokasi']}")
        print(f"{self.result['dirasakan']}")

    def run(self):
        self.ektraksi_data()
        self.tampilkan_data()


if __name__ == "__main__":
    gempa_di_indonesia = GempaTerkini('https://www.bmkg.go.id/')
    print('Deskripsi class', gempa_di_indonesia.description)
    gempa_di_indonesia.run()
    # gempa_di_indonesia.ektraksi_data()
    # gempa_di_indonesia.tampilkan_data()

if __name__ == "__main__":
    gempa_di_dunia = GempaTerkini('https://www.bmkg.go.id')
    print('Deskripsi class', gempa_di_dunia.description)
    gempa_di_dunia.run()

# self url
