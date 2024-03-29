import requests
from bs4 import BeautifulSoup

"""
OOP            <->     Procedural

obeject(class)
Methode         =      Fungsi
Field/Attribute =      variable
Constructor = method yang pertama kali dipanggil saat object diciptakan. Gunakan untuk 
              mendeklarasikan semua field pada class ini
"""


class Bencana:  # class
    def __init__(self, url, description):  # Methode
        self.description = description
        self.result = None
        self.url = url

    def tampilkan_keterangan(self):
        print(self.description)

    def scraping_data(self):
        print('Not yet implemented')

    def tampilkan_data(self):
        print('Not yet implemented')

    def run(self):
        self.scraping_data()
        self.tampilkan_data()


class BanjirTerkini(Bencana):
    def __init__(self, url):
        super(BanjirTerkini, self).__init__(url, 'NOT YET IMPLEMENTED, but it shoud return last flood in Indonesia')

    def tampilkan_keterangan(self):
        print('UNDER CONSTRUCTION', self.description)


class GempaTerkini(Bencana):
    def __init__(self, url):
        super(GempaTerkini, self).__init__(url, 'to get the latest earthquake in Indonesia from BMGK.go.id')

    def scraping_data(self):
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

    # def run(self):
    #     self.scraping_data()
    #     self.tampilkan_data()


if __name__ == "__main__":
    gempa_di_indonesia = GempaTerkini('https://www.bmkg.go.id/')
    gempa_di_indonesia.tampilkan_keterangan()
    gempa_di_indonesia.run()
    # gempa_di_indonesia.ektraksi_data()
    # gempa_di_indonesia.tampilkan_data()

    banjir_di_indonesia = BanjirTerkini('NOT YET')
    banjir_di_indonesia.tampilkan_keterangan()
    banjir_di_indonesia.run()

    daftar_bencana = [gempa_di_indonesia, banjir_di_indonesia]
    print('\nSemua bencana yang ada')
    for bencana in daftar_bencana:
        bencana.tampilkan_keterangan()



